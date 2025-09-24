# Feature Implementation Plan: Real Estate AI Agent

## 📋 Todo Checklist
- [ ] Set up project structure and dependencies.
- [ ] Implement the core ADK agent.
- [ ] Implement the Home Search tool with a mock API.
- [ ] Implement the Virtual Staging tool using Vertex AI.
- [ ] Create an application entrypoint to run the agent.
- [ ] Write unit and integration tests.
- [ ] Final Review and Testing.

## 🔍 Analysis & Investigation

### Codebase Structure
The current project is empty, containing only documentation and license files. The plan will establish a new Python project structure. The proposed structure will be:

```
/
├── agent.py           # Core ADK Agent definition
├── main.py            # Entrypoint to run the application
├── requirements.txt   # Python dependencies
├── .env.example       # Example environment variables
├── tools/
│   ├── __init__.py
│   ├── home_search.py
│   └── virtual_staging.py
└── tests/
    ├── __init__.py
    ├── test_home_search.py
    └── test_virtual_staging.py
```

### Current Architecture
The architecture will be built from the ground up based on the design document. It will be a Python application centered around the Google Agent Development Kit (ADK). The core agent will leverage two main tools: one for searching homes and another for virtual staging. The system will integrate with external services: a real estate API and Google's Vertex AI for image generation.

### Dependencies & Integration Points
- **Google Agent Development Kit (ADK):** The primary framework for building the conversational agent (`google-adk`).
- **Google Cloud AI Platform:** Required for the virtual staging feature (`google-cloud-aiplatform`).
- **Requests:** For making HTTP calls to the external real estate API (`requests`).
- **Pillow:** For image manipulation if required by the staging tool (`Pillow`).
- **Pytest:** For running tests (`pytest`).
- **External Real Estate API:** An API like Zillow or Realtor.com needs to be chosen. The plan will start with a mock interface to avoid dependency on a specific API key during initial development.

### Considerations & Challenges
- **API Selection:** A specific, reliable real estate API needs to be selected and subscribed to. The associated costs and rate limits must be considered.
- **Vertex AI Authentication:** The application needs to be properly authenticated to use the Vertex AI API. This will require setting up a Google Cloud project and handling credentials, likely via `gcloud auth application-default login`.
- **Prompt Engineering:** The quality of the virtual staging will heavily depend on the prompts sent to the Vertex AI model. The agent may need logic to refine user input into effective prompts.
- **Error Handling:** Robust error handling is needed for API calls (both real estate and Vertex AI) to manage network issues, invalid user input, and API errors gracefully.

## 📝 Implementation Plan

### Prerequisites
1.  Set up a Python 3.9+ virtual environment.
2.  Create a Google Cloud Platform project and enable the Vertex AI API.
3.  Install the Google Cloud SDK and run `gcloud auth application-default login` to authenticate.

### Step-by-Step Implementation
1.  **Step 1: Project Setup**
    - Files to create: `requirements.txt`, `main.py`, `agent.py`, `tools/__init__.py`, `tools/home_search.py`, `tools/virtual_staging.py`
    - Changes needed:
        - Create the directory structure as outlined in the analysis.
        - In `requirements.txt`, add the following dependencies:
          ```
          google-adk
          google-cloud-aiplatform
          requests
          Pillow
          pytest
          ```
        - Install the dependencies: `pip install -r requirements.txt`.

2.  **Step 2: Implement Core ADK Agent**
    - Files to modify: `agent.py`
    - Changes needed:
        - Define the `RealEstateAssistant` agent using the ADK.
        - Configure its name, description, and the Gemini model as specified in the design document.
        - Leave placeholders to add the tools in the subsequent steps.

3.  **Step 3: Implement Home Search Tool**
    - Files to modify: `tools/home_search.py`, `agent.py`
    - Changes needed:
        - In `tools/home_search.py`, implement the `search_homes(zip_code: str, max_price: int) -> list` function.
        - For the initial implementation, use a mock response. The function should return a hardcoded list of property dictionaries to simulate an API call.
        - In `agent.py`, import and register the `HomeSearchTool` with the `RealEstateAssistant` agent.

4.  **Step 4: Implement Virtual Staging Tool**
    - Files to modify: `tools/virtual_staging.py`, `agent.py`
    - Changes needed:
        - In `tools/virtual_staging.py`, implement the `stage_image(image_path: str, style_prompt: str) -> str` function.
        - This function will use the `vertexai` library to call the image generation model. It should load the image from `image_path` and send it along with the `style_prompt` to the Vertex AI API.
        - The function should handle the API response and return the URL of the generated image.
        - In `agent.py`, import and register the `VirtualStagingTool` with the `RealEstateAssistant` agent.

5.  **Step 5: Create Application Entrypoint**
    - Files to modify: `main.py`
    - Changes needed:
        - Write the main execution logic to initialize and run the `RealEstateAssistant` agent using the ADK's `run` or `start` method. This will start the conversational interface.

### Testing Strategy
- **Unit Tests:**
  - `tests/test_home_search.py`: Write a test to ensure `search_homes` returns the expected mock data structure.
  - `tests/test_virtual_staging.py`: Write a test for `stage_image`. This will require mocking the Vertex AI client (`vertexai.ImageGenerationModel`) to avoid making actual API calls during tests.
- **Integration Tests:**
  - Create a test file to verify that the ADK agent can correctly interpret user prompts and invoke the appropriate tool with the correct parameters.

## 🎯 Success Criteria
- The application starts without errors.
- The agent responds to a prompt like "find homes in 90210 under $2,000,000" by calling the `HomeSearchTool` and displaying the mock results.
- The agent responds to a prompt to "stage this room with modern furniture" (assuming an image path is provided) by calling the `VirtualStagingTool` and returning a (mocked or real) URL to a generated image.
- All unit tests pass.
