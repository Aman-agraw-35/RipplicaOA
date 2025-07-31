import os
import requests
from dotenv import load_dotenv

# Load API key
load_dotenv()
GEMINI_API_URL = "https://api.gemini.com/v1/complete"
API_KEY = os.getenv("GEMINI_API_KEY")


def summarize_content(pages: list) -> str:
    """
    Summarize a list of texts using Gemini, returning bullet points.
    """
    combined = "\n\n".join(pages)
    prompt = (
        "Summarize the following content into concise bullet points:\n\n" + combined
    )
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {"prompt": prompt, "max_tokens": 500}

    resp = requests.post(GEMINI_API_URL, headers=headers, json=data)
    if resp.status_code == 200:
        return resp.json().get("text", "").strip()
    return "[Error] Could not summarize content."