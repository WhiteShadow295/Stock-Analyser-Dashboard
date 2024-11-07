import google.generativeai as genai
from dotenv import load_dotenv
import os

class geminiService:
    
    def __init__(self):
        load_dotenv()
        self.api = os.getenv("GENAI_API_KEY")
    
    def get_introduction(self, symbol: str, genaiModel="gemini-1.5-flash") -> str:
        # Get introduction of the company
        genai.configure(api_key=self.api)
        model = genai.GenerativeModel(genaiModel)
            
        response = model.generate_content(f"Explain this US company with the stock symbol {symbol}")
        return response.text
