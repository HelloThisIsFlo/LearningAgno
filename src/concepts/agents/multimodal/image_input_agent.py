from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)


agent.print_response(
    "Please list all the image filenames you see in this UI",
    images=[
        Image(
            url="https://amansinghblog.wordpress.com/wp-content/uploads/2015/02/bad-userinterface.jpg"
        )
    ],
    stream=True,
    markdown=True,
)
