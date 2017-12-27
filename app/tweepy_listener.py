from time import sleep
import json


class TweepyListener:

    def __init__(self):
        self.count = 0

    def on_connect(self):
        print('Twitter logged in successfully !')
        sleep(2)

    def on_data(self, data):
        print('-')
        data = json.loads(data)
        print(data['text'])
        print('-')

        self.count += 1
        print(self.count)
        sleep(3)
        return True

    def on_error(self, status):
        print(status)

    def on_exception(self, data):
        print(data)
        print('exception raised')

    def keep_alive(self):
        print('keep your eyes on the road, dont sleep !')
        return True
