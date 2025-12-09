import csv
import time
import requests
from urllib.parse import urljoin, urlparse
from collections import defaultdict, deque
from typing import List, Tuple
import json
from pprint import pprint
import time

import node


class Crawler:
    def __init__(self):
        #self.map = hashmap.HashMap()
        self.graph = {}
        self.header = {'User-Agent': 'andys_first_webcrawler/v1.0 (my email: aashell24@yahoo.com)'}
        self.start_seed = "Queen_Maud_Land"
        self.queue = deque([self.start_seed])
        self.visited = set()
        self.visited.add(self.start_seed)
        self.num_nodes = 1
        
    def crawl(self):
        with open("./small_crawler/data.csv", 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            
            #current seeds starts with Queen_Maud_Land
            #will create a queue based off hyperlinks found on Queen_Maud_Land
            #loop through the queue and repeatedly add the links found on sequential pages
            #limit at 500 maybe?
            #we will likely find every article related to Queen_Maud_Land on wikipedia (hopefully)
            pages_count = 0
            limit = 200
            header = {'User-Agent': 'andys_first_webcrawler/v1.0 (my email: aashell24@yahoo.com)'}

            
            while (pages_count < limit and self.queue):
                current_seed = self.queue.popleft()
                print(f"Crawling: {current_seed} (Queue size: {len(self.queue)})")
                api_url = "https://en.wikipedia.org/w/api.php"
                params = {
                    "action": "query",
                    "format": "json",
                    "titles": current_seed,
                    "prop": "links",
                    "pllimit": "max",  
                    "formatversion": 2
                }

                
                #api_url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=links%7Cinfo&titles={current_seed}&formatversion=2&ellimit=20"
                try:
                    time.sleep(2)
                    response = requests.get(api_url, headers=self.header, params=params)
                    response.raise_for_status()
                    json_data = response.json()
                    
                        #print("--- Using json.dumps with indent=4 ---")
                        #pretty_json_string = json.dumps(json_data, indent=4)
                        #print(pretty_json_string)

                    if 'pages' not in json_data['query']:
                        continue
                    #print("\n--- Using pprint ---")
                    #pprint(json_data)
                    #print("\n--- Just the extlinks ---")
                    #this is list of dictionarys that maps the key 'url' to the url of the page
                    #print(json_data['query']['pages'][0]['extlinks'])
                    page_data = json_data['query']['pages'][0]

                    current_node = node.Node(current_seed)
                    self.graph[current_node] = []

                    if 'links' in page_data:
                        for ext_url in page_data['links']:
                            title = ext_url['title']
                            ns = ext_url['ns']
                            current_title = node.Node(title)
                            if ns == 0:
                                self.graph[current_node].append(current_title)
                            
                                if title not in self.visited:
                                    self.num_nodes += 1
                                    self.visited.add(title)
                                    self.queue.append(title)


                    

                    row = [current_node.title] + [i.title for i in self.graph[current_node]] + [''] * (30000 - len(self.graph[current_node]))
                    writer.writerow(row)
                    pages_count += 1
                    

                    
                except requests.exceptions.RequestException as e:
                    print(f"Error fetching {current_seed}: {e}")
                except KeyError as e:
                    print(f"Data format error for {current_seed}: {e}")

            print(f"\nFinished! Crawled {pages_count} pages.")
        return self.graph





