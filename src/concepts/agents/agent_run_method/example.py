from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.pprint import pprint_run_response
from dotenv import load_dotenv

load_dotenv()


agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="You are a Best-Selling Author who always researches a topic before writing!",
    tools=[DuckDuckGoTools()],
)

# Run agent and return the response as a variable
response: RunResponse = agent.run(
    "Tell me a 5 second short story about a robot, get inspiration for the robot name from the latest news"
)
# Run agent and return the response as a stream
response_stream: Iterator[RunResponse] = agent.run(
    "Tell me a 5 second short story about a lion", stream=True
)

# Print the response in markdown format
pprint_run_response(response, markdown=True)
# Print the response stream in markdown format
pprint_run_response(response_stream, markdown=True)
