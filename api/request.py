#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from time import sleep
from api.models import author
from api.globalHelpers import constants
from bson.objectid import ObjectId


def testKavita():
    #r = requests.get('http://127.0.0.1:5000/kavita?title=क')
    #r = requests.get('http://127.0.0.1:5000/kavita?author=क')
    r = requests.get('http://127.0.0.1:5000/kavita?=content=क')
    #r = requests.get('http://127.0.0.1:5000/kavita')
    print(r.status_code)
    #print(r.headers['content-type'])
    #print(r.json())
    js = r.json()
    data = js.get('data')
    hasMore = js.get('hasMore')
    print('hasMore; ', hasMore)
    #url = 'http://127.0.0.1:5000/kavita?title=क&nextItem=5a53082474ad350ba00ae83a'
    url = requests.get('http://127.0.0.1:5000/kavita')
    if hasMore is True:
        nextItem = js.get('nextItem')
        print ('url: ', nextItem)
        url = nextItem

    #print(type(data))
    #print(len(data))
    r = requests.get(url)
    print(r.status_code)
    #print(r.headers['content-type'])
    #print('2nd req. ',r.json())
    #js = r.json()
    # data = js.get('data')
    #print(type(data))
    hasMore = r.json().get('hasMore')
    print('2nd req. hasMore; ', hasMore)
    print(url)
    print(r.json().get('nextItem'))


def testMuhavare():
    r = requests.get('http://127.0.0.1:5000/muhavare?=content=क')
    r = requests.get('http://127.0.0.1:5000/muhavare')
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.json())
    js = r.json()
    data = js.get('data')
    hasMore = js.get('hasMore')
    print('hasMore; ', hasMore)
    url = requests.get('http://127.0.0.1:5000/')
    if hasMore is True:
        nextItem = js.get('nextItem')
        print ('url: ', nextItem)
        url = nextItem

    print(type(data))
    print(len(data))
    r = requests.get(url)
    print(r.status_code)
    print(r.headers['content-type'])
    print('2nd req. ',r.json())
    js = r.json()
    data = js.get('data')
    print(type(data))
    hasMore = r.json().get('hasMore')
    print('2nd req. hasMore; ', hasMore)
    print(url)
    print(r.json().get('nextItem'))




def testDohe():
    #r = requests.get('http://127.0.0.1:5000/dohe?author=क')
    r = requests.get('http://127.0.0.1:5000/dohe?limit=10')
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.json())
    js = r.json()
    data = js.get('data')
    hasMore = js.get('hasMore')
    print('hasMore; ', hasMore)
    url = requests.get('http://127.0.0.1:5000/')
    print(js.get('nextItem'))
    #if hasMore is True:
    #    nextItem = js.get('nextItem')
    #    print ('url: ', nextItem)
    #    url = nextItem

    #print(type(data))
    #print(len(data))
    #r = requests.get(url)
    #print(r.status_code)
    #print(r.headers['content-type'])
    #print('2nd req. ',r.json())
    #js = r.json()
    #data = js.get('data')
    #print(type(data))
    #hasMore = r.json().get('hasMore')
    #print('2nd req. hasMore; ', hasMore)
    #print(url)
    #print(r.json().get('nextItem'))


def testKahani():
    r = requests.get('http://127.0.0.1:5000/kahani?title=क')
    r = requests.get('http:/standalone/127.0.0.1:5000/kahani')
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.json())
    js = r.json()
    data = js.get('data')
    hasMore = js.get('hasMore')
    print('hasMore; ', hasMore)
    url = requests.get('http://127.0.0.1:5000/')
    if hasMore is True:
        nextItem = js.get('nextItem')
        print ('url: ', nextItem)
        url = nextItem

    print(type(data))
    print(len(data))
    r = requests.get(url)
    print(r.status_code)
    print(r.headers['content-type'])
    print('2nd req. ',r.json())
    js = r.json()
    data = js.get('data')
    print(type(data))
    hasMore = r.json().get('hasMore')
    print('2nd req. hasMore; ', hasMore)
    print(url)
    print(r.json().get('nextItem'))


try:
    #testKahani()
    #testMuhavare()
    testDohe()
except Exception as e:
    print(e)


##### Author object tests #####

def testFeaturedAuthor():
    return author.featuredAuthors()

def testGetAllAuthors():
    return author.getAllAuthors(10, None)

def testGetAuthorByName():
    return author.getAuthorByName('प्रेमनन्दन')

def testGetAuthorByDoha():
    doha = {
        "title": "कलजुगी दोहे",
        "authorName": "अंसार कम्बरी",
        "_id": "5a589b4274ad3522fbfd2cdf"
    }
    return author.getAuthorByContent(doha['_id'], constants.Art.dohe)


def testGetContentForAuthor():
    authorInfo = {
        "name": "कलजुगी",
        "dohe": [ObjectId("5a589b4274ad3522fbfd2cdc"), ObjectId("5a589b4274ad3522fbfd2cdf")]
    }
    return author.getContentForAuthor(authorInfo, constants.Art.dohe)