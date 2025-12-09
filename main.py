import csv
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import defaultdict, deque
from typing import List, Tuple
import json

import pagerank
import crawler
import hashmap

if __name__ == "__main__":
    arctic_crawler = crawler.Crawler()
    data = arctic_crawler.crawl()
    #print(json.dumps(data, indent=4))
    pageranking = pagerank.PageRank(arctic_crawler.graph, arctic_crawler.num_nodes)
    highest_rank_node = pageranking.calculate_pagerank()

    print(highest_rank_node)
