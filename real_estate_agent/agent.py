from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from real_estate_agent.tools.home_search import search_homes
from real_estate_agent.tools.virtual_staging import stage_image

# Create an Agent instance
root_agent = Agent(
    name="real_estate_agent",
    model="gemini-2.5-flash",
    tools=[
        search_homes,
        FunctionTool(stage_image),
    ],
)