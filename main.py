# The Young Stock Observer
# Brad Ofrim & Abid Rahman

import sys

import csv
from rtstock.stock import Stock
import rtstock.utils as Utils

def main():
    make_short_list_of_stocks()


def make_short_list_of_stocks():
    stocks_under_two = {}
    all_stocks = []
    all_stocks_updated = []
    with open("symbols.csv", "rb") as symbol_file:
        reader = csv.reader(symbol_file)
        for symbol in reader:
            all_stocks.append(symbol[0])

    for i in range(1,21):
        if i == 1:
            partial_stocks = all_stocks[:i*400]
        else:
            partial_stocks = all_stocks[prev_i:i*400]
        prev_i = i*400
        partial_stocks = fetch_latest_price(partial_stocks)
        all_stocks_updated = all_stocks_updated + partial_stocks

    for stock in all_stocks_updated:
        if stock[u'LastTradePriceOnly'] != None:
            curr_price = float(stock[u'LastTradePriceOnly'])
            if curr_price < 1.30:
                stocks_under_two[stock[u'Symbol']] = stock[u'LastTradePriceOnly']
                print(stock[u'Symbol'] + stock[u'LastTradePriceOnly'])

    print(len(stocks_under_two))


def fetch_latest_price(stock):
    return request_stock_info(stock, ['Symbol', 'LastTradePriceOnly'])


def request_stock_info(stock, info_needed):
    return Utils.request_quotes(stock, info_needed)

if __name__ == '__main__':
    main()
