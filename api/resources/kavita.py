#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import helperfunctions as H
from bson import Binary, Code
from bson.json_util import dumps

collection = H.initializeDB('literature', 'kavita')
TAG = "In Kavita.py file"

def getKavitaByTitle(title, userLimit, offset, lastItem):
    limit = 50
    if userLimit < limit:
        limit = userLimit
    regx = re.compile("^" + title, re.IGNORECASE)
    if lastItem is not None:
        cursor = collection.find(
            {'title': regx, '_id': {'$gt': lastItem}}).limit(limit)
    else:
        cursor = collection.find({'title': regx}).limit(limit)

    last_id = None
    last_index = max(0, min(limit,cursor.count()) - 1)
    for r in range(0, min(limit, cursor.count())):
        last_id = cursor.__getitem__(r).get("_id")
        print('last id: ' , last_id)

    #last_id = cursor.__getitem__(last_index).get("_id")
    print(TAG, ' last_id is: ', str(last_id))
    print(TAG, ' data is', cursor)
    serializedData = dumps(cursor)
    print(TAG, ' serialize ', serializedData)
    print(TAG, ' ', type(serializedData))
    count = cursor.count()
    if userLimit < limit:
        more = False
    else:
        more = hasMore(count, limit, offset)
    print("Cursor count: ", count)
    return serializedData, more, str(last_id)


def getKavitaByAuthor(author, userLimit, offset, lastItem):
    limit = 50
    regx = re.compile("^" + author, re.IGNORECASE)
    ret = collection.find({"authorName": regx}).limit(limit)
    last_id = ret[-1]['_id']
    if lastItem is not None:
        query = collection.find(
            {'title': regx, '_id': {'$gt': lastItem}}).limit(limit)
    else:
        query = collection.find({'title': regx})
    count = query.count()
    if userLimit < limit:
        more = False
    else:
        more = hasMore(count, userLimit, offset)
    print("Ret: ", ret.count())
    return ret, more, last_id


def getKavitaByContent(content, userLimit, offset, lastItem):
    limit = 50
    regx = re.compile("^" + content, re.IGNORECASE).limit(limit)
    ret = collection.find({"content": regx})
    last_id = ret[-1]['_id']
    if lastItem is not None:
        query = collection.find(
            {'title': regx, '_id': {'$gt': lastItem}}).limit(limit)
    else:
        query = collection.find({'title': regx})
    count = query.count()
    count = query.count()
    if userLimit < limit:
        more = False
    else:
        more = hasMore(count, offset, limit)
    print("Ret: ", ret.count())
    return ret, more, last_id


def hasMore(count, limit, offset):
    if count > (limit * offset + limit):
        return True
    else:
        return False

try:
    limit=50
    last = None
    offset = 0
    char = 'क'
    getKavitaByTitle(char, limit, offset, last)
except Exception as e:
    print('Exception', e)
    limit = 10
