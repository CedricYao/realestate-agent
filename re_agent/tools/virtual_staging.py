import google.generativeai as genai
from google.adk.tools import tool
from PIL import Image

# Configure the generative AI library to use Vertex AI
genai.configure(
    project="csaw-workshop1",
    location="us-central1",
)

@tool
def stage_image(image_path: str, style_prompt: str) -> str:
    """Virtually stages an image with furniture based on a style prompt."""

    try:
        print(f"Staging image at {image_path} with style: {style_prompt}")

        # Load the image
        img = Image.open(image_path)

        # Create the generative model
        model = genai.GenerativeModel("gemini-pro-vision")

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
