from bson.objectid import ObjectId
from bson.json_util import dumps
import re
import json
import os

API_LIMIT = 50
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))   # refers to application_top


def hasMore(count, limit):
    return True if (count > limit) else False


def getLimit(userLimit):
    userLimit = int(userLimit)
    return userLimit if (userLimit < API_LIMIT and userLimit > 0) else API_LIMIT


def getAllObjects(collection, lastItem, userLimit):
    if collection is None:  # TODO throw exception
        print('Collection is None')

    limit = getLimit(userLimit)
    if lastItem is not None:
        cursor = collection.find(
            {'_id': {'$gt': ObjectId(lastItem)}}).limit(limit)
    else:
        cursor = collection.find({}).limit(limit)
    count = cursor.count()
    if count == 0:
        return None, False, str(0)
    last_index = max(0, min(limit, count) - 1)
    last_id = cursor.__getitem__(last_index).get("_id")
    serializedData = dumps(cursor)
    more = hasMore(count, limit)
    data = json.loads(serializedData)
    return data, more, str(last_id)

def getObjectById(collection, objectId):
    if collection is None:  # TODO throw exception
        print('Collection is None')
    cursor = collection.find_one({"_id":ObjectId(objectId)})
    serializedData = dumps(cursor)
    data = json.loads(serializedData)
    return data

def getObjectByMultifieldSearch(collection, fieldValueMap): 
    if collection is None:  # TODO throw exception
        print('Collection is None')
    cursor = collection.find_one(fieldValueMap)
    serializedData = dumps(cursor)
    data = json.loads(serializedData)
    return data


def getObjectsByField(collection, lastItem, userLimit, fieldName, searchTerm, regx=None):
    if collection is None:  # TODO throw exception
        print('Collection is None')

    limit = getLimit(userLimit)
    if regx is None:
        regx = re.compile(".*" + searchTerm + ".*", re.IGNORECASE)
    if lastItem is not None:
        cursor = collection.find(
            {fieldName: regx, '_id': {'$gt': ObjectId(lastItem)}}).limit(limit)
    else:
        cursor = collection.find({fieldName: regx}).limit(limit)
    count = cursor.count()
    if count == 0:
        return None, False, str(0)
    last_index = max(0, min(limit, count) - 1)
    last_id = cursor.__getitem__(last_index).get("_id")
    serializedData = dumps(cursor)
    more = hasMore(count, limit)
    data = json.loads(serializedData)
    return data, more, str(last_id)

def getObjectsByFieldExactSearch(collection, lastItem, userLimit, fieldName, searchTerm):
    regx = re.compile(searchTerm, re.IGNORECASE)
    return getObjectsByField(collection, lastItem, userLimit, fieldName, searchTerm, regx)
