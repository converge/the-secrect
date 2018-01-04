from binance.client import Client
import time


class SignalSimulator:

    def __init__(self, symbol, buy_price, sell_price, stop_loss):
        self.symbol = symbol
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.stop_loss = stop_loss

        self.binance = Client(api_key, secrect_key)

    def monitor(self):
        sold_price = False
        bought_price = False
        on = True
        while(on):
            last_price = self.get_current_price()
            if bought_price is False and last_price <= self.buy_price:
                bought_price = last_price
                print('{} bought at price: {}'
                      .format(self.symbol, last_price))
            elif (bought_price and sold_price is False
                  and last_price >= self.sell_price):
                sold_price = last_price
                print('{} sold at price: {}'
                      .format(self.symbol, last_price))
                profit = (self.sell_price - self.buy_price)
                print('BOUGHT at ({}) , SOLD at ({}) , PROFIT ({})'
                      .format(self.buy_price, self.sell_price, profit))
                on = False

            if bought_price and last_price <= self.stop_loss:
                print('STOP LOSS called at {} price'.format(last_price))

            if bought_price is False:
                print('Waiting to BUY, current price: {}'
                      .format(self.get_current_price()))
            elif sold_price is False:
                print('Waiting to SELL, current price: {}'
                      .format(self.get_current_price()))
            time.sleep(7)

        return self

    def operation_overview(self):
        print('--------------------------------------------------------------')
        print('Going to buy {} at price {} and sell at price {}'
              .format(self.symbol, self.buy_price, self.sell_price))
        time.sleep(1)
        print('-')
        print('STOP LOSS at {}'.format(self.stop_loss))
        print('-')
        print('{} current price: {}'
              .format(self.symbol, self.get_current_price()))
        print('--------------------------------------------------------------')

    def get_current_price(self):
        return (
            float(self.binance.get_symbol_ticker(symbol=self.symbol)['price']))


if __name__ == '__main__':

    api_key = (
        '')
    secrect_key = (
        '')

    # signals values
    simulator = SignalSimulator(symbol='XRPBTC',
                                buy_price=0.00013000,
                                sell_price=0.00015000,
                                stop_loss=0.000125000)

    # simulator.set_stop_loss_percentage_after_goal(1)
    # simulator.set_increase_stop_loss_percentage_after_goal_reach(1)
    # stop_loss_percentage_after_goal=1)
    simulator.operation_overview()
    simulator.monitor()
