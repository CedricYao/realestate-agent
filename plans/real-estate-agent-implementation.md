# Feature Implementation Plan: Real Estate AI Agent (Refined)

## 📋 Todo Checklist
- [x] ~~Set up project structure and dependencies.~~ ✅ Implemented
- [x] ~~Implement the core ADK agent.~~ ✅ Implemented
- [x] ~~Implement the Home Search tool with a mock API.~~ ✅ Implemented
- [x] ~~Implement the Virtual Staging tool using `google-genai` with a Vertex AI backend.~~ ✅ Implemented
- [x] ~~Create an application entrypoint to run the agent.~~ ✅ Implemented
- [x] ~~Final Review.~~ ✅ Implemented

## 🔍 Analysis & Investigation

### Codebase Structure
The current project is empty. The plan will establish a new Python project structure:

```
/
├── pyproject.toml     # Project metadata and dependencies (managed by uv)
├── agent.py           # Core ADK Agent definition
├── main.py            # Entrypoint to run the application
└── tools/
    ├── __init__.py
    ├── home_search.py
    └── virtual_staging.py
```

### Current Architecture
The architecture will be a Python application centered around the Google Agent Development Kit (ADK). The core agent will leverage two main tools: one for searching homes and another for virtual staging. The system will integrate with an external real estate API and the Google AI Gemini API (via a Vertex AI endpoint) for image generation.

### Dependencies & Integration Points
- **UV:** The package manager for installing and managing Python dependencies.
- **Google Agent Development Kit (ADK):** The primary framework for the conversational agent (`google-adk`).
- **Google AI Python SDK:** Required for the virtual staging feature (`google-genai`).
- **Requests:** For making HTTP calls to the external real estate API (`requests`).
- **Pillow:** For image manipulation (`Pillow`).
- **External Real Estate API:** An API like Zillow or Realtor.com needs to be chosen. The plan will start with a mock interface.

### Considerations & Challenges
- **API Selection:** A specific, reliable real estate API needs to be selected. Costs and rate limits must be considered.
- **Vertex AI Authentication:** The application needs to be properly authenticated to use Vertex AI. This requires setting up a Google Cloud project and using Application Default Credentials (ADC).
- **Prompt Engineering:** The quality of the virtual staging will heavily depend on the prompts sent to the Gemini model. The agent may need logic to refine user input into effective prompts.
- **Error Handling:** Robust error handling is needed for all API calls to manage network issues, invalid input, and API errors gracefully.

## 📝 Implementation Plan

### Prerequisites
1.  Install `uv` (the Python package manager). Instructions can be found at `https://github.com/astral-sh/uv`.
2.  Set up a Python 3.9+ virtual environment: `python -m venv .venv && source .venv/bin/activate`.
3.  Initialize the project with uv: `uv init`.
4.  Create a Google Cloud Platform project and enable the Vertex AI API.
5.  Install the Google Cloud SDK and run `gcloud auth application-default login` to authenticate.

### Step-by-Step Implementation
1.  **Step 1: Project Setup and Dependencies**
    - Files to create: `agent.py`, `main.py`, `tools/__init__.py`, `tools/home_search.py`, `tools/virtual_staging.py`
    - Changes needed:
        - Create the directory structure as outlined in the analysis.
        - Add and install dependencies using `uv add`. This will automatically update the `pyproject.toml` file.
          ```bash
          uv add google-adk
          uv add google-genai
          uv add requests
          uv add Pillow
          ```
    - **Implementation Notes:** Project initialized with `uv init`. Directories and files created. All dependencies added using `uv add`.
    - **Status**: ✅ Completed

2.  **Step 2: Implement Core ADK Agent**
    - Files to modify: `agent.py`
    - Changes needed:
        - Define the `RealEstateAssistant` agent using the ADK.
        - Configure its name, description, and a Gemini model.
        - Leave placeholders to add the tools.
    - **Implementation Notes:** Created the basic `RealEstateAssistant` class and initialized the agent configuration.
    - **Status**: ✅ Completed

3.  **Step 3: Implement Home Search Tool**
    - Files to modify: `tools/home_search.py`, `agent.py`
    - Changes needed:
        - In `tools/home_search.py`, implement `search_homes(zip_code: str, max_price: int) -> list` using a mock response.
        - In `agent.py`, import and register the `HomeSearchTool`.
    - **Implementation Notes:** Created the `search_homes` tool with a mock property list and registered it with the agent.
    - **Status**: ✅ Completed

4.  **Step 4: Implement Virtual Staging Tool**
    - Files to modify: `tools/virtual_staging.py`, `agent.py`
    - Changes needed:
        - In `tools/virtual_staging.py`, implement `stage_image(image_path: str, style_prompt: str) -> str`.
        - This function will use the `google.generativeai` library, configured to use a Vertex AI endpoint. This is done by specifying the project and location during client initialization (e.g., `genai.configure(project="your-gcp-project", location="your-gcp-location")`).
        - It will load the image from `image_path`, construct a prompt, and call the appropriate Gemini model (e.g., `gemini-pro-vision`).
        - In `agent.py`, import and register the `VirtualStagingTool`.
    - **Implementation Notes:** Created the `stage_image` tool, configured it to use the Vertex AI backend with the user-provided project and location, and registered it with the agent.
    - **Status**: ✅ Completed

5.  **Step 5: Create Application Entrypoint**
    - Files to modify: `main.py`
    - Changes needed:
        - Write the main execution logic to initialize and run the `RealEstateAssistant` agent.
    - **Implementation Notes:** Created the `main.py` file to run the application using `uvicorn`.
    - **Status**: ✅ Completed

## 🎯 Success Criteria
- The application starts without errors.
- The agent responds to a prompt like "find homes in 90210 under $2,000,000" by calling the `HomeSearchTool` and displaying the mock results.
- The agent responds to a prompt to "stage this room with modern furniture" (assuming an image path is provided) by calling the `VirtualStagingTool` and returning a result from the Vertex AI backend.