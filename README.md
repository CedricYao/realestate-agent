# Real Estate AI Agent

This project implements an AI agent for real estate customers using the Google Agent Development Kit (ADK).

## Architecture

The project is structured as a Python package (`re_agent`) that contains the core agent logic and its tools.

-   **`re_agent/agent.py`**: Defines the main `root_agent` using `google.adk.agents.llm_agent.Agent`. This agent is configured with the Gemini model and is responsible for orchestrating the tools.
-   **`re_agent/tools/`**: This directory contains the tools that the agent can use.
    -   **`home_search.py`**: Implements a `HomeSearchTool` that allows users to search for homes based on zip code and price. It currently returns mock data.
    -   **`virtual_staging.py`**: Implements a `VirtualStagingTool` that takes an uploaded image and a style prompt to generate a virtually staged image using the Vertex AI `gemini-pro-vision` model.
-   **`pyproject.toml`**: Manages the project dependencies using `uv`.

The application is served as a web application using FastAPI, which is managed by the ADK framework.

## Getting Started

### Prerequisites

-   Python 3.9+
-   `uv` package manager [UV installation instructions](https://docs.astral.sh/uv/getting-started/installation/)
-   Google Cloud SDK installed and authenticated (`gcloud auth application-default login`)
-   A Google Cloud project with the Vertex AI API enabled.

### Installation and Setup

1.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2.  **Install dependencies:**
    Use `uv sync` to install the dependencies listed in `pyproject.toml`.
    ```bash
    uv sync
    ```

### Running the Application

To start the web server, run the following command from the project root:

```bash
uv run adk web
```

This will start the ADK web interface, which you can access in your browser to interact with the agent.
