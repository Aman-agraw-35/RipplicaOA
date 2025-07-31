### agent.py
**Path:** `web-query-agent/agent.py`
```python
import os
from dotenv import load_dotenv
from validator import is_valid_query
from embedder import find_similar_query, save_query
from scraper import scrape_top_results
from summarizer import summarize_content

# Load environment variables
load_dotenv()


def handle_query(query: str) -> str:
    """
    Main pipeline: validate, retrieve cache or scrape & summarize, then cache.
    """
    # 1. Validate query
    if not is_valid_query(query):
        return "This is not a valid query."

    # 2. Check cache
    cached = find_similar_query(query)
    if cached:
        return f"[Cached Result]\n{cached}"

    # 3. Scrape web
    pages = scrape_top_results(query)
    if not pages:
        return "No content found for your query."

    # 4. Summarize
    summary = summarize_content(pages)

    # 5. Save to cache
    save_query(query, summary)
    return summary


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        user_query = " ".join(sys.argv[1:])
    else:
        user_query = input("Enter your query: ")
    result = handle_query(user_query)
    print(result)