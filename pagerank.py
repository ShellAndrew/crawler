#here goes the implementation for the pagerank algorithm
import csv
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import defaultdict, deque
from typing import List, Tuple
import json
from pprint import pprint
import time
import numpy as np

import hashmap
import node


class PageRank:
    def __init__(self, graph, num_nodes):
        self.graph = graph
        self.inlink = {}
        self.num_nodes = num_nodes


    def create_inlink(self):
        all_nodes = set(self.graph.keys())
        for target_nodes in self.graph.values():
            all_nodes.update(target_nodes)
        initial_rank = 1.0 / self.num_nodes

        inlinks = {}

        for node in all_nodes:
            node.page_rank = initial_rank
            if not hasattr(node, 'out_degree'):
                node.out_degree = 0
        
        for source_node, target_nodes in self.graph.items():
            source_node.out_degree = len(target_nodes)

            for target_node in target_nodes:
                if target_node not in inlinks:
                    inlinks[target_node] = []
                inlinks[target_node].append(source_node)

        self.inlink = inlinks

    def PR(self, node):
        val = 0
        Ba = self.inlink[node]
        for i in Ba:
            val += self.PR(i) / len(self.graph[i])
        
        node.page_rank = 0.15 + (0.85 * val)

    def calculate_pagerank(self, iterations=100, damping_factor = 0.85) -> node:
        self.create_inlink()
        all_nodes = set(self.graph.keys())
        for target_nodes in self.graph.values():
            all_nodes.update(target_nodes)

        node_list = list(all_nodes)
        base_rank = (1.0 - damping_factor) / self.num_nodes

        for iteration in range(iterations):
            max_change = 0.0
            new_ranks = {}
            for node in node_list:
                sum_part = 0.0
                if node in self.inlink:
                    for inbound_node in self.inlink[node]:
                        if inbound_node.out_degree == 0:
                            sum_part += inbound_node.page_rank / self.num_nodes
                        else:
                            sum_part += inbound_node.page_rank / inbound_node.out_degree

                new_rank = base_rank + (damping_factor * sum_part)
                new_ranks[node] = new_rank
                change = abs(new_rank - node.page_rank)
                max_change = max(max_change, change)
        
            for node in node_list:
                node.page_rank = new_ranks[node]

            if max_change < 0.0001:
                print(f"Converged after {iteration + 1} iterations.")
                break


            
        return max(node_list, key=lambda n: n.page_rank)



''''





'''