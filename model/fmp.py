import requests
from dotenv import load_dotenv
import os

class Fmp:
    
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv("FMP_BASE_URL")
        self.api = os.getenv("FMP_API_KEY")
        
    def get_company_key_metrics(self, period: str, symbol: str):
        
        url = f'{self.base_url}/key-metrics/{symbol}?period={period}&apikey={self.api}'
        response = requests.get(url)
        
        if response.status_code != 200:
            return {'error': 'An error occurred, check your ticker symbol',
                    'errorcode': response.status_code}
        else:
            return response.json()
        
    def get_historical_data(self, symbol: str):
        
        url = f'{self.base_url}/historical-price-full/{symbol}?apikey={self.api}'
        response = requests.get(url)
        
        if response.status_code != 200:
            return {'error': 'An error occurred, check your ticker symbol',
                    'errorcode': response.status_code}
        else:
            return response.json()