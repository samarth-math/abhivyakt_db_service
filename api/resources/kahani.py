#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import helperfunctions as H
from bson.json_util import dumps
from bson.objectid import ObjectId

collection = H.initializeDB('literature', 'kahani')
TAG = "In kahani.py file"


def getKahaniByTitle(author, userLimit, lastItem):
    limit = 50
    if userLimit < limit:
        limit = userLimit
    regx = re.compile(".*" + author + ".*", re.IGNORECASE)
    if lastItem is not None:
        print(lastItem, " is not None")
        cursor = collection.find(
            {'title': regx, '_id': {'$gt': ObjectId(lastItem)}}).limit(limit)
    else:
        cursor = collection.find({'title': regx}).limit(limit)
    count = cursor.count()
    last_index = max(0, min(limit, count) - 1)
    print('last_index is: ', last_index)
    last_id = cursor.__getitem__(last_index).get("_id")
    print('last_index is: ', last_index, ' last_id is: ', str(last_id))
    serializedData = dumps(cursor)
    more = hasMore(count, limit, userLimit)
    print('count: ', count, ' hasMore ', more)
    return serializedData, more, str(last_id)



def getKahaniByAuthor(author, userLimit, lastItem):
    limit = 50
    if userLimit < limit:
        limit = userLimit
    regx = re.compile(".*" + author + ".*", re.IGNORECASE)
    if lastItem is not None:
        print(lastItem, " is not None")
        cursor = collection.find(
            {'author': regx, '_id': {'$gt': ObjectId(lastItem)}}).limit(limit)
    else:
        cursor = collection.find({'author': regx}).limit(limit)
    count = cursor.count()
    last_index = max(0, min(limit, count) - 1)
    print('last_index is: ', last_index)
    last_id = cursor.__getitem__(last_index).get("_id")
    print('last_index is: ', last_index, ' last_id is: ', str(last_id))
    serializedData = dumps(cursor)
    more = hasMore(count, limit, userLimit)
    print('count: ', count, ' hasMore ', more)
    return serializedData, more, str(last_id)


def getKahaniByContent(content, userLimit, lastItem):
    limit = 50
    if userLimit < limit:
        limit = userLimit

    regx = re.compile(".*" + content + ".*", re.IGNORECASE)
    if lastItem is not None:
        print(lastItem, " is not None")
        cursor = collection.find(
            {'kahaniText': regx, '_id': {'$gt': ObjectId(lastItem)}}).limit(limit)
    else:
        cursor = collection.find({'kahaniText': regx}).limit(limit)
    count = cursor.count()
    last_index = max(0, min(limit, count) - 1)
    print('last_index is: ', last_index)
    last_id = cursor.__getitem__(last_index).get("_id")
    print('last_index is: ', last_index, ' last_id is: ', str(last_id))
    serializedData = dumps(cursor)
    more = hasMore(count, limit, userLimit)
    print('count: ', count, ' hasMore ', more)
    return serializedData, more, str(last_id)


def getAllKahani(userLimit, lastItem):
    limit = 50
    if userLimit < limit:
        limit = userLimit

    if lastItem is not None:
        cursor = collection.find(
            {'_id': {'$gt': ObjectId(lastItem)}}).limit(limit)
    else:
        if collection is None:
            print('Collection is None')
        cursor = collection.find({}).limit(limit)
    count = cursor.count()
    last_index = max(0, min(limit, count) - 1)
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
    char = 'क'
    # getKahaniByTitle(char, limit, last)
except Exception as e:
    print('Exception', e)
