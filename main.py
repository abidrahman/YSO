# The Young Stock Observer
# Brad Ofrim & Abid Rahman

import sys

import csv
from rtstock.stock import Stock

def main():
	short_list = []
	with open("symbols.csv", "rb") as symbol_file:
		reader = csv.reader(symbol_file)
		for symbol in reader:
			latest_stock_price = Stock(symbol).get_latest_price()[0]
			print(symbol)
			print(latest_stock_price[u'LastTradePriceOnly'])
			if latest_stock_price[u'LastTradePriceOnly'] < 2.00:
				short_list.append(symbol)

	with open("symbols_short_list.csv", "wb") as file:
		writer = csv.writer(file)
		writer.writerow(short_list)

if __name__ == '__main__':
    main()
