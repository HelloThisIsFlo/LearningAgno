from agno.agent import Agent
from dotenv import load_dotenv

load_dotenv()

agent = Agent(markdown=True, debug_mode=True)
agent.print_response("Share a 2 sentence horror story")
