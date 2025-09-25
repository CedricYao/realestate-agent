import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from unittest.mock import AsyncMock
from google.genai import types
from agents_gallery.real_estate_agent.tools.virtual_staging import stage_image
import os

@pytest.mark.asyncio
async def test_stage_image_success():
    """Tests the stage_image function with a mocked tool context."""
    # Arrange
    # The user has indicated that the virtual staging tool is working correctly.
    # We will mock the tool context to pass the image data to the tool.
    # The test will still make a real API call to the generative model.
    with open("tests/living_room.jpeg", "rb") as f:
        image_bytes = f.read()

    mock_tool_context = AsyncMock()
    mock_tool_context.list_artifacts.return_value = ["test_artifact_id"]
    
    artifact_part = types.Part(inline_data=types.Blob(data=image_bytes, mime_type="image/jpeg"))
    mock_tool_context.load_artifact.return_value = artifact_part

    # Act
    result = await stage_image(tool_context=mock_tool_context, style_prompt="add a comfy sofa and modern art")

    # Assert
    assert result["status"] == "success"
    assert "staged_image" in result["filenames"]
    
    mock_tool_context.save_artifact.assert_called_once()
    saved_artifact_name = mock_tool_context.save_artifact.call_args[0][0]
    saved_artifact_part = mock_tool_context.save_artifact.call_args[0][1]
    
    assert saved_artifact_name == result["filenames"]
    assert isinstance(saved_artifact_part, types.Part)
    assert saved_artifact_part.inline_data.data is not None
    assert saved_artifact_part.inline_data.mime_type == "image/jpeg"