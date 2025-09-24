
from google import genai
from google.genai import types
from PIL import Image

def stage_image(image_path: str, style_prompt: str) -> str:
    """
    Virtually stages an image with furniture based on a style prompt.

    Args:
        image_path: The path to the image to stage.
        style_prompt: A text prompt describing the desired style.

    Returns:
        The path to the generated image.
    """
    try:
        print(f"Staging image at {image_path} with style: {style_prompt}")

        # Initialize the client. It will automatically use Vertex AI
        # configuration from the environment variables.
        client = genai.Client()

        # Open the user's uploaded image
        img = Image.open(image_path)

        # Create a reference to the uploaded image
        raw_ref_image = types.RawReferenceImage(
            reference_id="1",
            reference_image=img,
        )

        # Create a mask of the entire image to allow for general staging
        # For a more advanced implementation, this could be a specific area.
        mask_ref_image = types.MaskReferenceImage(
            reference_id="2",
            config=types.MaskReferenceConfig(
                mask_mode='MASK_MODE_BACKGROUND',
                mask_dilation=0,
            ),
        )

        # Call the edit_image API
        response = client.models.edit_image(
            model='imagen-3.0-capability-001',
            prompt=style_prompt,
            reference_images=[raw_ref_image, mask_ref_image],
            config=types.EditImageConfig(
                edit_mode='EDIT_MODE_INPAINT_INSERTION',
                number_of_images=1,
            ),
        )

        if response.generated_images:
            generated_image = response.generated_images[0]
            # The image data is in generated_image.image.image_bytes
            # For simplicity, we'll save it and return the path.
            output_path = f"staged_{image_path.split('/')[-1]}"
            with open(output_path, "wb") as f:
                f.write(generated_image.image.image_bytes)
            print(f"Saved staged image to {output_path}")
            return output_path
        else:
            print("Image generation failed. No images were returned.")
            return ""

    except Exception as e:
        print(f"An error occurred during image staging: {e}")
        return ""

