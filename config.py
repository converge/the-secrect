from app import TheSecrect

consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''

secrect = TheSecrect(consumer_key,
                     consumer_secret,
                     access_token_key,
                     access_token_secret)

secrect.set_exchange(exchange_name='poloniex')

secrect.calculate_twitter_references(term='bitcoin')
