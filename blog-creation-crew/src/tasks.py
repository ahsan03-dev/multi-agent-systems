from crewai import Task
from src.agents import researcher, writer, editor


research_task = Task(
    description=(
        "Research the topic: {topic}\n\n"
        "Use the web_search tool to find current information. "
        "Cover: what it is, why it matters, key facts, and current trends. "
        "Write your findings as organized bullet points."
    ),
    expected_output="A list of organized research notes with facts and sources",
    agent=researcher
)


write_task = Task(
    description=(
        "Write a blog post about: {topic}\n\n"
        "Use the research notes provided to write a 500-800 word post. "
        "Include: a hook in the intro, clear headings, examples, and a conclusion. "
        "Write in a friendly, conversational tone."
    ),
    expected_output="A complete blog post draft with headings and body text",
    agent=writer,
    context=[research_task]
)


edit_task = Task(
    description=(
        "Edit the blog post about: {topic}\n\n"
        "Fix grammar, improve sentence flow, and add a catchy headline. "
        "Make sure the intro grabs attention and the conclusion has a clear takeaway. "
        "Return the final polished version."
    ),
    expected_output="A polished blog post with a headline, intro, body, and conclusion",
    agent=editor,
    context=[write_task],
    output_file="output/blog_post.md"
)