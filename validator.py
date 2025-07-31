import os
import requests
from dotenv import load_dotenv

# Load API key
load_dotenv()
GEMINI_API_URL = "https://api.gemini.com/v1/complete"
API_KEY = os.getenv("GEMINI_API_KEY")


def is_valid_query(query: str) -> bool:
    """
    Classify query validity using Gemini. Returns True if valid.
    """
    prompt = (
        "Determine if the following user input is a valid web search query. "
        "Respond with ONLY 'VALID' or 'INVALID'.\n\nQuery: " + query
    )
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {"prompt": prompt, "max_tokens": 5}

    resp = requests.post(GEMINI_API_URL, headers=headers, json=data)
    if resp.status_code != 200:
        # Fallback to simple heuristic
        return True
    text = resp.json().get("text", "").strip().upper()
    return text == "VALID"