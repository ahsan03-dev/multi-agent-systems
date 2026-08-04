# Blog Creation Crew

A multi-agent system built with [CrewAI](https://crewai.com) that researches, writes, and edits blog posts automatically. Give it a topic, and it handles the rest.


## How It Works

Three AI agents work together like a real content team:

1. **Research Analyst** — Searches the web for current facts and trends
2. **Content Writer** — Drafts a structured blog post from the research
3. **Content Editor** — Polishes grammar, adds a headline, and finalizes the post

The final blog post is saved as a markdown file in the `output/` folder.

<img width="600" height="300" alt="test4" src="https://github.com/user-attachments/assets/6ab5cbf8-88f0-4259-be4c-67ca0897a76b" />

## File Structure  

``` 
blog-crew/
├── src/
│   ├── agents.py      
│   ├── tasks.py       
│   ├── tools.py       
│   └── crew.py
├── main.py            
├── requirements.txt
├── .env.example
├── .gitignore
└── output/            
```

## Tech Stack

- Python 3.12
- CrewAI
- DuckDuckGo Search (free, no API key needed for research)


## Example Inputs

-> `Agentic AI : How Multi Agent Systems Are Replacing Traditional Workflows in 2026.`  
-> `Quantum Computing and How It Will Shape The Future.`  
-> `Solar Battery Homes in 2026: Is Going Offgrid Finally Worth It`  
-> `Rise of Gaming : Advantages and Disadvantages`  

**Output:** You can see the `output/` for blog files I have generated from these inputs.
