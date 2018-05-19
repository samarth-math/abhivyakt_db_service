from __future__ import print_function
import requests
from bs4 import BeautifulSoup, Tag, NavigableString
from pymongo import MongoClient
from pprint import pprint
from os import path
import json
import urllib.parse


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


def saveToMongoDB(collection, entry):
    try:
        collection.insert_one(entry)
        return True
    except Exception as e:
        print("Error in saving to MongoDB: ", e)
        return False


def initializeDB(dbName, collectionName):
    host = 'localhost'
    PORT = '27017'
    username = 'public'
    password = 'mongo@mongo'
    URL = 'mongodb://' + urllib.parse.quote_plus(username) + ':' + urllib.parse.quote_plus(
        password) + '@' + host + ':' + PORT + '/literature'
    print(URL)
    client = MongoClient(URL)
    dbNames = set(['literature'])
    collections = set(['kahani', 'dohe', 'dictionary', 'kavita', 'muhavare'])
    if dbName in dbNames:
        db = client[dbName]
        if collectionName in collections:
            return db[collectionName]
    return None


def saveToLocalDB(fileName, content):
    filePath = path.relpath(fileName)
    with open (filePath, 'w') as outfile:
        json.dump(content, outfile)


def viewCollection(collection):
    c = collection.find({}).count()
    print("Number of documents: ", c)
