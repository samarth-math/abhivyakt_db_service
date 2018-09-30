import requests
from bs4 import BeautifulSoup, Tag, NavigableString
from pymongo import MongoClient
from pprint import pprint
from os import path
import json
import urllib.parse
from api.globalHelpers.utilities import logger
from api.configurations.credentials import login


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
    db = getDBHandler(dbName)
    dbNames = set(['literature'])
    collections = set(['kahani', 'dohe', 'dictionary',
                       'kavita', 'muhavare', 'author'])
    if dbName in dbNames:
        if collectionName in collections:
            return db[collectionName]
    return None


def saveToLocalFile(fileName, content):
    filePath = path.relpath(fileName)
    with open(filePath, 'w') as outfile:
        json.dump(content, outfile)


def viewCollection(collection):
    c = collection.find({}).count()
    print("Number of documents: ", c)


def getDBHandler(dbName):
    """[This method returns database handler which
    is used by methods for saving and retrieving files.]

    Arguments:
        db_name {[string]} -- [name of the database]

    Returns:
        [type] -- [returns db handler]
    """

    host = 'localhost'
    PORT = '27017'
    username = login['username']
    password = login['password']
    URL = 'mongodb://' + urllib.parse.quote_plus(username) + ':' + \
        urllib.parse.quote_plus(password) + '@' + host + ':' + \
        PORT + '/' + dbName
    client = MongoClient(URL)
    db = client[dbName]

    return db
