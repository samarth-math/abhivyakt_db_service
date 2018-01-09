from __future__ import print_function
from time import sleep
import requests
import json
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from os import path
from pymongo import MongoClient
from pprint import pprint

baseURL = "http://kavitakosh.org"
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
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
collection = db['kavita']
cursor = collection.find({})
c = 0
for document in cursor:
      c = c +1
      print(document)

print ("Number of documents: ", c)

def parseKavitaKosh():
    try:
        page = requests.get(baseURL)
        encoding = page.encoding if 'charset' in page.headers.get('content-type', '').lower() else None
    except requests.exceptions.ConnectionError:
        r.status_code = "Connection Refused"
    soup = BeautifulSoup(page.content, 'lxml', from_encoding=encoding)
    # print(soup.prettify())
    al = []
    div = soup.find_all("div", {"class": "poet-list-section"})
    for d in div:
        kl = d.find_next('ul').find_all('li')
        for l in kl:
            if l is not None and l.a is not None and l.a.has_attr('href'):
                al.append(l.a.get('href'))

    print("Total authors: ", len(al))
    pool = ThreadPoolExecutor(30)
    futures = [pool.submit(getKavitaList,author) for author in al]
    results =  [r.result() for r in as_completed(futures)]

def getKavitaList(author):
    global numKavitaG
    global invalidKavitaG
    global invalidBirthSpanG
    url = baseURL + author
    try:
        kavitaPage = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)

    kavitaPage = requests.get(url)
    kavitaSoup = BeautifulSoup(kavitaPage.content, 'lxml')
    births_span = kavitaSoup.find("div", {"id":"kkparichay-lower-border"})
    if births_span is None or births_span.find_next('ul') is None:
        print ("births_span is None")
        kl = None
        invalidBirthSpanG = invalidBirthSpanG + 1
        invalidBirthSpanList.append(births_span)
    else:
        kl = births_span.find_next('ul').find_all('li')
        for l in kl:
            if l is not None and l.a is not None and l.a.has_attr('href'):
                numKavitaG = numKavitaG + 1
                print("Poems link: ", l.a.get('href'))
                kavitalist.append(l.a.get('href'))
                if numKavitaG % 100 == 0:
                    print ("Total number of kavitas: ", numKavitaG)
            else:
                invalidKavitaList.append(l)
                invalidKavitaG = invalidKavitaG + 1
    return kl

def getWikiInfo():
    wikiInfo = ""

def saveToMongoDB(entry):
    global db
    db.kavita.insert_one(entry)

def parseKavita(relURL):
    try:
        global db
        url = baseURL + relURL
        print(url)
        page = requests.get(url)
        ksoup = BeautifulSoup(page.content, 'lxml')
        title = ksoup.find("span", {"dir":"auto"}).text
        try:
            tsplit = title.split('/')
            poemTitle = tsplit[0]
            poemAuthor = tsplit[1]
        except:
            poemTitle = title
            poemAuthor = ""
        tags = []
        pDiv = ksoup.find("div", {"class":"poem"})
        if pDiv is not None and pDiv.find_next('p') is not None:
            poemText = pDiv.find_next('p').getText()
        else:
            poemText = ""
        pfooter = ksoup.find("div", {"class":"printfooter"})
        if pfooter is not None and pfooter.find_next('ul') is not None:
            for l in pfooter.find_next('ul').find_all('li'):
                if l is not None and l.a is not None and l.a.text is not None:
                    tags.append(l.a.text)
                    print("Tags: ", l.a.text)
        print("Author:", poemAuthor, "Title: ", poemTitle, " Poem Text: ", poemText)
        entry = {
            'authorName': poemAuthor,
            'title':poemTitle,
            'content':poemText,
            'tags':tags,
            'source':url
        }
        saveToMongoDB(entry)
        #print(ksoup.prettify())
    except requests.exceptions.ConnectionError as r:
        r.status_code = "Connection Refused"


def saveKavitaListToDB():
    kavitaFileName = path.relpath("kavita")
    kavitaInvalidFileName = path.relpath("invalidkavita")
    invalidBirthSpanFileName = path.relpath("invalidspan")
    print ("Total kavita: ", numKavitaG)
    print ("Total invalid kavita: ", invalidKavitaG)
    print ("Total invalid birthspan: ", invalidBirthSpanG)
    with open (kavitaFileName, 'w') as outfile:
        json.dump(kavitalist, outfile)

    with open(kavitaInvalidFileName, 'w') as outf:
        json.dump(invalidKavitaList, outf)

    with open(invalidBirthSpanFileName, 'w') as outf:
        json.dump(invalidBirthSpanList, outf)

def loadKavitaFromDB():
    kavitaFileName = path.relpath("kavita")
    kavitalist = json.loads(open("/home/rishabh/Projects/hindived/kavita", 'r').read())
    print("Total kavit links: ", len(kavitalist))
    for k in kavitalist:
        parseKavita(k)
    print("loaded kavita from DB")

try:
    #parseKavitaKosh()
    #loadKavitaFromDB()
    print ("")

finally:
    #saveKavitaListToDB()
    print("Completed")
