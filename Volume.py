from bs4 import BeautifulSoup
import urllib

def volumeIndicator(symbol, multiplier):
    url = getURL(symbol)
    html = getHtml(url)
    soup = getSoup(html)
    try:
        volume = int(findVolume(soup, symbol).replace(',',''))
        avgVolume = int(fiftyDayAverageVolume(soup, symbol).replace(',',''))
    except ValueError:
        return [False, 'NA', 'NA']
    volume_spiked = (volume > avgVolume * multiplier)
    return [volume_spiked, volume, avgVolume]

def getURL(symbol):
    return "http://www.nasdaq.com/symbol/" + symbol

def getHtml(urlString):
    return urllib.urlopen(urlString).read()

def getSoup(htmlString):
    return BeautifulSoup(htmlString, 'html.parser')

def findVolume(soup, symbol):
    volumeLabel = soup.find(id=symbol.upper()+"_Volume")
    try:
        return volumeLabel.string
    except AttributeError:
        return "NA"

def fiftyDayAverageVolume(soup, symbol):
    volumeLabel = soup.find(id=symbol.upper()+"_Volume")
    tag = volumeLabel.parent.patent
    avgVolumeRow = volumeLabel.parent.parent.next_sibling.next_sibling
    avgVolume = avgVolumeRow.contents[3]
    try:
        return avgVolume.string
    except AttributeError:
        return "NA"

if __name__ == "__main__":
    symbol = raw_input("Please enter a symbol: ")
    url = getURL(symbol)
    html = getHtml(url)
    soup = getSoup(html)
    volume = findVolume(soup, symbol)
    avgVolume = fiftyDayAverageVolume(soup, symbol)
    print("Day       | 50 day Avg")
    print(volume + " : " + avgVolume)
