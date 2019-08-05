# -*- coding: utf-8 -*-
from api.models.helpers import modelHelper as helper
from api.models.helpers.collections import collectionByTypeString
from api.models.helpers.collections import rachnakarCollection as collection
from bson.objectid import ObjectId
from bson.json_util import dumps
import api.globalHelpers.validationUtils as validationUtils
import json


def getAllRachnakar(userLimit, lastItem):
    return helper.getAllObjects(collection, lastItem, userLimit)


def getRachnakarByContent(contentId, contentType):
    cursor = collection.find_one({contentType.value: ObjectId(contentId)})
    serialized = dumps(cursor)
    return json.loads(serialized)


def getRachnakarByName(name):
    rachnakarInfo, _, _ = helper.getObjectsByField(
        collection, None, 1, 'name', name)
    if rachnakarInfo is not None and len(rachnakarInfo) == 1:
        return rachnakarInfo[0]
    return []


def getRachnakarById(objectId):
    return helper.getObjectById(collection, objectId)


def getContentForRachnakarId(userLimit, lastItem, rachnakarId: str, artType: str):
    validationUtils.validateObjectId(rachnakarId)
    validationUtils.validateArtType(artType)
    artList = extractArtIdsFromRachnakar(rachnakarId, artType)
    response = helper.getObjectsByIds(collectionByTypeString(artType), artList, userLimit, lastItem)
    return response


def extractArtIdsFromRachnakar(rachnakarId: str, artType: str):
    rachnakar = getRachnakarById(rachnakarId)
    artIdList = []
    if artType in rachnakar.keys():
        for id in rachnakar[artType]:
            artIdList.append(id['$oid'])
    return artIdList


def featuredRachnakar():
    return helper.featured(collection, "featuredRachnakar.json", "rachnakar")


def homePageRachnakar():
    return helper.featured(collection, "homePageRachnakar.json", "rachnakar")


def getRachnakarByNamePrefix(userLimit, lastItem, startCharacter):
    return helper.getObjectsByStartCharacter(collection, lastItem, userLimit,
                                             'name', startCharacter)
