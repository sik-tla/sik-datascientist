
from bs4 import BeautifulSoup as bs
import requests
import networkx as nx

# class Spider: #TODO overvejer class
# """Creating web crawler spider network from a website"""
#     def __init__(self, website):
#         self.website = website
#         self.graph = nx.DiGraph()
#         self.crawled = set()
#         self.queue = set()  # queue of urls to crawl
#         self.queue.add(website)
#         self.crawl()



def main():
    # Define the website to crawl
    website = "https://www.sit.dk/"
    # Create a spider network
    r = requests.get(website)
    # Create a BeautifulSoup object
    soup = bs(r.content, "html.parser")
    # Find all links in the website and save them in a list, looking for a-tags
    links = soup.find_all("a")
    breakpoint()
