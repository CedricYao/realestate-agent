
import io
import os
import uuid
from io import BytesIO
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

load_dotenv()
project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
location = os.getenv("GOOGLE_CLOUD_LOCATION") # needs to be set to 'global'

def stage_image() -> str:
    """Virtually stages an image with furniture based on a style prompt.

    This tool takes an image as bytes and uses a generative AI model to edit it
    based on the provided style prompt.

    Args:
        image_data: The image data in bytes.
        mime_type: The mime type of the image.
        style_prompt: A text prompt describing the desired style of furniture.
    """
    try:
        client = genai.Client(vertexai=True, project=project_id, location=location)
        
        with open("tests/living_room.jpeg", "rb") as f:
            image_bytes = f.read()

        image_stream = io.BytesIO(image_bytes)
        img_stream = Image.open(image_stream)
        prompt = "add a comfy sofa and modern art"

        response = client.models.generate_content(
            model="gemini-2.5-flash-image-preview",
            contents=[prompt, img_stream],
        )
        print("Received response from model.")
        
        for part in response.candidates[0].content.parts:
            if part.text is not None:
                print(part.text)
                return ("no parts with text found in response")
            elif part.inline_data is not None:
                image = Image.open(BytesIO(part.inline_data.data))
                image.save("generated_image.png")
                return "Image generation failed. No images were returned."

    except Exception as e:
        return f"An error occurred during image staging: {e}"

stage_image()

