from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    return [
        (article["title"], article["url"])
        for article in search_news(
            {"title": {"$regex": title, "$options": "i"}}
        )
    ]


# Requisito 8
def search_by_date(date):
    try:
        dateFormated = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        return [
            (article["title"], article["url"])
            for article in search_news({"timestamp": {"$eq": dateFormated}})
        ]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
