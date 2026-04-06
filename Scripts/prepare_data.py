import requests
import os
import time
from typing import Dict, Any, List

WIKI_API_URL: str = "https://en.wikipedia.org/w/api.php"

HEADERS: Dict[str, str] = {"User-Agent": "RAG-ChatBot/1.0 (rahul@example.com)"}


def fetch_full_wikipedia_page(title: str, folder: str = "docs") -> None:
    params: Dict[str, Any] = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "extracts",
        "explaintext": True,
    }

    try:
        response: requests.Response = requests.get(
            WIKI_API_URL,
            params=params,
            headers=HEADERS,
            timeout=10,
        )

        if response.status_code != 200:
            print(f"Failed ({response.status_code}) for {title}")
            return

        data: Dict[str, Any] = response.json()

    except Exception as e:
        print(f"Error for {title}: {e}")
        return

    pages: Dict[str, Any] = data.get("query", {}).get("pages", {})

    for _, page_data in pages.items():
        content: str = page_data.get("extract", "")

        if not content:
            print(f"No content for {title}")
            return

        os.makedirs(folder, exist_ok=True)
        filename: str = os.path.join(folder, f"{title.replace(' ', '_')}.txt")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Title: {title}\n\n")
            f.write(content)

        print(f"Saved '{title}' → {filename}")


def fetch_multiple_companies(companies: List[str]) -> None:
    for company in companies:
        fetch_full_wikipedia_page(company)
        time.sleep(1)


companies: List[str] = ["Google", "Microsoft", "SpaceX", "Tesla", "Nvidia"]

fetch_multiple_companies(companies)
