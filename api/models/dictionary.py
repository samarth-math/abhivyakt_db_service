# -*- coding: utf-8 -*-
from .helpers import databaseHelperFunctions as db
from .helpers import modelHelper as helper

collection = db.initializeDB('literature', 'dictionary')
TAG = "In dictionary.py file"


def getWord(content, userLimit=-1, lastItem=None):
    return helper.getObjectsByFieldExactSearch(collection, lastItem, userLimit, 'key', content)


def getAllWords(userLimit=-1, lastItem=None):
    return helper.getAllObjects(collection, lastItem, userLimit)
