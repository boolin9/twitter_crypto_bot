from requests import Session
from dotenv import load_dotenv
import json
import os


class CryptoData:
    
    
    def __init__(self):
        load_dotenv()
        self.endpoint = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': os.getenv('CMC_API_KEY'),
        }
        self.parameters = {
            'start': '1',
            'limit': '5000',
            'convert': 'USD',
        }
        
        
    def get_data(self):
        session = Session()
        session.headers.update(self.headers)
        
        response = session.get(self.endpoint, params=self.parameters)
        data = json.loads(response.text)
        return data['data'][0]['quote']['USD']