# Feature Implementation Plan: Real Estate AI Agent

## 📋 Todo Checklist
- [ ] Set up project structure and dependencies.
- [ ] Implement the Home Search tool with a mock API.
- [ ] Implement the Virtual Staging tool with Vertex AI.
- [ ] Create and configure the main ADK Agent.
- [ ] Implement a CLI for agent interaction.
- [ ] Final Review and Testing.

## 🔍 Analysis & Investigation

### Codebase Structure
The current codebase is minimal, containing only a `README.md`, `LICENSE`, `.gitignore`, and a design document. The project will be built from scratch as a Python application based on the provided `real-estate-agent-design.md`. The plan is to create a new directory structure for the Python application.

### Current Architecture
The design document specifies a system architecture centered around the Google Agent Development Kit (ADK). The core components are:
- **ADK Agent**: The central component for processing user requests.
- **Home Search Tool**: A tool to search for properties via an external API.
- **Virtual Staging Tool**: A tool to generate virtually staged images using Vertex AI.

The application will be a Python service, and interaction will initially be via a command-line interface (CLI).

### Dependencies & Integration Points
- **`adk-python`**: The core framework for building the agent.
- **`google-cloud-aiplatform`**: To interact with Google Vertex AI for image generation.
- **Real Estate API**: An external API for property data. For development, a mock API will be used, as a real API key is not available.
- **Google Cloud SDK**: Required for authenticating with Google Cloud services (Vertex AI).

### Considerations & Challenges
- **API Keys & Secrets Management**: The application will require API keys for the Real Estate API and credentials for Google Cloud. These must be managed securely and not hard-coded. The plan will recommend using environment variables.
- **Real Estate API Choice**: The design document mentions Zillow or Realtor.com. The actual choice will affect the implementation of the `HomeSearchTool`. The plan will start with a generic, mocked interface to allow for flexibility.
- **Prompt Engineering**: The quality of the virtual staging will heavily depend on the prompts sent to Vertex AI. The implementation should include robust prompt construction logic.
- **Error Handling**: The agent needs to handle potential errors gracefully, such as failed API calls, invalid user input, or issues with image processing.

## 📝 Implementation Plan

### Prerequisites
1.  **Install Python**: Ensure Python 3.9+ is installed.
2.  **Google Cloud Account**: A Google Cloud project with the Vertex AI API enabled is required.
3.  **gcloud CLI**: The Google Cloud CLI must be installed and configured (`gcloud auth application-default login`).

### Step-by-Step Implementation

1.  **Step 1: Project Setup & Initialization**
    - **Action**: Create the directory structure for the application and set up the Python environment.
    - **New Files**:
        - `real_estate_agent/`
        - `real_estate_agent/__init__.py`
        - `real_estate_agent/agent.py`
        - `real_estate_agent/tools/`
        - `real_estate_agent/tools/__init__.py`
        - `real_estate_agent/tools/home_search.py`
        - `real_estate_agent/tools/virtual_staging.py`
        - `real_estate_agent/cli.py`
        - `requirements.txt`
        - `tests/`
        - `tests/test_home_search.py`
        - `tests/test_virtual_staging.py`
    - **Changes**:
        - Create a virtual environment: `python3 -m venv .venv` and activate it.
        - Create `requirements.txt` with the following content:
          ```
          adk-python
          google-cloud-aiplatform
          ```
        - Install dependencies: `pip install -r requirements.txt`.

2.  **Step 2: Implement the Home Search Tool**
    - **Action**: Create the `HomeSearchTool` with a mocked API response. This allows for development without a real API key.
    - **Files to modify**: `real_estate_agent/tools/home_search.py`
    - **Changes needed**:
        - Define the `search_homes` function as specified in the design document.
        - For now, the function will return a hard-coded list of properties to simulate an API call.
        - Add comments indicating where the actual API call should be made.

3.  **Step 3: Implement the Virtual Staging Tool**
    - **Action**: Create the `VirtualStagingTool` to interact with the Vertex AI API.
    - **Files to modify**: `real_estate_agent/tools/virtual_staging.py`
    - **Changes needed**:
        - Define the `stage_image` function.
        - Use the `google-cloud-aiplatform` library to call a Vertex AI image generation model.
        - The function will take an image path and a style prompt, and return the URL or data of the generated image.
        - Implement error handling for the API call.

4.  **Step 4: Create the ADK Agent**
    - **Action**: Set up the main ADK agent and integrate the tools.
    - **Files to modify**: `real_estate_agent/agent.py`
    - **Changes needed**:
        - Import the `search_homes` and `stage_image` functions.
        - Create an `Agent` instance from the `adk.api` module.
        - Configure the agent with the Gemini model and register the two functions as tools.

5.  **Step 5: Build the Command-Line Interface (CLI)**
    - **Action**: Create a simple CLI to interact with the agent.
    - **Files to modify**: `real_estate_agent/cli.py`
    - **Changes needed**:
        - Import the agent from `agent.py`.
        - Create a loop that takes user input and sends it to the agent.
        - Print the agent's responses to the console.
        - Add logic to handle multi-turn conversations.

### Testing Strategy
- **Unit Tests**:
    - `tests/test_home_search.py`: Write a test for `search_homes` to ensure it returns the expected mock data structure.
    - `tests/test_virtual_staging.py`: Write a test for `stage_image`. This will require mocking the Vertex AI API call using `unittest.mock`.
- **Integration Tests**:
    - Manually run the CLI (`python real_estate_agent/cli.py`) to test the end-to-end flow for both home searching and virtual staging.
    - Verify that the agent correctly understands user intent and calls the appropriate tools.

## 🎯 Success Criteria
- The project is successfully set up with all dependencies installed.
- The `HomeSearchTool` correctly processes queries and returns formatted property lists (from the mock data).
- The `VirtualStagingTool` successfully sends requests to Vertex AI and handles the generated images.
- The ADK agent correctly routes user requests to the appropriate tool.
- The CLI provides a functional interface for interacting with the agent.
- All unit tests pass.
