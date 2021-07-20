# propertyfinder-crawler
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)](https://www.python.org/)

Property Finder scrapper for python developers

## How to use ? :cowboy_hat_face:
1. install reuired packages `pip3 install scrapy`
2. run `python3 scrapper.py`

and **that's it**

## Extras :star2:
- you can specify the output file format (**default** is `json`) of the crawling process `python3 scrapper.py -t csv`
- you can change the name of the output file (**default** is the `datetime.today()`) like this `python3 scrapper.py -f output.json`
- And of course you can use both at the same time `python3 scrapper.py -t csv -f output.csv`
