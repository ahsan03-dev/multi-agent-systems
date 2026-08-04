
import os
from datetime import datetime
from dotenv import load_dotenv
from src.crew import create_blog_crew
from src.tasks import edit_task
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def main():
    load_dotenv()
    
    if not os.getenv("OPENROUTER_API_KEY"):
        print("ERROR: No OPENROUTER_API_KEY found.")
        print("Create a .env file and add your OpenRouter key.")
        return
    
    print("=" * 50)
    print("     BLOG CONTENT CREATION CREW")
    print("=" * 50)
    print()
    
    topic = input("What topic should we write about? ")
    
    if not topic.strip():
        print("No topic entered. Exiting.")
        return
    
    # output folder
    os.makedirs("output", exist_ok=True)
    
    # dynamic filename
    clean = "".join(c if c.isalnum() or c.isspace() else "" for c in topic)
    clean = clean.strip().replace(" ", "_").lower()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output/{clean}_{timestamp}.md"
    
    # Editor's task to save to this file
    edit_task.output_file = filename
    
    print(f"\nWorking on: '{topic}'...")
    print(f"Will save to: {filename}\n")
    
    crew = create_blog_crew()
    result = crew.kickoff(inputs={"topic": topic})
    
    print("\n" + "=" * 60)
    print(f"  Blog post saved to: {filename}")
    print("=" * 60)


if __name__ == "__main__":
    main()