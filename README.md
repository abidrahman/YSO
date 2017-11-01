# Young Stock Observer

The Young Stock Observer scrapes the web for all stock information, while allowing the user to filter the results using adjustable indicators.

**Still under development**

### Prerequisites

Using the real time stock library, rtstock, the YSO retrieves stock information about all NASDAQ stocks from Yahoo Finance. 

Find out more about rtstock: https://realtime-stock.readthedocs.io/en/latest/

```
pip install realtime-stock
```

## How to Run

To use the YSO, simply naviagate to the project directory, 

```
> python main.py
Welcome to the Young Stock Observer.
Enter stock file:
```

The YSO will allow the user to enter a filename (.csv) that incudes the stock symbols to be used. The file provided with the repo, symbols.csv, includes a list of ALL stocks listed on the NASDAQ as of July, 2017.

After entering the name of the stock file, the user will be prompted with the options of enabling/disabling several indicators. The indicators currently implimented are the following:

1) Price Filter
	- Allows the user to set a minimum stock price. Only stocks under the set price will be returned. Eg. Searching for all stocks under $2.00.

```
Would you like to add a price filter? (Y/N): Y
Enter maximum price: 2.00
```

2) Volume Multiplier
	- Allows the user to set a volume multiplier filter on the list of stocks. The volume indicator can be useful in spotting 'hot' stocks with a high increase in volume. The volume multiplier queries the fifty day moving average of the stock and compares it with the volume of the previous day using the following equation using the following equation, only stocks that meet this condition will be returned: 
```
//Equation: prev_day_volume > fifty_day_avg_volume * volume_multiplier

Would you like to use the volume indicator? (Y/N): Y
Enter minimum volume multiplier: 2
```
	
3) News Indicator
	- Allows the user to add a News filer on the list of stocks. The news indicator scrapes the nasdaq website for news articles relating to each stock. If the news indicator is added, the list of stocks will be sorted based on the date of the last press release of that stock. The output will also include the headline of the last press release.
```
Would you like to use the news indicator? (Y/N): Y
```

The YSO will prompt the user to enter the name for an output file (.csv).

--Current implementation prints the stock name out to the terminal as the volume and news values are queried--

## Todo

- Create a database to store stock prices with stock recommendations.