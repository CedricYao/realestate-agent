# Feature Implementation Plan: Real Estate AI Agent (Refined)

## 📋 Todo Checklist
- [ ] Set up project structure and dependencies.
- [ ] Implement the core ADK agent.
- [ ] Implement the Home Search tool with a mock API.
- [ ] Implement the Virtual Staging tool using `google-genai`.
- [ ] Create an application entrypoint to run the agent.
- [ ] Write unit and integration tests.
- [ ] Final Review and Testing.

## 🔍 Analysis & Investigation

### Codebase Structure
The current project is empty. The plan will establish a new Python project structure:

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
The architecture will be a Python application centered around the Google Agent Development Kit (ADK). The core agent will leverage two main tools: one for searching homes and another for virtual staging. The system will integrate with an external real estate API and the Google AI Gemini API for image generation.

### Dependencies & Integration Points
- **UV:** The package manager for installing and managing Python dependencies.
- **Google Agent Development Kit (ADK):** The primary framework for the conversational agent (`google-adk`).
- **Google AI Python SDK:** Required for the virtual staging feature (`google-genai`).
- **Requests:** For making HTTP calls to the external real estate API (`requests`).
- **Pillow:** For image manipulation (`Pillow`).
- **Pytest:** For running tests (`pytest`).
- **External Real Estate API:** An API like Zillow or Realtor.com needs to be chosen. The plan will start with a mock interface.

### Considerations & Challenges
- **API Selection:** A specific, reliable real estate API needs to be selected. Costs and rate limits must be considered.
- **API Key Management:** The `GOOGLE_API_KEY` for the Google AI SDK must be stored securely and not exposed in the source code. Using a `.env` file is the proposed approach.
- **Prompt Engineering:** The quality of the virtual staging will heavily depend on the prompts sent to the Gemini model. The agent may need logic to refine user input into effective prompts.
- **Error Handling:** Robust error handling is needed for all API calls to manage network issues, invalid input, and API errors gracefully.

## 📝 Implementation Plan

### Prerequisites
1.  Install `uv` (the Python package manager). Instructions can be found at `https://github.com/astral-sh/uv`.
2.  Set up a Python 3.9+ virtual environment: `python -m venv .venv && source .venv/bin/activate`.
3.  Obtain a `GOOGLE_API_KEY` from Google AI Studio.
4.  Create a `.env` file and add your key: `GOOGLE_API_KEY="your_api_key_here"`.

### Step-by-Step Implementation
1.  **Step 1: Project Setup**
    - Files to create: `requirements.txt`, `.env.example`, `main.py`, `agent.py`, `tools/__init__.py`, `tools/home_search.py`, `tools/virtual_staging.py`
    - Changes needed:
        - Create the directory structure as outlined in the analysis.
        - In `requirements.txt`, add the dependencies:
          ```
          google-adk
          google-genai
          requests
          Pillow
          pytest
          python-dotenv
          ```
        - Install dependencies using UV: `uv pip install -r requirements.txt`.

2.  **Step 2: Implement Core ADK Agent**
    - Files to modify: `agent.py`
    - Changes needed:
        - Define the `RealEstateAssistant` agent using the ADK.
        - Configure its name, description, and a Gemini model.
        - Leave placeholders to add the tools.

3.  **Step 3: Implement Home Search Tool**
    - Files to modify: `tools/home_search.py`, `agent.py`
    - Changes needed:
        - In `tools/home_search.py`, implement `search_homes(zip_code: str, max_price: int) -> list` using a mock response.
        - In `agent.py`, import and register the `HomeSearchTool`.

4.  **Step 4: Implement Virtual Staging Tool**
    - Files to modify: `tools/virtual_staging.py`, `agent.py`
    - Changes needed:
        - In `tools/virtual_staging.py`, implement `stage_image(image_path: str, style_prompt: str) -> str`.
        - This function will use the `google.generativeai` library. It will configure the client with the API key from the environment variables.
        - It will load the image from `image_path`, construct a prompt combining the image and the `style_prompt`, and call the appropriate Gemini model (e.g., `gemini-pro-vision`).
        - In `agent.py`, import and register the `VirtualStagingTool`.

5.  **Step 5: Create Application Entrypoint**
    - Files to modify: `main.py`
    - Changes needed:
        - Write the main execution logic to load environment variables, initialize, and run the `RealEstateAssistant` agent.

### Testing Strategy
- **Unit Tests:**
  - `tests/test_home_search.py`: Test that `search_homes` returns the expected mock data.
  - `tests/test_virtual_staging.py`: Test `stage_image` by mocking the `google.generativeai` client to avoid actual API calls.
- **Integration Tests:**
  - Verify that the ADK agent correctly interprets prompts and invokes the appropriate mocked tools.

## 🎯 Success Criteria
- The application starts without errors using `uv run`.
- The agent correctly calls the `HomeSearchTool` and displays mock results.
- The agent correctly calls the `VirtualStagingTool` and returns a (mocked or real) result.
- All tests pass when run with `uv run pytest`.