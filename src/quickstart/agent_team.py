from datetime import datetime

from agno.agent import Agent
from agno.models.mistral import MistralChat
from agno.models.openai import OpenAIChat, OpenAILike
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()


def get_model():
    local = False
    if local:
        return OpenAILike(
            id="qwen2.5-7b-instruct-1m@q8_0",
            api_key="not-used",
            base_url="http://127.0.0.1:1234/v1",
        )
    else:
        return OpenAIChat(id="gpt-4o")


web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=get_model(),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=get_model(),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
        )
    ],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=get_model(),
    instructions=["Always include sources", "Use tables to display data"],
    additional_context=f"Current date and time is: {datetime.now().isoformat()}",
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response(
    "What's the market outlook and financial performance of AI semiconductor companies?",
    stream=True,
)
