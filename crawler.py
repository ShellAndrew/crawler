import csv
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import defaultdict, deque
from typing import List, Tuple
import json
from pprint import pprint

import hashmap


class Crawler:
    def __init__(self):
        #self.map = hashmap.HashMap()
        self.dict = {}
        self.header = {'User-Agent': 'andys_first_webcrawler/v1.0 (my email: aashell24@yahoo.com)'}
        self.start_seed = "Queen_Maud_Land"
        
    def crawl(self):
        #current seeds starts with Queen_Maud_Land
        #will create a queue based off hyperlinks found on Queen_Maud_Land
        #loop through the queue and repeatedly add the links found on sequential pages
        #limit at 500 maybe?
        #we will likely find every article related to Queen_Maud_Land on wikipedia (hopefully)
        current_seed = self.start_seed
        header = {'User-Agent': 'andys_first_webcrawler/v1.0 (my email: aashell24@yahoo.com)'}
        api_url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extlinks%7Cinfo&titles={current_seed}&formatversion=2&ellimit=20"
        response = requests.get(api_url, headers={self.header})
        response.raise_for_status()
        json_data = response.json()
        if response.status_code == 200:
            text1 = response.text
            json_data = response.json()
            #print("--- Using json.dumps with indent=4 ---")
            #pretty_json_string = json.dumps(json_data, indent=4)
            #print(pretty_json_string)

            print("\n--- Using pprint ---")
            pprint(json_data)
        else:
            print(f"Error: Request failed with status code {response.status_code}")





