# Blog Creation Crew

A multi-agent system built with [CrewAI](https://crewai.com) that researches, writes, and edits blog posts automatically. Give it a topic, and it handles the rest.


## How It Works

Three AI agents work together like a real content team:

1. **Research Analyst** — Searches the web for current facts and trends
2. **Content Writer** — Drafts a structured blog post from the research
3. **Content Editor** — Polishes grammar, adds a headline, and finalizes the post

The final blog post is saved as a markdown file in the `output/` folder.


## Tech Stack

- Python 3.12
- CrewAI
- DuckDuckGo Search (free, no API key needed for research)


## Example Inputs

**Input:** `Agentic AI : How Multi Agent Systems Are Replacing Traditional Workflows in 2026.`

**Input:** `Quantum Computing and How It Will Shape The Future.`

**Input:** `Solar Battery Homes in 2026: Is Going Offgrid Finally Worth It`

**Input:** `Rise of Gaming : Advantages and Disadvantages`


**Output:** See the `output/` folder for a fully researched and proper blog file.


## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/blog-crew.git
   cd blog-crew
