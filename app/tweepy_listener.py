import time
import json


class TweepyListener:

    def __init__(self):
        self.count = 0
        self.tweets_peer_period = []
        self.start_time = None

    def on_connect(self):
        print('Twitter logged in successfully !')
        time.sleep(2)

    def on_data(self, data):
        if self.start_time is None:
            self.start_time = time.time()
        else:
            if ((time.time() - self.start_time) >= 10):
                print('##################################################')
                print('Number of times bitcoin word was mentioned '
                      '(every 10 seconds) {}'.format(self.count))
                self.start_time = None
                self.tweets_peer_period.append(self.count)
                for i, tweets in enumerate(self.tweets_peer_period):
                    print('{} {}'.format(i, tweets))
                print('##################################################')
                time.sleep(5)
                self.count = 0

        data = json.loads(data)
        print('-')
        print(data['text'])
        print(data['created_at'])
        print('-')

        self.count += 1
        print(self.count)
        # time.sleep(1)
        return True

    def on_error(self, status):
        print(status)

    def on_exception(self, data):
        print(data)
        print('exception raised')

    def keep_alive(self):
        print('keep your eyes on the road, dont sleep !')
        return True
