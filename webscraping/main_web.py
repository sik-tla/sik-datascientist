from bs4 import BeautifulSoup
import requests


class Spider:
    """Creating web crawler spider network from a website"""

    def __init__(self, website):
        """Tilføje attributter til klassen"""
        self.website = website
        self.crawled = set()
        self.queue = set()  # queue of urls to crawl
        self.queue.add(website)  # tilføje website til queue
        self.crawl()  # kører crawl metoden

    def crawl(self):
        """Crawl the website"""
        # Iteration over the queue
        while self.queue:
            url = self.queue.pop()
            self.crawled.add(url)
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")
            links = soup.find_all("a")

            # Iteration over links og derefter over attributterne i links, ved brug af .attrs (dictionary)
            for link in links:
                breakpoint()
                if "href" in link.attrs:
                    new_url = link.attrs["href"]
                    if new_url not in self.crawled:
                        self.queue.add(new_url)
                        # TODO fix tel:+45 slet tel: fra new_url
                        breakpoint()


def sik_ulr(url):
    # hjemmesider som bliver henvist til.

    # Define the website to crawl
    website = url
    # Get the website content
    r = requests.get(website)
    # Create a BeautifulSoup object
    soup = BeautifulSoup(r.content, "html.parser")
    # Find all links in the website and save them in a list, looking for a-tags
    links = soup.find_all("a")
    # breakpoint()
    # Print links ved at kigge efter href i attributterne
    for link in links:
        print(link["href"])
        # if "href" in link.attrs:
        #     print(link.attrs["href"])
