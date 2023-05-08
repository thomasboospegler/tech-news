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
    try:
        selector = Selector(text=html_content)
        next_page_link = selector.css(".next.page-numbers::attr(href)").get()
        return next_page_link
    except Exception:
        return None


# Requisito 4
def scrape_news(html_content):
    try:
        article = {}
        selector = Selector(text=html_content)
        article["title"] = selector.css("h1.entry-title::text").get().strip()
        article["writer"] = selector.css(".author > a::text").get()
        article["category"] = (
            selector.css(".category-style > .label::text").get())
        article["summary"] = (
            selector.css(".entry-content p").xpath("string()").get().strip())
        article["timestamp"] = selector.css(".meta-date::text").get()
        article["reading_time"] = int(
            selector.css(".meta-reading-time::text").get().split()[0])
        article["url"] = selector.css("link[rel=canonical]::attr(href)").get()
        return article
    except Exception:
        return {}


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
