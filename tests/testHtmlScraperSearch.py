from hltbapi import HtmlScraper

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