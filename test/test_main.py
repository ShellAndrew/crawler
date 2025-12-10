import csv
import time
import requests
from urllib.parse import urljoin, urlparse
from collections import defaultdict, deque
from typing import List, Tuple
import json

import test_pagerank
import test_node

if __name__ == "__main__":
    a = test_node.Node("A")
    b = test_node.Node("B")
    c = test_node.Node("C")
    d = test_node.Node("D")

    graph = {}
    graph[a] = [b]
    graph[b] = [a, d,c]
    graph[c] = [b, d]
    graph[d] = [b, c]


    pageranking = test_pagerank.PageRank(graph, 4)
    highest_rank_node = pageranking.calculate_pagerank()

    print(highest_rank_node)
