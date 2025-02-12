from datetime import datetime

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

MODEL = "gpt-4o"

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id=MODEL),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id=MODEL),
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
    model=OpenAIChat(id=MODEL),
    instructions=["Always include sources", "Use tables to display data"],
    additional_context=f"Current date and time is: {datetime.now().isoformat()}",
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response(
    "What's the market outlook and financial performance of AI semiconductor companies?",
    stream=True,
)
