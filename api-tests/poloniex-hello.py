from poloniex import Poloniex
from time import sleep
import sys
import os

# documentation at https://poloniex.com/support/api/

os.system('clear')

p = Poloniex()

while(True):
    sys.stdout.write('USDT / BTC last value: {}'
                     .format(p('returnTicker')['USDT_BTC']['last']))
    sys.stdout.write('\n')
    sys.stdout.write('Percent Change: {}'
                     .format(p('returnTicker')['USDT_BTC']['percentChange']))
    sys.stdout.write('\r')
    sleep(3)
    sys.stdout.flush()
