import json
import urllib.parse
from os import path
from pprint import pprint

import chardet
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from pymongo import MongoClient
import indexing
import sys
import databaseHelperFunctions as db

fieldNameDict = {
    'kavita': ['content', 'title', 'authorName'],
    'kahani': ['kahaniText', 'title', 'author'],
    'dohe': ['doha', 'meaning', 'author'],
    'muhavare': ['muhavara', 'meaning'],
    'dictionary': ['id', 'key', 'meanings']
}

collectionDict = {}


# Driver function
def run_cleaning_tasks(delete = False):
    for collectionName, fieldNames in fieldNameDict.items():
        # get_indexes(collectionDict[collectionName])
        print('Collection: ', collectionName)
        for fieldName in fieldNames:
            # Add operations here you want to run on the db
            find_empty_entries(collectionDict[collectionName], fieldName, collectionName, delete)
            find_html_tags(collectionDict[collectionName], fieldName, collectionName, delete)
            find_bom(collectionDict[collectionName], fieldName, collectionName)
            


# Find if a given field has HTML data.
def find_html_tags(collection, fieldName, collectionName, delete = False):
    print("****** Analysing for HTML tags in " + collectionName + "[" + fieldName + "]" + " *****")
    allObjects = collection.find({})
    count = 0
    for object in allObjects:
        try:
            if BeautifulSoup(object[fieldName], "html.parser").find():
                print("HTML content found!" + str(object['_id']))
                if delete:
                    save(object)
                    db.remove_entry(collection, object)
                count += 1
        except Exception as e:
            print('Exception in object: ' + ' ' + str(e) + '\n content for ' + collectionName + '[' + fieldName + ']: ' + str(object[fieldName]))
            count += 1
    print("Number of documents with HTML tags: ", count, ' and field ', fieldName)



# Function to find all empty entries (field) for a given collection.
def find_empty_entries(collection, fieldName, collectionName, delete = False):
    print("****** Analysing for empty entries in " + collectionName + "[" + fieldName + "]" + " ******")
    allObjects = collection.find({})
    count = 0
    for object in allObjects:
        if fieldName not in object:
            print('field name ' + fieldName + ' is not an attribute on ' + collectionName + ' ' + str(object['_id']))
        if fieldName in object and not object[fieldName]:
            print("Empty Content! " + str(object['_id']))
            if delete:
                save(object)
                db.remove_entry(collection, object)
            count += 1
    print("Number of empty documents: ", count, ' and field ', fieldName)



# Function to find BOM characters from a field
def find_bom(collection, fieldName, collectionName):
    print("****** Analysing for BOM in " + collectionName + "[" + fieldName + "]" + " ******")
    allObjects = collection.find({})
    count = 0
    BOM = '\ufeff'
    for object in allObjects:
        if BOM in object[fieldName]:
            fieldValueWithoutBOM = object[fieldName].translate(
                {ord(allObjects): None for allObjects in BOM})
            print('Object: ' + str(object['_id']) + " field with BOM:  " + fieldName + ";")
            db.update_entry(collection, object, fieldName, fieldValueWithoutBOM)
            count += 1
    print("Number of documents with BOM: ", count, ' and field ', fieldName)



def save(object):
    # yet to be done
    return


if __name__ == '__main__':
    for c in fieldNameDict:
        dbHandler = db.initialize_db('literature', c)
        collectionDict[c] = dbHandler

    if len(sys.argv) == 1 or sys.argv[1] == 'view' :
        run_cleaning_tasks(False)
    elif sys.argv[1] == 'delete':
        run_cleaning_tasks(True)
    else:
        print("Illegal argument! " + str(sys.argv[1]) )
        print("Use 'delete' for deleting discrepencies,\n 'view' or no arguments for only viewing..")
