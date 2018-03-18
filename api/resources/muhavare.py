#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import helperfunctions as H
from bson.json_util import dumps
from bson.objectid import ObjectId

collection = H.initializeDB('literature', 'muhavare')
TAG = "In muhavare.py file"


def getMuhavareByContent(content, userLimit, lastItem):
    limit = 50
    if userLimit < limit:
        limit = userLimit

    regx = re.compile(".*" + content + ".*", re.IGNORECASE)
    if lastItem is not None:
        print(lastItem, " is not None")
        cursor = collection.find(
            {'muhavara': regx, '_id': {'$gt': ObjectId(lastItem)}}).limit(limit)
    else:
        cursor = collection.find({'muhavara': regx}).limit(limit)
    count = cursor.count()
    last_index = max(0, min(limit, count) - 1)
    print('last_index is: ', last_index)
    last_id = cursor.__getitem__(last_index).get("_id")
    print('last_index is: ', last_index, ' last_id is: ', str(last_id))
    serializedData = dumps(cursor)
    more = hasMore(count, limit, userLimit)
    print('count: ', count, ' hasMore ', more)
    return serializedData, more, str(last_id)


def getAllMuhavare(userLimit, lastItem):
    limit = 50
    if userLimit < limit:
        limit = userLimit

    if lastItem is not None:
        cursor = collection.find(
            {'_id': {'$gt': ObjectId(lastItem)}}).limit(limit)
    else:
        cursor = collection.find({}).limit(limit)
    count = cursor.count()
    last_index = max(0, min(limit, count) - 1)
    print('last_index is: ', last_index)
    if count==0:
        return None, False, str(0)
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
    char = ''
    getMuhavareByContent(char, limit, last)
    # getAllmuhavare(limit, last)
except Exception as e:
    print('Exception', e)
