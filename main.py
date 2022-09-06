import tweepy
from dotenv import load_dotenv
import os
import crypto_api


class Twitter:
    
    def __init__(self):
        load_dotenv()
        self.client = tweepy.Client(consumer_key=os.getenv('TWITTER_KEY'),
                                    consumer_secret=os.getenv('TWITTER_SECRET'),
                                    access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
                                    access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
                                   )
        
    
    def send_tweet(self):
        crypto = crypto_api.CryptoData()
        if str(crypto.get_data()['percent_change_24h'])[0] == '-':
            text = f"Sell, sell, sell!\n-\nCurrent Price: ${round(crypto.get_data()['price'], 2)}\nPercentage change over the last 24 hours: {round(crypto.get_data()['percent_change_24h'], 2)}%"
            self.client.create_tweet(text=text)
        else:
            text = f"Buy, buy, buy!\n-\nCurrent Price: ${round(crypto.get_data()['price'], 2)}\nPercentage change over the last 24 hours: +{round(crypto.get_data()['percent_change_24h'], 2)}%"
            self.client.create_tweet(text=text)


        
if __name__ == "__main__":
    twit = Twitter()
    twit.send_tweet()