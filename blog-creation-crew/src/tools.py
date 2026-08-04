
from crewai.tools import tool
from ddgs import DDGS


@tool
def web_search(query: str) -> str:
    """
    Search the web for current information on any topic.
    Use this tool when you need facts, data, trends, or recent news
    to write an accurate and up-to-date blog post.
    
    Args:
        query: What to search for (e.g., 'AI trends 2026', 'best python frameworks')
    """
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=5)
            
            if not results:
                return "No results found for this query."
            
            output = f"Search results for '{query}':\n\n"
            for i, r in enumerate(results, 1):
                output += f"{i}. {r['title']}\n"
                output += f"   {r['href']}\n"
                output += f"   {r['body']}\n\n"
            
            return output
            
    except Exception as e:
        return f"Search failed: {str(e)}"