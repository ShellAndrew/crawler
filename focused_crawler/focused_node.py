import csv
import time
import requests
from urllib.parse import urljoin, urlparse
from collections import defaultdict, deque
from typing import List, Tuple
import json
from pprint import pprint
import time
import numpy as np


class Node():
    def __init__(self, title):
        self.title = title
        self.page_rank = 0
        self.out_degree = 0

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.title == other.title
        
    def __hash__(self):
        return hash(self.title)

    def __repr__(self):
        return f"Node('{self.title}', Rank={self.rank:.4f})"
    
    def __str__(self):
        return f"title: '{self.title}' rank: '{self.page_rank}' out_degree: {self.out_degree}"
    


#Node

'''
This is the class that makes up the map that we are constructing

member_variables:
    -probability distribution
    -link to this page
    -links to other pages
'''

