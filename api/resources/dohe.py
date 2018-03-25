#!/usr/bin/env python
# -*- coding: utf-8 -*-
import databaseHelperFunctions as db
import commonHelperFunctions as helper

collection = db.initializeDB('literature', 'dohe')
TAG = "In dohe.py file"


def getDoheByAuthor(author, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'author', author)


def getDoheByContent(content, userLimit, lastItem):
    helper.getObjectsByField(collection, lastItem, userLimit, 'doha', content)

def getAllDohe(userLimit, lastItem):
    return helper.getAllObjects(collection, lastItem, userLimit)

try:
    limit = 5
    last = None
    char = 'क'
    #getAllDohe(limit, last)
except Exception as e:
    print('Exception', e)
