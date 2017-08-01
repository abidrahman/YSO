from bs4 import BeautifulSoup
import urllib

def newsIndicator(symbol):
    url = getURL(symbol)
    html = getHtml(url)
    soup = getSoup(html)
    return (getRecentPressDateString(soup, symbol), getRecentPressTitle(soup))

def getURL(symbol):
    return "http://www.nasdaq.com/symbol/" + symbol + "/press-releases"

def getHtml(urlString):
    return urllib.urlopen(urlString).read()

def getSoup(htmlString):
    return BeautifulSoup(htmlString, 'html.parser')

def getRecentPressDateString(soup, symbol, articleNumber=0):
    try:
        newsTable = soup.find_all('div', {'class': 'news-headlines'})[0]
        articles = newsTable.find_all('a')[articleNumber]
        dateString = articles.parent.find_next_sibling('small').string.strip().split()[0]
        return dateString.encode()
    except:
        return "1/1/2000"

def getRecentPressTitle(soup, articleNumber=0):
    try:
        newsTable = soup.find_all('div', {'class': 'news-headlines'})[0]
        return newsTable.find_all('a')[articleNumber].string
    except:
        return "NA"

def getRecentPressText(soup, articleNumber=0):
    try:
        newsTable = soup.find_all('div', {'class': 'news-headlines'})[0]
        articleUrl = newsTable.find_all('a')[articleNumber].get('href')
        articleSoup = getSoup(getHtml(articleUrl))
        articleBody = articleSoup.find(id="articlebody")
        paragraphs = articleBody.find_all('p')
        articleText = "\n\t".join([paragraph.string for paragraph in paragraphs if paragraph.string is not None])
        return articleText
    except:
        return "NA"

if __name__ == "__main__":
    symbol = raw_input("Please enter a symbol: ")
    url = getURL(symbol)
    html = getHtml(url)
    soup = getSoup(html)

    print getRecentPressTitle(soup)
    print getRecentPressDateString(soup, symbol)
    print getRecentPressText(soup)
