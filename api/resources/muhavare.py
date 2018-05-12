# -*- coding: utf-8 -*-
from . import databaseHelperFunctions as db
from . import commonHelperFunctions as helper

collection = db.initializeDB('literature', 'muhavare')
TAG = "In muhavare.py file"

def getMuhavareByContent(content, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'muhavara', content)


def getAllMuhavare(userLimit, lastItem):
    return helper.getAllObjects(collection, lastItem, userLimit)


try:
    limit = 5
    last = None
    char = ''
    getMuhavareByContent(char, limit, last)
    # getAllmuhavare(limit, last)
except Exception as e:
    print('Exception', e)
