import csv
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import defaultdict, deque
from typing import List, Tuple


import hashmap

CUSTOM_AGENT = "Andy's_custom_Crawler/v1/0 (Contact: aashell24@yahoo.com) "
BROWSER_AGENT = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}

HEADERS = {
    "User-Agent" : f"{CUSTOM_AGENT} {BROWSER_AGENT}"
}

def fetch_page(url: str) -> str:

    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.text

def parse_front_page(html: str) -> List[Tuple[str, str]]:

    soup = BeautifulSoup(html, "html.parser")

    title_nodes = soup.select(".titleline")

    items: List[Tuple[str, str]] = []

    for node in title_nodes:
        main_link = node.find("a")
        if not main_link:
            continue
        title = main_link.get_text(strip=True)
        href = main_link.get("href", "")

        items.append((title, href))

    return items

def crawl_hacker_news() -> None:
    url = "https://news.ycombinator.com/"
    html = fetch_page(url)
    stores = parse_front_page(html)
    for i, (title,href) in enumerate(stores[:10], start=1):
        print(f"{i}. {title} -> {href}")


if __name__ == "__main__":
    crawl_hacker_news()



