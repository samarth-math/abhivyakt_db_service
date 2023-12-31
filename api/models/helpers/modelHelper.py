from bson.objectid import ObjectId
from bson.json_util import dumps
import re
import json
import os
import threading
import gridfs
from api.globalHelpers.utilities import logger
from api.globalHelpers.constants import API_LIMIT
from api.globalHelpers.constants import FEATURED_FILE_PATH
from api.globalHelpers.constants import Error
from api.globalHelpers.utilities import ValidationError
from api.globalHelpers.constants import Art
from api.globalHelpers.validationUtils import validateNotNone
from api.globalHelpers.validationUtils import validateObjectId
from api.models.helpers.databaseHelperFunctions import getDBHandler
from bson import errors


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
    validateObjectId(objectId)
    cursor = collection.find_one({"_id": ObjectId(objectId)})
    serializedData = dumps(cursor)
    data = json.loads(serializedData)
    return data


def getObjectsByIds(collection, objectIds: list, userLimit, lastItem):  # potential bug on ordering
    if collection is None:
        raise ValidationError(Error.COLLECTION_NONE)

    limit = getLimit(userLimit)
    modifiedObjectIds = list(map(lambda x: ObjectId(x), objectIds))
    if lastItem is not None:
        cursor = collection.find({
            '$and': [
                {'_id': {'$in': modifiedObjectIds}},
                {'_id': {'$gt': ObjectId(lastItem)}}
            ]
        }).limit(limit)
    else:
        cursor = collection.find({
            '_id': {'$in': modifiedObjectIds}
        }).limit(limit)
    count = cursor.count()
    if count == 0:
        return None, False, str(0)
    lastIndex = max(0, min(limit, count) - 1)
    lastId = cursor.__getitem__(lastIndex).get("_id")
    serializedData = dumps(cursor)
    more = hasMore(count, limit)
    data = json.loads(serializedData, encoding='utf-8')
    return data, more, str(lastId)


def getObjectByMultifieldExactSearch(collection, fieldValueMap):
    if collection is None:
        raise ValidationError(Error.COLLECTION_NONE)
    cursor = collection.find_one(fieldValueMap)
    serializedData = dumps(cursor)
    data = json.loads(serializedData)
    return data


def getObjectsByField(collection, lastItem, userLimit, fieldName, searchTerm):
    regx = re.compile(".*" + searchTerm + ".*", re.IGNORECASE)
    return getObjectsByRegex(collection, lastItem, userLimit, fieldName, regx)


def getObjectsByRegex(collection, lastItem, userLimit, fieldName, regx):
    if collection is None:
        raise ValidationError(Error.COLLECTION_NONE)

    limit = getLimit(userLimit)
    if lastItem is not None:
        cursor = collection.find(
            {fieldName: regx, '_id': {'$gt': ObjectId(lastItem)}}).limit(limit)
    else:
        cursor = collection.find({fieldName: regx}).limit(limit)
    # The count() method is probably deprecated, might need to use
    # count_documents in future check this link:
    #  # http://api.mongodb.com/python/current/changelog.html
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
    return getObjectsByRegex(collection, lastItem, userLimit, fieldName, regx)


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
                    retrievedArtItem = getObjectByMultifieldExactSearch(
                        collection, item)
                    validateNotNone(retrievedArtItem)
                    item["objectId"] = retrievedArtItem["_id"]["$oid"]
                    rewriteFileWithJsonObject(jsonDataObject, fp)
                retrievedArtItem["type"] = Art[artType].value
                featuredObjects.append(retrievedArtItem)
    return featuredObjects


def getObjectsByStartCharacter(collection, lastItem, userLimit, fieldName,
                               startCharacter, regx=None):
    regx = re.compile('^' + startCharacter + '.*', re.UNICODE)
    return getObjectsByRegex(collection, lastItem, userLimit, fieldName, regx)


def getFileById(fid):
    """[Returns a file which has been stored using GridFS convention.]

    Arguments:
        db {[pymongo.database.Database]} -- [database from where file is to be
                                             retrieved]
        fid {[bson.objectid.ObjectId]} -- [file id which needs to be fetched
                                           from db]

    Returns:
        [<class 'bytes'>] -- [Returns file in form of bytes]
    """
    if fid is None:
        raise ValidationError(Error.UNEXPECTED_NULL)
    dbHandler = getDBHandler('literature')
    fs = gridfs.GridFS(dbHandler)
    logger.info('file id:' + fid)
    try:
        fid = ObjectId(fid)
        fileOut = fs.find_one({'_id': fid})
        if fileOut is None:
            return None
        fileObj = fileOut.read()
        return fileObj
    except errors.InvalidId:
        return None
