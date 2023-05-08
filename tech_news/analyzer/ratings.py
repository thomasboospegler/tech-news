from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    categories = [new["category"] for new in find_news()]
    categories = [
        category[0]
        for category in Counter(sorted(categories)).most_common(5)
    ]
    return categories
