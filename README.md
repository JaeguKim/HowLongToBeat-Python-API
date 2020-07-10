# HowLongToBeat Python API
[![Build Status](https://travis-ci.com/JaeguKim/HowLongToBeat-Python-API.svg?branch=master)](https://travis-ci.com/JaeguKim/HowLongToBeat-Python-API)   
You can easily search play-time of specific game you want to know by using this package.   

## Usage
## How To Install
```python
pip install HowLongToBeat-Python-API
```
## How To Use

### Import 
```python
from hltbapi import HtmlScraper
```
### Example 
```python
res = HtmlScraper().search(name='last of us') #res contains following data of games containing 'last of us'
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
```

## Authors

* **JaeguKim**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details