import unittest
from unittest.mock import patch, Mock
from model.fmp import Fmp

class TestFmp(unittest.TestCase):

    @patch('model.fmp.requests.get')
    @patch('model.fmp.os.getenv')
    def setUp(self, mock_getenv, mock_requests_get):
        mock_getenv.side_effect = lambda key: {
            "FMP_BASE_URL": "https://financialmodelingprep.com/api/v3",
            "FMP_API_KEY": "test_api_key"
        }.get(key)
        self.fmp = Fmp()

    @patch('model.fmp.requests.get')
    def test_get_company_key_metrics_success(self, mock_requests_get):
        mock_response = Mock()
        expected_data = {'metric': 'value'}
        mock_response.status_code = 200
        mock_response.json.return_value = expected_data
        mock_requests_get.return_value = mock_response

        result = self.fmp.get_company_key_metrics('annual', 'AAPL')
        self.assertEqual(result, expected_data)

    @patch('model.fmp.requests.get')
    def test_get_company_key_metrics_failure(self, mock_requests_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_requests_get.return_value = mock_response

        result = self.fmp.get_company_key_metrics('annual', 'INVALID')
        self.assertEqual(result, {'error': 'An error occurred, check your ticker symbol', 'errorcode': 404})

    @patch('model.fmp.requests.get')
    def test_get_historical_data_success(self, mock_requests_get):
        mock_response = Mock()
        expected_data = {'historical': 'data'}
        mock_response.status_code = 200
        mock_response.json.return_value = expected_data
        mock_requests_get.return_value = mock_response

        result = self.fmp.get_historical_data('AAPL')
        self.assertEqual(result, expected_data)

    @patch('model.fmp.requests.get')
    def test_get_historical_data_failure(self, mock_requests_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_requests_get.return_value = mock_response

        result = self.fmp.get_historical_data('INVALID')
        self.assertEqual(result, {'error': 'An error occurred, check your ticker symbol', 'errorcode': 404})
