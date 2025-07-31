from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
import requests

def scrape_top_results(query: str, max_results: int = 5):
    """
    Returns list of page texts for top search results.
    """
    texts = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            url = r.get('href')
            try:
                res = requests.get(url, timeout=5)
                soup = BeautifulSoup(res.text, 'html.parser')
                paragraph_text = ' '.join(p.text for p in soup.find_all('p'))
                texts.append(paragraph_text[:2000])  # truncate
            except Exception:
                continue
    return texts