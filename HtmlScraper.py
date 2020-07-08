from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
from urllib import parse
from .HowLongToBeatEntry import HowLongToBeatEntry
from typing import List

class HtmlScraper:
    BASE_URL = 'https://howlongtobeat.com'
    SEARCH_SUFFIX = 'search_results.php'

    def search(self,name:str)->List[HowLongToBeatEntry]:
        resHtml = self.getSearchResult(name)
        if resHtml:
            soup = bs(resHtml)
            parsedHtml = self.parseHtml(soup)
            return parsedHtml
        return None

    def getSearchResult(self,name:str)->str:
        body = {
            'queryString': name,
            't': 'games',
            'sorthead': 'popular',
            'sortd': 'Normal Order',
            'plat': '',
            'length_type': 'main',
            'length_min': '',
            'length_max': '',
            'detail': '0'
        }
        data = parse.urlencode(body).encode("utf-8")
        req = Request('{}/{}'.format(self.BASE_URL,self.SEARCH_SUFFIX),headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req,data=data) as f:
            resp = f.read().decode('utf-8')
            return resp
        return None

    def parseHtml(self,soup):
        results = []
        if len(soup.h3) > 0:
            liElements = soup.findAll('li')
            for elem in liElements:
                gameTitleAnchor = elem.findAll('a')[0]
                gameName = gameTitleAnchor.get('title')
                gameDescription = ''
                playableOn = []
                detailId = gameTitleAnchor.get('href')[gameTitleAnchor.get('href').index('?id=')+4:]
                gameImage = gameTitleAnchor.findAll('img')[0].get('src')
                timeLabels = []
                main = 0; mainExtra = 0; complete = 0
                gameTimeDivTags = elem.select("div[class*=search_list_tidbit]")
                #print(gameName)
                for i in range(len(gameTimeDivTags)):
                    line = str(gameTimeDivTags[i].string)
                    if line.startswith('Main Story') or line.startswith('Single-Player') or line.startswith('Solo'):
                        main = self.parseTime(str(gameTimeDivTags[i+1].string))
                        timeLabels.append('gameplayMain')
                        #print('MAIN STORY : {}'.format(main))
                    elif line.startswith('Main + Extra') or line.startswith('Co-Op'):
                        mainExtra = self.parseTime(str(gameTimeDivTags[i+1].string))
                        timeLabels.append('gameplayMainExtra')
                        #print('MAIN EXTRA : {}'.format(mainExtra))
                    elif line.startswith('Completionist') or line.startswith('Vs.'):
                        complete = self.parseTime(str(gameTimeDivTags[i+1].string))
                        timeLabels.append('gameplayCompletionist')
                        #print('COMPLETIONIST : {}'.format(complete))
                results.append(HowLongToBeatEntry(detailId,gameName,gameDescription,playableOn,gameImage,timeLabels,main,mainExtra,complete))
        return results
            
    def parseTime(self,text):
        if text.startswith('--'):
            return 0
        if ' - ' in text:
            return handleRange(text)
        return self.getTime(text)

    def handleRange(self,text):
        range = text.split(' - ')
        number = (self.getTime(range[0])+self.getTime(range[1]))/2
        return number

    def getTime(self,text):
        timeUnit = text[text.index(' ') + 1:]
        if timeUnit == 'Mins':
            return 1
        time = text[0:text.index(' ')]
        if '½' in time:
            return 0.5 + int(time[0:text.index('½')])
        return int(time)

def test():
    res = HtmlScraper().search(name='last of us')
    testEntry(res)

def testEntry(res):
    for entry in res:
        print('===================================')
        print(entry.detailId)
        print(entry.gameName)
        print(entry.description)
        print(entry.playableOn)
        print(entry.imageUrl)
        print(entry.timeLabels)
        print(entry.gameplayMain)
        print(entry.gameplayMainExtra)
        print(entry.gameplayCompletionist)
        print('===================================')

test()