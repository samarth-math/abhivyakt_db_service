from __future__ import print_function
import requests
from bs4 import BeautifulSoup, Tag, NavigableString
from pprint import pprint
import helperfunctions as H
import os
import threading
import pdb
import pickle
import json
# collection = H.initializeDB('literature', 'kahani')
count = 0
baseURL = "http://dsalsrv02.uchicago.edu"

import sys
#sys.setrecursionlimit(200000)
def parseDictionary(url, fileName):
    # global count
    # global baseURL
    # dictlist = []
    print("parsing file", url)
    entries = []
    try:
        print("parsing")
        soup = H.getSoup(url)
        print("extracting")
        # div = soup.find('div2', {'type': 'article'})
        #td = soup.find('td', {'align': 'right'})
        #nextPageURL = td.a.get('href')
        total_count = 0
        count = 0
        for word in soup.find_all('div2',{"type":"article"}):
            total_count += 1
            try:
                id = word['id']
                key = word.find('span',{'class':'hi'})
                meanings  = [content for content in word.d.contents]
                entry = {"id":id,"key":key,"meanings":meanings}
                entries.append(entry)
                count += 1
            except:
                #pdb.set_trace()
                print("error occured")
        print(total_count,count)
        print("saving content")

        #filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),"Content","dictionary-dsalsrv",fileName+".pkl")
        #pdb.set_trace()
        pickle.dump(entries,open("Content\\"+fileName+".pkl","wb"))
        print("done")
        # for word in soup.find_all('span',{'class':'hi'}):
        #     count += 1
        #print "Hello", count
        return count
        # word = soup.find('span', {'class': 'hi'}).text
        # meanings = []
        # meaning = soup.find_all('d')
        # for meaning in soup.find_all('d'):
        #     meanings.append(meaning.text)
        # pdb.set_trace()
        # #dictlist.append(baseURL + nextPageURL)
        # count += 1
        #print(nextPageURL)
        #url = baseURL + nextPageURL
        # for d in div:
        #    span = d.find('span', {'class': 'hi'})
        #    print('word: ', span.getText())
        #    count += 1
        # return nextPageURL
    except Exception as e:
        print("Encountered exception, save to disk and return", e)
        errorFileName = "Error_" + fileName
        #H.saveToLocalDB(errorFileName, e)
    # finally:
    #     #H.saveToLocalDB(fileName, dictlist)
    #     return True


try:
    # url = "/cgi-bin/philologic/getobject.pl?c.0:1:1.dasahindi"
    # url = "/cgi-bin/philologic/getobject.pl?p.0:0.dasahindi"
    # url = "/cgi-bin/philologic/getobject.pl?c.1:1:0.dasahindi"
    # url = "/cgi-bin/philologic/getobject.pl?c.2:1:0.dasahindi"
    numSeed = 20
    threads = []
    middleURL = "/cgi-bin/philologic/getobject.pl?c."
    endURL = ":1.dasahindi"
    urls = []
    for i in range(0,numSeed+1):
        url = baseURL + middleURL + str(i) + endURL
        print(url)
        urls.append(url)
    #pdb.set_trace()
    for i in range(numSeed+1):
        fileName = "dictionaryJSON" + str(i)
        # thr = threading.Thread(
        #     target=parseDictionary, args=(urls[i], fileName), kwargs={})
        # threads.append(thr)
        # thr.start()
        counts =  parseDictionary(urls[i],fileName)
        pprint(counts)
    # for i in range(numSeed):
    #     threads[i].join()
finally:
    print("No. of words: ", count)
