from google.adk.agents.llm_agent import Agent
from .tools.home_search import search_homes
from .tools.virtual_staging import stage_image

root_agent = Agent(
    model="gemini-2.5-flash",
    name="RealEstateAssistant",
    description="An AI agent to help with home searching and virtual staging.",
    tools=[search_homes, stage_image],
)