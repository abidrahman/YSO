from bs4 import BeautifulSoup
import urllib

def getURL(symbol):
    return "http://www.nasdaq.com/symbol/" + symbol + "/press-releases"

def getHtml(urlString):
    return urllib.urlopen(urlString).read()

def getSoup(htmlString):
    return BeautifulSoup(htmlString, 'html.parser')

def findMostRecentPressDateString(soup, symbol):
    try:
        newsTable = soup.find_all('div', {'class': 'news-headlines'})[0]
        articles = newsTable.find_all('a')
        dateString = articles[0].parent.find_next_sibling('small').string.strip().split()[0]
        return dateString
    except:
        return "NA"

if __name__ == "__main__":
    symbol = raw_input("Please enter a symbol: ")
    url = getURL(symbol)
    html = getHtml(url)
    soup = getSoup(html)
    print findMostRecentPressDateString(soup, symbol)
