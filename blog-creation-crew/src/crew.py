
from crewai import Crew, Process
from src.agents import researcher, writer, editor
from src.tasks import research_task, write_task, edit_task


def create_blog_crew():
    """
    Creates and returns the Blog Content Creation Crew.
    Uses sequential process: research → write → edit.
    """
    crew = Crew(
        agents=[researcher, writer, editor],
        tasks=[research_task, write_task, edit_task],
        process=Process.sequential,
        verbose=True
    )
    
    return crew