import csv
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import defaultdict, deque
from typing import List, Tuple

import hashmap


class Crawler:
    def __init__(self):
        self.map = hashmap.HashMap()
        self.CUSTOM_AGENT = "Andy's_custom_Crawler/v1/0 (Contact: aashell24@yahoo.com) "
        self.BROWSER_AGENT = BROWSER_AGENT = {
                                "User-Agent": (
                                    "Mozilla/5.0 (X11; Linux x86_64) "
                                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                                    "Chrome/122.0.0.0 Safari/537.36"
                                )
                            }
        self.HEADERS = { "User-Agent" : f"{CUSTOM_AGENT} {BROWSER_AGENT}" }

        def fetch_page(url: str) -> str:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            return response.text
    