# The Young Stock Observer
# Brad Ofrim & Abid Rahman

import sys

import csv
from rtstock.stock import Stock
import rtstock.utils as Utils
from Volume import volumeIndicator

def main():
    make_short_list_of_stocks()

def make_short_list_of_stocks():
    all_stocks = read_in_symbols("symbols.csv")
    all_stocks_updated = update_stock_prices(all_stocks)
    stocks_under_one_fifty = short_list_under_n(1.50, all_stocks_updated)
    volume_short_list_under_one_fifty = volume_indicator(stocks_under_one_fifty, 3)
    write_stocks_to_file(volume_short_list_under_one_fifty, "symbols_short_list.csv")

def write_stocks_to_file(stock_dict, file_name):
    with open(file_name, "wb") as write_file:
        writer = csv.writer(write_file)
        for stock in stock_dict.items():
            writer.writerow(stock)

def volume_indicator(stock_list, multiplier):
    updated_stock_list = {}
    for stock in stock_list:
        volume_info = volumeIndicator(stock, multiplier)
        if volume_info[0]:
            updated_stock_list[stock] = [stock_list[stock], volume_info[1], volume_info[2]]
            print stock
            print updated_stock_list[stock]
    return updated_stock_list

def short_list_under_n(n, all_stocks):
    stocks_under_n = {}
    for stock in all_stocks:
        if stock[u'LastTradePriceOnly'] != None:
            curr_price = float(stock[u'LastTradePriceOnly'])
            if curr_price < n:
                stocks_under_n[stock[u'Symbol']] = stock[u'LastTradePriceOnly']
    return stocks_under_n

def update_stock_prices(stock_symbol_list):
    all_stocks_updated = []
    for i in range(1,21):
        if i == 1:
            partial_stocks = stock_symbol_list[:i*400]
        else:
            partial_stocks = stock_symbol_list[prev_i:i*400]
        prev_i = i*400
        partial_stocks = fetch_latest_price(partial_stocks)
        all_stocks_updated = all_stocks_updated + partial_stocks
    return all_stocks_updated

def read_in_symbols(file_name):
    all_stocks = []
    with open(file_name, "rb") as symbol_file:
        reader = csv.reader(symbol_file)
        for symbol in reader:
            all_stocks.append(symbol[0])
    return all_stocks

def fetch_latest_price(stock):
    return request_stock_info(stock, ['Symbol', 'LastTradePriceOnly'])

def request_stock_info(stock, info_needed):
    return Utils.request_quotes(stock, info_needed)

if __name__ == '__main__':
    main()
