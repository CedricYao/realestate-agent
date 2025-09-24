from google.adk.agents import Agent
from google.adk.config import init_agent_config

from .tools.home_search import search_homes
from .tools.virtual_staging import stage_image

init_agent_config(
    name="RealEstateAssistant",
    description="An AI agent to help with home searching and virtual staging.",
)

class RealEstateAssistant(Agent):
    tools = [search_homes, stage_image]
