
from google.adk.agents import Agent

from real_estate_agent.tools.home_search import search_homes
from real_estate_agent.tools.virtual_staging import stage_image

# Create an Agent instance
root_agent = Agent(
    name="real_estate_agent",
    model="gemini-1.5-flash",
    # The ADK will use the default model configured for the environment,
    # which is typically a Gemini model when using Vertex AI.
    tools=[
        search_homes,
        stage_image,
    ],
)
