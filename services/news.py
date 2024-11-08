import requests
from dotenv import load_dotenv
from dateutil.relativedelta import relativedelta
from datetime import datetime
import os

class News:
    
    def __init__(self):
        load_dotenv()
        self.api = os.getenv("NEWS_API_KEY")
        self.base_url = os.getenv("NEWS_BASE_URL")
        
    def get_previous_month_date(self) -> str:
            today = datetime.today()
            last_month_date = today - relativedelta(months=1)
            return last_month_date.strftime("%Y-%m-%d")     
    
    def get_news(self, query: str, sortBy:str = "popularity"):
        
        date = self.get_previous_month_date()
        
        url = f"{self.base_url}/everything?q={query}&from={date}&sortBy={sortBy}&apiKey={self.api}"
        response = requests.get(url)
        
        if response.status_code != 200:
            return {'error': 'An error occurred, check your query',  
                    'errorcode': response.status_code}
        else:
            return response.json()
        
    
    