from __future__ import print_function
import requests
from bs4 import BeautifulSoup, Tag, NavigableString
from pymongo import MongoClient
from pprint import pprint
from os import path
import json


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
    PORT = 27017
    client = MongoClient(host, PORT)
    db = client.literature
    if dbName == 'literature':
        db = client.literature
    else:
        return None
    serverStatusResult = db.command("serverStatus")
    pprint(serverStatusResult)
    if collectionName == 'kahani':
        collection = db['kahani']
    elif collectionName == 'doha':
        collection = db['doha']
    elif collectionName == 'kavita':
        collection = db['kavita']
    elif collectionName == 'muhavare':
        collection = db['muhavare']
    else:
        return None
    return collection



def saveToLocalDB(fileName, content):
    filePath = path.relpath(fileName)
    with open (filePath, 'w') as outfile:
        json.dump(content, outfile)


def viewCollection(collection):
    cursor = collection.find({})
    c = 0
    for document in cursor:
        c = c + 1
        print(document)
    print("Number of documents: ", c)
