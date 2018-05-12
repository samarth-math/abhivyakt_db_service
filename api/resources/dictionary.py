# -*- coding: utf-8 -*-
from . import databaseHelperFunctions as db
from . import commonHelperFunctions as helper
collection = db.initializeDB('literature', 'dictionary')
TAG = "In dictionary.py file"


def getWord(content, userLimit=-1, lastItem=None):
    return helper.getObjectsByFieldExactSearch(collection, lastItem, userLimit, 'key', content)


def getAllWords(userLimit=-1, lastItem=None):
    return helper.getAllObjects(collection, lastItem, userLimit)


try:
    limit = 5
    last = None
    char = ''
    # getWord(char, limit, last)
    # getAlldictionary(limit, last)
except Exception as e:
    print('Exeption', e)
