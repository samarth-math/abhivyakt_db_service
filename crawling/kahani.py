from __future__ import print_function
import requests
from bs4 import BeautifulSoup, Tag, NavigableString
from pymongo import MongoClient
from pprint import pprint

baseURL = "http://www.hindikibindi.com/content/manoranjan/stories/"
numKavitaG = 0
kavitalist = []
invalidKavitaList = []
invalidKavitaG = 0
invalidBirthSpanG = 0
invalidBirthSpanList = []

host = 'localhost'
PORT = 27017
client = MongoClient(host, PORT)
db = client.literature
serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult)
collection = db['kahani']
cursor = collection.find({})
c = 0
for document in cursor:
    c = c + 1
    print(document)

print("Number of documents: ", c)


def getSoup(url):
    try:
        page = requests.get(url)
        encoding = page.encoding if 'charset' in page.headers.get(
            'content-type', '').lower() else None
    except requests.exceptions.ConnectionError as r:
        r.status_code = "Connection Refused"
        return None
    soup = BeautifulSoup(page.content, 'lxml', from_encoding=encoding)
    return soup


def parseKahani():
    soup = getSoup(baseURL)
    div = soup.find('div', {'class': 'col-lg-12'})
    p = div.find_next('p').find_all('a')
    for a in p:
        print(a.get('href'))
        kahaniText = u''
        title = u''
        absURL = baseURL + a.get('href')
        soup = getSoup(absURL)
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
        saveToMongoDB(entry)


def saveToMongoDB(entry):
    global db
    db.kahani.insert_one(entry)


try:
    # parseKahani()
    doNothing = 1
finally:
    print("Completed")
