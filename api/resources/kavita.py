#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import helperfunctions as H
from bson import Binary, Code
from bson.json_util import dumps
from bson.objectid import ObjectId

collection = H.initializeDB('literature', 'kavita')
TAG = "In Kavita.py file"


def getKavitaByTitle(title, userLimit, lastItem):
    limit = 50
    if userLimit < limit:
        limit = userLimit
    regx = re.compile(".*" + title + ".*", re.IGNORECASE)
    if lastItem is not None:
        print(lastItem, " is not None")
        cursor = collection.find(
            {'title': regx, '_id': {'$gt': ObjectId(lastItem)}}).limit(limit)
    else:
        cursor = collection.find({'title': regx}).limit(limit)
    print(cursor.count())
    last_id = None
    last_index = max(0, min(limit, cursor.count()) - 1)
    for r in range(0, min(limit, cursor.count())):
        last_id = cursor.__getitem__(r).get("_id")
        print('last id: ', last_id)

    # last_id = cursor.__getitem__(last_index).get("_id")
    print(TAG, ' last_id is: ', str(last_id))
    print(TAG, ' data is', cursor)
    serializedData = dumps(cursor)
    print(TAG, ' serialize ', serializedData)
    print(TAG, ' ', type(serializedData))
    count = cursor.count()
    if userLimit < limit:
        more = False
    else:
        more = hasMore(count, limit, userLimit)
    print("Cursor count: ", count)
    return serializedData, more, str(last_id)


def getKavitaByAuthor(author, userLimit, lastItem):
    limit = 50
    if userLimit < limit:
        limit = userLimit
    regx = re.compile(".*" + author + ".*", re.IGNORECASE)
    if lastItem is not None:
        print(lastItem, " is not None")
        cursor = collection.find(
            {'authorName': regx, '_id': {'$gt': ObjectId(lastItem)}}).limit(limit)
    else:
        cursor = collection.find({'authorName': regx}).limit(limit)
    count = cursor.count()
    last_index = max(0, min(limit, count)- 1)
    print('last_index is: ', last_index)
    last_id = cursor.__getitem__(last_index).get("_id")
    print('last_index is: ', last_index, ' last_id is: ', str(last_id))
    serializedData = dumps(cursor)
    more = hasMore(count, limit, userLimit)
    print('count: ', count, ' hasMore ', more)
    return serializedData, more, str(last_id)


def getKavitaByContent(content, userLimit, lastItem):
    limit = 50
    if userLimit < limit:
        limit = userLimit

    regx = re.compile(".*" + content + ".*", re.IGNORECASE)
    if lastItem is not None:
        print(lastItem, " is not None")
        cursor = collection.find(
            {'content': regx, '_id': {'$gt': ObjectId(lastItem)}}).limit(limit)
    else:
        cursor = collection.find({'content': regx}).limit(limit)
    count = cursor.count()
    last_index = max(0, min(limit, count)- 1)
    print('last_index is: ', last_index)
    last_id = cursor.__getitem__(last_index).get("_id")
    print('last_index is: ', last_index, ' last_id is: ', str(last_id))
    serializedData = dumps(cursor)
    more = hasMore(count, limit, userLimit)
    print('count: ', count, ' hasMore ', more)
    return serializedData, more, str(last_id)


def getAllKavita(userLimit, lastItem):
    limit = 50
    if userLimit < limit:
        limit = userLimit

    if lastItem is not None:
        cursor = collection.find({'_id': {'$gt': ObjectId(lastItem)}}).limit(limit)
    else:
        cursor = collection.find({}).limit(limit)
    count = cursor.count()
    last_index = max(0, min(limit, count)- 1)
    print('last_index is: ', last_index)
    last_id = cursor.__getitem__(last_index).get("_id")
    print('last_index is: ', last_index, ' last_id is: ', str(last_id))
    serializedData = dumps(cursor)
    more = hasMore(count, limit, userLimit)
    print('count: ', count, ' hasMore ', more)
    return serializedData, more, str(last_id)


def hasMore(count, limit, userLimit):
    if count > userLimit:
        return True
    else:
        return False


try:
    limit = 5
    last = None
    # char = 'क'
    # getAllKavita(limit, last)
except Exception as e:
    print('Exception', e)
