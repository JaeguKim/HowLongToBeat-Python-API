from unittest import TestCase
from hltbapi import HtmlScraper,HowLongToBeatEntry
from typing import List

class TestSearch(TestCase):

    def test(self):
        res = HtmlScraper().search(name='last of us')
        self.assertIsNotNone(res)
        self.assertGreater(len(res),0)

    # @staticmethod
    # def testEntry(res):
    #     for entry in res:
    #         print('===================================')
    #         print(entry.detailId)
    #         print(entry.gameName)
    #         print(entry.description)
    #         print(entry.playableOn)
    #         print(entry.imageUrl)
    #         print(entry.timeLabels)
    #         print(entry.gameplayMain)
    #         print(entry.gameplayMainExtra)
    #         print(entry.gameplayCompletionist)
    #         print('===================================')

