import csv
import time
import requests
from urllib.parse import urljoin, urlparse
from collections import defaultdict, deque
from typing import List, Tuple
import json

import focused_pagerank
import focused_crawler


if __name__ == "__main__":
    arctic_crawler = focused_crawler.Crawler()
    data = arctic_crawler.crawl()
    #print(json.dumps(data, indent=4))
    pageranking = focused_pagerank.PageRank(arctic_crawler.graph, arctic_crawler.num_nodes)
    highest_rank_node = pageranking.calculate_pagerank()

    print(highest_rank_node)
