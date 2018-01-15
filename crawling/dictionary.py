from __future__ import print_function
import requests
from bs4 import BeautifulSoup, Tag, NavigableString
from pymongo import MongoClient
from pprint import pprint
import helperfunctions as H
import threading

# collection = H.initializeDB('literature', 'kahani')
count = 0
baseURL = "http://dsalsrv02.uchicago.edu"


def parseDictionary(url, fileName):
    global count
    global baseURL
    dictlist = []
    try:
        while(True):
            soup = H.getSoup(url)
            # div = soup.find('div2', {'type': 'article'})
            td = soup.find('td', {'align': 'right'})
            nextPageURL = td.a.get('href')
            dictlist.append(baseURL + nextPageURL)
            count += 1
            print(nextPageURL)
            url = baseURL + nextPageURL
            # for d in div:
            #    span = d.find('span', {'class': 'hi'})
            #    print('word: ', span.getText())
            #    count += 1
            # return nextPageURL
    except Exception as e:
        print("Encountered exception, save to disk and return", e)
        errorFileName = "Error_" + fileName
        H.saveToLocalDB(errorFileName, e)
    finally:
        H.saveToLocalDB(fileName, dictlist)
        return True


try:
    # url = "/cgi-bin/philologic/getobject.pl?c.0:1:1.dasahindi"
    # url = "/cgi-bin/philologic/getobject.pl?p.0:0.dasahindi"
    # url = "/cgi-bin/philologic/getobject.pl?c.1:1:0.dasahindi"
    # url = "/cgi-bin/philologic/getobject.pl?c.2:1:0.dasahindi"
    numSeed = 21
    threads = []
    middleURL = "/cgi-bin/philologic/getobject.pl?c."
    endURL = ":1:0.dasahindi"
    urls = []
    for i in range(numSeed):
        url = baseURL + middleURL + str(i) + endURL
        print(url)
        urls.append(url)

    for i in range(numSeed):
        fileName = "dictionaryJSON" + str(i)
        thr = threading.Thread(
            target=parseDictionary, args=(urls[i], fileName), kwargs={})
        threads.append(thr)
        thr.start()

    for i in range(numSeed):
        threads[i].join()
finally:
    print("No. of words: ", count)
