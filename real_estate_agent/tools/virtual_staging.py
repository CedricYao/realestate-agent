
import io
import os
import uuid
from typing import Dict, Any
from io import BytesIO
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image
from google.adk.tools import ToolContext

load_dotenv()
project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
location = "global"

async def stage_image(
    tool_context: ToolContext, 
    style_prompt: str = "mid-century modern"
) -> Dict[str, Any]:
    """Virtually stages an image with furniture based on a style prompt.

    This tool takes an image as bytes and uses a generative AI model to edit it
    based on the provided style prompt.

    Args:
        tool_context: The context object provided by the ADK framework, containing state.
        style_prompt: A text prompt describing the desired style of furniture.

    Returns:
        {
          "status": "success",
          "detail": "...",
          "filenames": ["filename.png", ...],
        }
    """
    print("------------------------------------------------")
    artifact_ids = await tool_context.list_artifacts()

    # Get the first artifact ID from the list which is the doc uploaded by the user
    artifact_id = artifact_ids[0]
    print(f"Reading artifact with ID: {artifact_id}")

    try:
        print(f"Staging image with style: {style_prompt}")
        artifact_content = await tool_context.load_artifact(artifact_id)
        print( "The doc type: ", artifact_content.inline_data.mime_type )
        image_data = artifact_content.inline_data.data

        client = genai.Client(vertexai=True, project=project_id, location=location)

        image_stream = io.BytesIO(image_data)
        image = Image.open(image_stream)

        response = client.models.generate_content(
            model="gemini-2.5-flash-image-preview",
            contents=[style_prompt, image],
        )
        print("Received response from model.")
        
        for part in response.candidates[0].content.parts:
            if part.text is not None:
                print(part.text)
                return ("no parts with text found in response")
            elif part.inline_data is not None:
                image_bytes = part.inline_data.data
                filename = f"staged_image_{uuid.uuid4()}.jpeg"
                await tool_context.save_artifact(
                    filename, types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")
                )
                print(f"Saved artifact {filename}")

                detail = (
                    "Images generated via nano banna; bytes saved as artifacts."
                    if filename
                    else "Images generated via nano banana; artifacts not saved (download failed)."
                )

                return {
                    "status": "success",
                    "detail": detail,
                    "filenames": filename,  # artifact filenames you can reference later
                }
        return {
            "status": "failed",
            "detail": "Image generation failed. No images were returned.",
            "filenames": "",  # artifact filenames you can reference later
        }
        return 

    except Exception as e:
        return f"An error occurred during image staging: {e}"
