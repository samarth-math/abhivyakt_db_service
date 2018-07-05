import json
import urllib.parse
from os import path

from pymongo import MongoClient


def save_to_mongo_db(collection, entry):
    try:
        # collection.insert_one(entry)
        return True
    except Exception as e:
        print("Error in saving to MongoDB: ", e)
        return False


def initialize_db(dbName, collectionName):
    host = 'localhost'
    PORT = '27017'
    username = 'public'
    password = 'mongo@mongo'
    URL = 'mongodb://' + urllib.parse.quote_plus(username) + ':' + \
        urllib.parse.quote_plus(password) + '@' + host + ':' + \
        PORT + '/literature'
    print(URL)
    client = MongoClient(URL)
    dbNames = set(['literature'])
    collections = set(['kahani', 'dohe', 'dictionary', 'kavita', 'muhavare'])
    if dbName in dbNames:
        db = client[dbName]
        if collectionName in collections:
            return db[collectionName]
    return None


def save_to_local_db(fileName, content):
    filePath = path.relpath(fileName)
    with open(filePath, 'w') as outfile:
        json.dump(content, outfile)


def update_entry(collection, field, updatedField):
    pass


def remove_entry(collection, id):
    pass


# Helper function to view an entire collection.
def view_collection(collection):
    collection.find({})
