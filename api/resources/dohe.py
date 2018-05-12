# -*- coding: utf-8 -*-
from . import databaseHelperFunctions as db
from . import commonHelperFunctions as helper

collection = db.initializeDB('literature', 'dohe')
TAG = "In dohe.py file"


def getDoheByAuthor(author, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'author', author)


def getDoheByContent(content, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'doha', content)

def getAllDohe(userLimit, lastItem):
    return helper.getAllObjects(collection, lastItem, userLimit)

try:
    limit = 5
    last = None
    char = 'क'
    #getAllDohe(limit, last)
except Exception as e:
    print('Exception', e)
