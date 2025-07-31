# Web Query Agent

A smart web-search assistant that:
- Classifies queries as valid/invalid
- Checks past similar queries using semantic similarity
- Scrapes top 5 results using Playwright
- Summarizes content using OpenAI or HuggingFace LLM
- Stores the result for future queries

## Features

- Semantic search with FAISS
- Headless scraping with Playwright
- Summarization via LLM
- CLI-based interface

## Getting Started

```bash
git clone https://github.com/YOUR_USERNAME/web-query-agent.git
cd web-query-agent
pip install -r requirements.txt
