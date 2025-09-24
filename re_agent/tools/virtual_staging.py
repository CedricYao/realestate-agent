from google.genai import Client
from google.adk.tools import FunctionTool
from PIL import Image

def stage_image_func(image_path: str, style_prompt: str) -> str:
    """Virtually stages an image with furniture based on a style prompt."""

    try:
        print(f"Staging image at {image_path} with style: {style_prompt}")

        # Initialize the client for Vertex AI
        client = Client(
            vertexai=True,
            project="csaw-workshop1",
            location="us-central1",
        )

        # Load the image
        img = Image.open(image_path)

        # Get the generative model
        model = client.get_model("gemini-pro-vision")

        # Generate content
        response = model.generate_content([style_prompt, img])

        # For this example, we'll just return the generated text.
        # In a real application, you might upload the generated image to a bucket
        # and return the URL.
        return response.text

    except FileNotFoundError:
        return f"Error: Image file not found at {image_path}"
    except Exception as e:
        return f"An error occurred: {e}"

stage_image = FunctionTool(stage_image_func)
