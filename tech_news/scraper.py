import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        sleep(1)
        response = requests.get(
            url,
            timeout=3,
            headers={"User-Agent": "Fake user-agent"}
            )
        if response.status_code == 200:
            return response.text
        return None
    except Exception:
        return None


# Requisito 2
def scrape_updates(html_content):
    try:
        selector = Selector(text=html_content)
        links = selector.css(".entry-title > a::attr(href)").getall()
        return links
    except Exception:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
