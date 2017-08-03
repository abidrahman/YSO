# The Young Stock Observer
# Brad Ofrim & Abid Rahman

import sys
import csv
import datetime

from rtstock.stock import Stock
import rtstock.utils as Utils

from Volume import volumeIndicator
from News import newsIndicator

def make_short_list_of_stocks(file_in, price, volume, news, file_out):

    print("Fetching symbols..")
    all_stocks = read_stocks_from_file(file_in)
    print("Updating prices..")
    all_stocks_updated = update_stock_prices(all_stocks)

    if price[0]:
        print("Adding price filer..")
        all_stocks_updated = price_filter(price[1], all_stocks_updated)
    if volume[0]:
        print("Adding volume indicator..")
        all_stocks_updated = volume_indicator(all_stocks_updated, volume[1])
    if news:
        print("Adding news indicator..")
        all_stocks_updated = news_indicator(all_stocks_updated)

    print("Writing to output file..")
    write_stocks_to_file(all_stocks_updated, file_out)
    print("Complete.")


def news_indicator(stock_list):
    updated_stock_list = []
    for stock in stock_list:
        l = len(stock)
        print stock
        stock_news_date = newsIndicator(stock[0])[0]
        if l == 2:
            updated_stock_list.append((stock[0], stock[1], stock_news_date, newsIndicator(stock[0])[1]))
        elif l == 4:
            updated_stock_list.append((stock[0], stock[1], stock_news_date, stock[2], stock[3], newsIndicator(stock[0])[1]))
    updated_stock_list.sort(key=lambda stock: datetime.datetime.strptime(stock[2], '%m/%d/%Y'))
    return updated_stock_list

def volume_indicator(stock_list, multiplier):
    updated_stock_list = []
    for stock in stock_list:
        print stock
        volume_info = volumeIndicator(stock[0], multiplier)
        if volume_info[0]:
            updated_stock_list.append((stock[0], stock[1], volume_info[1], volume_info[2]))
    return updated_stock_list

def price_filter(n, all_stocks):
    stocks_under_n = []
    for stock in all_stocks:
        if stock[1] != None:
            if float(stock[1]) < n:
                stocks_under_n.append((stock[0], stock[1]))
    return stocks_under_n

def update_stock_prices(stock_symbol_list):
    all_stocks_updated = []
    num_stocks = len(stock_symbol_list)
    number_of_calls = num_stocks/400 + 1;
    for i in range(1,number_of_calls):
        if i == 1:
            partial_stocks = stock_symbol_list[:i*400]
        else:
            partial_stocks = stock_symbol_list[prev_i:i*400]
        prev_i = i*400
        partial_stocks = fetch_latest_price(partial_stocks)
        all_stocks_updated = all_stocks_updated + partial_stocks

    updated_list = []
    for stock in all_stocks_updated:
        stock_u = (stock[u'Symbol'], stock[u'LastTradePriceOnly'])
        updated_list.append(stock_u)

    return updated_list

def write_stocks_to_file(stock_list, file_name):
    with open(file_name, "wb") as write_file:
        writer = csv.writer(write_file)
        for stock in stock_list:
            print(stock[0:-1])
            print(stock[-1])
            print()
            writer.writerow(stock[0:-1])

def read_stocks_from_file(file_name):
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
    print("Welcome to the Young Stock Observer.")
    file_in = raw_input("Enter stock file: ")

    #Price Filter
    price = raw_input("Would you like to add a price filter? (Y/N): ")
    if price.upper() == 'Y':
        price_input = raw_input("Enter maximum price: ")
        price = (True, float(price_input))
    else:
        price = (False, "NA")

    #Volume Indicator
    volume = raw_input("Would you like to use the volume indicator? (Y/N): ")
    if volume.upper() == 'Y':
        volume_input = raw_input("Enter minimum volume multiplier: ")
        volume = (True, float(volume_input))
    else:
        volume = (False, "NA")

    #News Indicator
    news = raw_input("Would you like to use the news indicator? (Y/N): ")
    if news.upper() == 'Y':
        news = True
    else:
        news = False

    #Output
    file_out = raw_input("Enter name for output file: ")
    print("Calculating..")
    make_short_list_of_stocks(file_in, price, volume, news, file_out)
