from __future__ import print_function
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pprint import pprint

# To parse all kavitas, initially all kavita links
# were save to local db (in json format). Finally
# using the local database all poems were crawled and saved to MongoDB.

baseURL = "https://hindividya.com/kabir-ke-dohe/"
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
collection = db['kavita']
cursor = collection.find({})
c = 0
for document in cursor:
    c = c + 1
    print(document)

print("Number of documents: ", c)


def parseDohe():
    try:
        page = requests.get(baseURL)
        encoding = page.encoding if 'charset' in page.headers.get(
            'content-type', '').lower() else None
    except requests.exceptions.ConnectionError as r:
        r.status_code = "Connection Refused"
    soup = BeautifulSoup(page.content, 'lxml', from_encoding=encoding)
    # print(soup.prettify())
    p = soup.find_all('p')
    dohaText = ""
    for e in p:
        t = e.contents
        for x in t:
            try:
                if x.find("Meaning") > -1:
                    print("doha: " + dohaText)
                    meaning = x
                    entry = {
                        'doha': dohaText,
                        'meaning': meaning,
                        'author': 'Kabir'
                    }
                    saveToMongoDB(entry)
                    dohaText = ""
                    print(meaning)
                elif (x.find("<input") > -1 or
                      ord(x[0]) < 128
                      or x.find("Kabir") > -1):
                    doNothing = 1
                else:
                    dohaText += x
            except:
                doNothing = 1


def saveToMongoDB(entry):
    global db
    db.dohe.insert_one(entry)


try:
    parseDohe()
    doNothing = 1
finally:
    print("Completed")
