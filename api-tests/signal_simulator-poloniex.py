from poloniex import Poloniex
import time


class SignalSimulator:

    def __init__(self, coin_code, buy_price, sell_price, stop_loss):
        self.coin_code = coin_code
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.stop_loss = stop_loss

        self.polo = Poloniex()

    def monitor(self):
        sold_price = False
        bought_price = False
        while(True):
            last_price = self.get_current_price()
            if bought_price is False and last_price <= self.buy_price:
                bought_price = last_price
                print('{} bought at price: {}'
                      .format(self.coin_code, last_price))
            elif sold_price is False and last_price >= self.sell_price:
                sold_price = last_price
                print('{} sold at price: {}'
                      .format(self.coin_code, last_price))

            if bought_price and last_price <= self.stop_loss:
                print('STOP LOSS called at {} price'.format(last_price))

            if bought_price is False:
                print('Waiting to BUY, current price: {}'
                      .format(self.get_current_price()))
            else:
                print('Waiting to SELL, current price: {}'
                      .format(self.get_current_price()))
            time.sleep(5)

        return self

    def operation_overview(self):
        print('--------------------------------------------------------------')
        print('Going to buy {} at price {} and sell at price {}'
              .format(self.coin_code, self.buy_price, self.sell_price))
        time.sleep(1)
        print('-')
        print('STOP LOSS at {}'.format(self.stop_loss))
        print('-')
        print('{} current price: {}'
              .format(self.coin_code, self.get_current_price()))
        print('--------------------------------------------------------------')

    def get_current_price(self):
        return float(self.polo('returnTicker')[self.coin_code]['last'])


if __name__ == '__main__':
    # signals values
    simulator = SignalSimulator(coin_code='BTC_OMG',
                                buy_price=0.00110794,
                                sell_price=0.002,
                                stop_loss=0.001105)

    simulator.set_stop_loss_percentage_after_goal(1)
    simulator.set_increase_stop_loss_percentage_after_goal_reach(1)
    # stop_loss_percentage_after_goal=1)
    simulator.operation_overview()
    simulator.monitor()
