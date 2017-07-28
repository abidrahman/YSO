from bs4 import BeautifulSoup
import urllib

def getURL(symbol):
    return "http://www.nasdaq.com/symbol/" + symbol

def getHtml(urlString):
    return urllib.urlopen(urlString).read()

def getSoup(htmlString):
    return BeautifulSoup(htmlString, 'html.parser')

def findVolume(soup, symbol):
    volumeLabel = soup.find(id=symbol.upper()+"_Volume")
    return volumeLabel.string

def fiftyDayAverageVolume(soup, symbol):
    volumeLabel = soup.find(id=symbol.upper()+"_Volume")
    tag = volumeLabel.parent.patent
    avgVolumeRow = volumeLabel.parent.parent.next_sibling.next_sibling
    avgVolume = avgVolumeRow.contents[3]
    return avgVolume.string

if __name__ == "__main__":
    symbol = raw_input("Please enter a symbol: ")
    url = getURL(symbol)
    html = getHtml(url)
    soup = getSoup(html)
    volume = findVolume(soup, symbol)
    avgVolume = fiftyDayAverageVolume(soup, symbol)
    print("Day       | 50 day Avg")
    print(volume + " : " + avgVolume)
