import json
import urllib.parse
from os import path
from pprint import pprint

import chardet
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from pymongo import MongoClient

import databaseHelperFunctions as db

fieldDict = {
    'kavita': ['content', 'title'],
    'kahani': ['kahaniText', 'title'],
    'dohe': ['doha', 'meaning'],
    'muhavare': ['muhavara', 'meaning'],
    'dictionary': ['id', 'key', 'meanings']
}

indexDict = {
    'kavita': [("content", "text")],
    'kahani': [("kahaniText", "text")],
    'dohe': [("doha", "text")],
    'muhavare': [("muhavara", "text")],
    'dictionary': [("key", "text")]
}
collectionList = ['kavita', 'kahani', 'dohe', 'muhavare', 'dictionary']
collectionDict = {}


def run_cleaning_tasks():
    for k, vl in fieldDict.items():
        # get_indexes(collectionDict[k])
        print('Collection: ', k)
        for v in vl:
            # print('key ', k, ' val: ', v)
            find_and_remove_empty_entries(collectionDict[k], v)
            find_html_tags(collectionDict[k], v)
            remove_bom(collectionDict[k], v)


# Function to remove BOM characters from a field and update the entry
# in database.
def remove_bom(collection, field):
    c = collection.find({})
    BOM = '\ufeff'
    for data in c:
        if BOM in data[field]:
            fieldWithoutBOM = data[field].translate(
                {ord(c): None for c in BOM})
            db.update_entry(collection, field, fieldWithoutBOM)


# Find if a given field has HTML data.
def find_html_tags(collection, field):
    c = collection.find({})
    count = 0
    try:
        for data in c:
            if BeautifulSoup(data[field], "html.parser").find():
                print("HTML content found!")
                print('Data: ', data['_id'])
                db.remove_entry(collection, data['_id'])
                count += 1
    except:
        print('Exception in data: ', data[field])
    print("Number of documents with HTML tags: ", count, ' and field ', field)


# Function to find and remove all empty entries (field) for a given collection.
def find_and_remove_empty_entries(collection, field):
    c = collection.find({})
    count = 0
    for data in c:
        if not data[field]:
            print("Empty Content!")
            db.remove_entry(collection, data['_id'])
            count += 1
    print("Number of empty documents: ", count, ' and field ', field)


# Function to create index according to scheme define in indexDict dictionary.
def create_indexes():
    for k, vl in indexDict.items():
        create_index(collectionDict[k], vl)
        print('After creating...')
        get_indexes(collectionDict[k])
        drop_index(collectionDict[k], vl)
        print('After dropping...')
        get_indexes(collectionDict[k])


# Function to index a collection on the keys.
def create_index(collection, keys):
    collection.create_index(keys)


# Function to output all the indexes of a collection.
def get_indexes(collection):
    indexes = collection.list_indexes()
    for index in indexes:
        print('Index: ', index)
    # print("Total number of indexes: ", len(indexes))


# Function to drop an index from a collection..
def drop_index(collection, index):
    collection.drop_index(index)


if __name__ == '__main__':
    for c in collectionList:
        dbHandler = db.initialize_db('literature', c)
        collectionDict[c] = dbHandler
        db.view_collection(dbHandler)

    # Add tasks here for cleaning the database.
    run_cleaning_tasks()
    create_indexes()
