import requests
from dotenv import load_dotenv
import os

##  Setting up the env
load_dotenv()

class Fmp:
    
    def __init__(self):
        self.base_url = os.getenv("FMP_BASE_URL")
        self.api = os.getenv("FMP_API_KEY")
        
    def get_company_key_metrics(self, period: str, symbol: str):
        
        url = f'{self.base_url}/key-metrics/{symbol}?period={period}&apikey={self.api}'
        response = requests.get(url)
        return response.json()