import json
import urllib.parse
from os import path
from bson.objectid import ObjectId

from pymongo import MongoClient

def save_to_db(collection, entry):
    try:
        collection.insert_one(entry)
    except Exception as e:
        print("Error in saving to MongoDB: ", e)


def initialize_db(dbName, collectionName):
    host = 'localhost'
    PORT = '27017'
    username = 'root1'
    password = 'password'
    URL = 'mongodb://' + urllib.parse.quote_plus(username) + ':' + \
        urllib.parse.quote_plus(password) + '@' + host + ':' + \
        PORT + '/admin'
    print(URL)
    client = MongoClient(URL)
    dbNames = set(['literature'])
    collections = set(['kahani', 'dohe', 'dictionary', 'kavita', 'muhavare'])
    if dbName in dbNames:
        db = client[dbName]
        if collectionName in collections:
            return db[collectionName]
    return None


def update_entry(collection, object, fieldName, updatedFieldValue):
    print("Updating object's (" + str(object['_id']) + ") field " + fieldName)
    try:
        collection.update_one({
            '_id': object['_id']
            },{
            '$set': {
            fieldName : updatedFieldValue
            }
        }, upsert=False)
    except Exception as e:
        print(e)

def remove_entry(collection, object):
    print("Removing object with id: " + str(object['_id']) + " from database")
    try:
        collection.remove({ '_id' : ObjectId(object['_id'])})
    except Exception as e:
        print(e)


# Helper function to view an entire collection.
def view_collection(collection):
    collection.find({})
