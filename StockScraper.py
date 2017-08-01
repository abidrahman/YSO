from bs4 import BeautifulSoup
import urllib

attributes = {
"previous close": "PREV_CLOSE-value",
"open": "OPEN-value",
"bid": "BID-value",
"ask": "ASK-value",
"days range": "DAYS_RANGE-value",
"years range": "FIFTY_TWO_WK_RANGE-value",
"volume": "TD_VOLUME-value",
"average volume": "AVERAGE_VOLUME_3MONTH-value",
"market cap": "MARKET_CAP-value",
"beta": "BETA-value",
"pe ratio": "PE_RATIO-value",
"eps ratio": "EPS_RATIO-value",
"earnings date": "EARNINGS_DATE-value",
"dividend and yield": "DIVIDEND_AND_YIELD-value",
"exdividend rate": "EXDIVIDEND_DATE-value",
"one year target": "ONE_YEAR_TARGET_PRICE-value"
}

def getURL(symbol):
    return "https://ca.finance.yahoo.com/quote/" + symbol

def getHtml(urlString):
    return urllib.urlopen(urlString).read()

def getSoup(htmlString):
    return BeautifulSoup(htmlString, 'html.parser')

def getDataPoint(soup, attrString):
    try:
        return soup.find(attrs={"data-test": attributes[attrString]}).find("span").string
    except AttributeError:
        return "NA"

def getAllData(symbol):
    url = getURL(symbol)
    html = getHtml(url)
    soup = getSoup(html)
    data = {}
    for attr in attributes.keys():
        data[attr] = getDataPoint(soup, attr) 

if __name__ == "__main__":
    symbol = raw_input("Please enter a symbol: ")
    url = getURL(symbol)
    html = getHtml(url)
    soup = getSoup(html)
    for attr in attributes.keys():
        print attr + ": " + str(getDataPoint(soup, attr))
