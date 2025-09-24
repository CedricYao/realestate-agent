from google.genai import Client
from google.adk.tools import FunctionTool
from PIL import Image
import io

def stage_image_func(image, style_prompt: str) -> str:
    """Virtually stages an image with furniture based on a style prompt."""

    try:
        print(f"Staging image with style: {style_prompt}")

        # Initialize the client for Vertex AI
        client = Client(
            vertexai=True,
            project="csaw-workshop1",
            location="us-central1",
        )

        # The image will be passed as bytes from the ADK web interface
        img = Image.open(io.BytesIO(image))

        # Get the generative model
        model = client.get_model("gemini-pro-vision")

        # Generate content
        response = model.generate_content([style_prompt, img])

        return response.text

    except Exception as e:
        return f"An error occurred: {e}"

stage_image = FunctionTool(stage_image_func)