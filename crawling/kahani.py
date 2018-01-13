from __future__ import print_function
import requests
from bs4 import BeautifulSoup, Tag, NavigableString
from pymongo import MongoClient
from pprint import pprint
import helperfunctions as H

collection = H.initializeDB('literature', 'kahani')


def parseKahani():
    baseURL = "http://www.hindikibindi.com/content/manoranjan/stories/"
    soup = H.getSoup(baseURL)
    div = soup.find('div', {'class': 'col-lg-12'})
    p = div.find_next('p').find_all('a')
    for a in p:
        print(a.get('href'))
        kahaniText = u''
        title = u''
        absURL = baseURL + a.get('href')
        soup = H.getSoup(absURL)
        div = soup.find('div', {'class': 'col-lg-12'})
        p = div.find_next('p').getText()
        title = p.partition('\n')[0]
        for br in div.find_next('p').findAll('br'):
            next_s = br.nextSibling
            if not (next_s and isinstance(next_s, NavigableString)):
                continue
            next2_s = next_s.nextSibling
            if next2_s and isinstance(next2_s, Tag) and next2_s.name == 'br':
                text = next_s
                if text:
                    kahaniText = kahaniText + next_s
        print(title)
        print(kahaniText)
        entry = {
            'title': title,
            'kahaniText': kahaniText
        }
        H.saveToMongoDB(collection, entry)


def parsePremchandKahani():
    global collection
    url = 'http://premchand.kahaani.org/2009/09/contents.html'
    soup = H.getSoup(url)
    div = soup.find('div', {'class': 'nobrtable'})
    li = div.find_next('tr').find_all('li')
    count = 0
    for links in li:
        print(links.a.get('href'))
        soup = H.getSoup(links.a.get('href'))
        div = soup.find('div', {'class': 'post-body entry-content'})
        kahaniText = div.getText()
        title = soup.find('meta', property='og:title')["content"]
        print(title)
        print(kahaniText)
        entry = {
            "title": title,
            "kahaniText": kahaniText,
            "author":  "Munshi Premchand"
        }
        H.saveToMongoDB(collection, entry)
        count += 1
    print("No. of links: ", count)


try:
    # parseKahani()
    # parsePremchandKahani()
    H.viewCollection(collection)
finally:
    print("Completed")
