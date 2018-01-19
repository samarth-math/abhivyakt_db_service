#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from time import sleep

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


testMuhavare()
