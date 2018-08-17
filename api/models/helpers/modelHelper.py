from bson.objectid import ObjectId
from bson.json_util import dumps
import re
import json
import os
import threading
from api.globalHelpers.utilities import logger
from api.globalHelpers.constants import API_LIMIT
from api.globalHelpers.constants import FEATURED_FILE_PATH
from api.globalHelpers.constants import Error
from api.globalHelpers.utilities import ValidationError
from api.globalHelpers.constants import Art
from api.models.helpers.collections import collectionByType
from api.globalHelpers.validationUtils import validateNotNone


def hasMore(count, limit):
    return True if (count > limit) else False


def getLimit(userLimit):
    userLimit = int(userLimit)
    return userLimit if (userLimit < API_LIMIT and userLimit > 0) else API_LIMIT


def getAllObjects(collection, lastItem, userLimit):
    if collection is None:
        raise ValidationError(Error.COLLECTION_NONE)
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
    if collection is None:
        raise ValidationError(Error.COLLECTION_NONE)
    cursor = collection.find_one({"_id": ObjectId(objectId)})
    serializedData = dumps(cursor)
    data = json.loads(serializedData)
    return data


def getObjectsByIds(collection, objectIds):
    if collection is None:
        raise ValidationError(Error.COLLECTION_NONE)
    cursor = collection.find({'_id': {'$in': objectIds}})
    serializedData = dumps(cursor)
    data = json.loads(serializedData)
    return data


def getObjectByMultifieldSearch(collection, fieldValueMap):
    if collection is None:
        raise ValidationError(Error.COLLECTION_NONE)
    cursor = collection.find_one(fieldValueMap)
    serializedData = dumps(cursor)
    data = json.loads(serializedData)
    return data


def getObjectsByField(collection, lastItem, userLimit, fieldName, searchTerm, regx=None):
    if collection is None:
        raise ValidationError(Error.COLLECTION_NONE)

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


def rewriteFileWithJsonObject(jsonObject, filePointer):
    filePointer.seek(0)
    json.dump(jsonObject, filePointer, ensure_ascii=False, indent=4)
    filePointer.truncate()


def featured(collection, fileName, artType):
    lock = threading.Lock()
    with lock:
        with open(os.path.join(FEATURED_FILE_PATH, fileName), "r+") as fp:
            jsonDataObject = json.load(fp)
            featuredObjects = []
            retrievedArtItem = {}
            for item in jsonDataObject[artType]:
                if 'objectId' in item and item['objectId'] != "":
                    objectId = item['objectId']
                    retrievedArtItem = getObjectById(collection, objectId)
                else:
                    retrievedArtItem = getObjectByMultifieldSearch(
                        collection, item)
                    validateNotNone(retrievedArtItem)
                    item["objectId"] = retrievedArtItem["_id"]["$oid"]
                    rewriteFileWithJsonObject(jsonDataObject, fp)
                retrievedArtItem["type"] = Art[artType].value
                featuredObjects.append(retrievedArtItem)
    return featuredObjects


def getObjectsByStartCharacter(collection, lastItem, userLimit, fieldName,
                               startCharacter, regx=None):
    if collection is None:
        raise ValidationError(Error.COLLECTION_NONE)

    limit = getLimit(userLimit)
    if regx is None:
        regx = re.compile('^' + startCharacter + '.*', re.UNICODE)

    if lastItem is not None:
        cursor = collection.find(
            {fieldName: regx, '_id': {'$gt': ObjectId(lastItem)}}).limit(limit)
    else:
        cursor = collection.find({fieldName: regx}).limit(limit)
        # The count() method is probably deprecated, might need to use
        # count_documents in future check this link:
        # http://api.mongodb.com/python/current/changelog.html
        count = cursor.count()
        if count == 0:
            return None, False, str(0)
        last_index = max(0, min(limit, count) - 1)
        last_id = cursor.__getitem__(last_index).get("_id")
        serializedData = dumps(cursor)
        more = hasMore(count, limit)
        data = json.loads(serializedData)
        return data, more, str(last_id)
