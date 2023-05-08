from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest
from unittest.mock import MagicMock


def test_reading_plan_group_news():
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(-1)

    ReadingPlanService._db_news_proxy = MagicMock(
        return_value=[
            {
                "url": "https://blog.betrybe.com/novidades/noticia-1",
                "title": "Notícia 1",
                "timestamp": "14/03/2022",
                "writer": "Thomas",
                "reading_time": 4,
                "summary": "Algo top",
                "category": "Tecnologia",
            },
            {
                "url": "https://blog.betrybe.com/novidades/noticia-2",
                "title": "Notícia 2",
                "timestamp": "15/05/2020",
                "writer": "Sofia",
                "reading_time": 100,
                "summary": "algo bad",
                "category": "Sociedade",
            },
        ])

    result = ReadingPlanService.group_news_for_available_time(27)

    assert len(result["readable"]) == 1
    assert result["readable"][0]["unfilled_time"] == 23
    assert len(result["unreadable"]) == 1
