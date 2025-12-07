import csv
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import defaultdict, deque
from typing import List, Tuple

import crawler
import hashmap

if __name__ == "__main__":
    arctic_crawler = crawler()
    