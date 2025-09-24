import unittest
from unittest.mock import patch, MagicMock
from real_estate_agent.tools.virtual_staging import stage_image
import os
from PIL import Image

class TestVirtualStaging(unittest.TestCase):

    @patch('real_estate_agent.tools.virtual_staging.genai.Client')
    def test_stage_image_success(self, MockClient):
        """Tests the stage_image function with a mocked client."""
        # Arrange
        mock_client_instance = MockClient.return_value
        mock_generated_image = MagicMock()
        mock_generated_image.image.image_bytes = b'test-image-data'
        mock_response = MagicMock()
        mock_response.generated_images = [mock_generated_image]
        mock_client_instance.models.edit_image.return_value = mock_response

        # Create a dummy image file for the test
        dummy_image_path = "test_image.png"
        img = Image.new('RGB', (1, 1), color = 'red')
        img.save(dummy_image_path, 'PNG')

        # Act
        result_path = stage_image(dummy_image_path, "modern furniture")

        # Assert
        self.assertTrue(result_path.startswith("staged_"))
        mock_client_instance.models.edit_image.assert_called_once()
        with open(result_path, "rb") as f:
            self.assertEqual(f.read(), b'test-image-data')

        # Clean up created files
        os.remove(dummy_image_path)
        os.remove(result_path)

    @patch('real_estate_agent.tools.virtual_staging.genai.Client')
    def test_stage_image_failure(self, MockClient):
        """Tests that the function handles API failures gracefully."""
        # Arrange
        mock_client_instance = MockClient.return_value
        mock_client_instance.models.edit_image.side_effect = Exception("API Error")

        dummy_image_path = "test_image_fail.png"
        with open(dummy_image_path, "w") as f:
            f.write("dummy image content")

        # Act
        result_path = stage_image(dummy_image_path, "modern furniture")

        # Assert
        self.assertEqual(result_path, "")

        # Clean up
        os.remove(dummy_image_path)

if __name__ == '__main__':
    unittest.main()