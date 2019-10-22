"""
import requests
from bs4 import BeautifulSoup


def spider(maxPages):
    page = 1
    while page <= maxPages:
        url = 'https://www.ebay.com/b/Pro-Audio-Equipment/180014/bn_1865231?_pgn=' + str(page)
        sourceCode = requests.get(url)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText, features="html.parser")
        for link in soup.findAll('a', {'class': 's-item__title'}):
            title = link.string
            print(title)
            href = link.get('href')
        page += 1

spider(1)
"""
import threading

class ForkyMassenger(threading, Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = ForkyMassenger(name='Send out messages')
y = ForkyMassenger(name='Receive messages')
x.start()
y.start()
