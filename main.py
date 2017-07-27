# The Young Stock Observer
# Brad Ofrim & Abid Rahman
'''
Command line interface for simulating an investment account
Give user ability to pull data related to a specitic stock
Display data for the user
Allow user to login to an account or create a new account
Option to delete existing accounts
New accounts should be created with initial funds
'''

'''
Organization:
    Classes:
        - Application:
            * Starting point
            * Initializes resources
            * Connects to web services
            * Directs to 'login' options

        - Account:
            * Hold account info
            * Balances
            * Holdings
            * Quantities
            * Purchase prices
            * Changes

        - Stock
            * Data pertaining to the stock
'''
import sys

import csv
import stocks
from helper import *
from rtstock.stock import Stock

def main():
	short_list = []
	with open("symbols.csv", "rb") as symbol_file:
		reader = csv.reader(symbol_file)
		for symbol in reader:
			latest_stock_price = Stock(symbol).get_latest_price()[0]
			if latest_stock_price[u'LastTradePriceOnly'] < 2.00:
				short_list.append(symbol)

	with open("symbols_short_list.csv", "wb") as file:
		writer = csv.writer(file)
		writer.writerow(short_list)

if __name__ == '__main__':
    main()