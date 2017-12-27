from __future__ import unicode_literals
from .tweepy_listener import TweepyListener
from poloniex import Poloniex
import tweepy
import requests
import json

# documentation at https://poloniex.com/support/api/


class TheSecrect:

    def __init__(self,
                 consumer_key,
                 consumer_secret,
                 access_token_key,
                 access_token_secret):

        # exchange api
        self.exchange = None
        self.crypto_coins = self.get_crypto_coins()

        # Twitter connection
        self.tweepy_listener = TweepyListener()
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token_key, access_token_secret)

    # get all Coin Market Cap available coins informations
    def get_crypto_coins(self):
        # 10, for testing
        req = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=10')
        crypto_coins = json.loads(req.text)
        return crypto_coins

    def set_exchange(self, exchange_name):
        if exchange_name == 'poloniex':
            self.exchange = Poloniex()
            print('{} exchange set'.format(exchange_name))
        else:
            print('exchange not supported')

    def calculate_twitter_references(self, term):
        stream = tweepy.Stream(self.auth, self.tweepy_listener)
        stream.filter(track=[term])

    # todo: rewrite
    def get_coins_to_buy_from_twitter_user(self, twitter_user_id=None):

        user_tweets = self.twitter.GetUserTimeline(user_id=twitter_user_id,
                                                   count=10)
        for tweet in user_tweets:
            print('tweet -> {}'.format(tweet.text))
            for coin in self.crypto_coins:
                if coin['name'] in tweet.text:
                    print("bot: I'll BUY {} !".format(coin['name']))
        return self
