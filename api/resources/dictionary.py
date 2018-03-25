#!/usr/bin/env python
# -*- coding: utf-8 -*-
import databaseHelperFunctions as db
import commonHelperFunctions as helper
collection = db.initializeDB('literature', 'dictionary')
TAG = "In dictionary.py file"


def getWord(content, userLimit, lastItem):
    helper.getObjectsByField(collection, lastItem, userLimit, 'word', content)


def getAllWords(userLimit, lastItem):
    return helper.getAllObjects(collection, lastItem, userLimit)


try:
    limit = 5
    last = None
    char = ''
    # getWord(char, limit, last)
    # getAlldictionary(limit, last)
except Exception as e:
    print('Exception', e)
