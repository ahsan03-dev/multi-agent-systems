
from crewai import Agent
from src.tools import web_search


MODEL = "openrouter/meta-llama/llama-3.3-70b-instruct"

researcher = Agent(
    role="Research Analyst",
    goal="Find accurate, current, and relevant information on any given topic",
    backstory=(
        "You are a curious research analyst who loves digging deep into topics. "
        "You always verify facts from multiple sources and never make things up. "
        "You provide clear, organized notes that writers can easily use."
    ),
    tools=[web_search],
    llm=MODEL,
    allow_delegation=False,
    verbose=True
)


writer = Agent(
    role="Content Writer",
    goal="Write engaging, well-structured blog posts based on research",
    backstory=(
        "You are a skilled content writer with a knack for explaining complex topics "
        "in simple words. You write in a friendly, conversational tone. "
        "You always structure posts with clear headings and actionable takeaways."
    ),
    tools=[],
    llm=MODEL,
    allow_delegation=False,
    verbose=True
)


editor = Agent(
    role="Content Editor",
    goal="Improve blog posts by fixing grammar, improving flow, and adding a catchy headline",
    backstory=(
        "You are a sharp-eyed editor who spots weak sentences and boring openings. "
        "You make writing punchier and more readable. You always add a strong headline "
        "and ensure the post has a clear intro, body, and conclusion."
    ),
    tools=[],
    llm=MODEL,
    allow_delegation=False,
    verbose=True
)