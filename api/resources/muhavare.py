#!/usr/bin/env python
# -*- coding: utf-8 -*-
import databaseHelperFunctions as db
import commonHelperFunctions as helper

collection = db.initializeDB('literature', 'muhavare')
TAG = "In muhavare.py file"

def getMuhavareByContent(content, userLimit, lastItem):
    helper.getObjectsByField(collection, lastItem, userLimit, 'muhavara', content)


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
