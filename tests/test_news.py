from datetime import datetime
import unittest
from unittest.mock import patch, Mock
from services.news import News

class TestNews(unittest.TestCase):

    @patch('services.news.os.getenv')
    def setUp(self, mock_getenv):
        mock_getenv.side_effect = lambda key: {
            'NEWS_API_KEY': 'test_api_key',
            'NEWS_BASE_URL': 'https://newsapi.org/v2'
        }.get(key)
        self.news = News()

    def test_get_previous_month_date(self):
        with patch('services.news.datetime') as mock_datetime:
            mock_datetime.today.return_value = datetime(2023, 10, 15)
            mock_datetime.side_effect = lambda *args, **kw: datetime(*args, **kw)
            result = self.news.get_previous_month_date()
            self.assertEqual(result, '2023-09-15')

    @patch('services.news.requests.get')
    def test_get_news_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'articles': []}
        mock_get.return_value = mock_response

        result = self.news.get_news('test_query')
        self.assertEqual(result, {'articles': []})

    @patch('services.news.requests.get')
    def test_get_news_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        result = self.news.get_news('test_query')
        self.assertEqual(result, {'error': 'An error occurred, check your query', 'errorcode': 400})