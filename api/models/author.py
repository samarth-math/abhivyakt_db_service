# -*- coding: utf-8 -*-
import api.models
from api.models.helpers import databaseHelperFunctions as db
from api.models.helpers import modelHelper as helper
from api.models.helpers.collections import collectionByType
from api.models.helpers.collections import authorCollection as collection
from bson.objectid import ObjectId
from bson.json_util import dumps
from api.globalHelpers.utilities import logger
import json

TAG = "In author.py file"


def getAllAuthors(userLimit, lastItem):
    return helper.getAllObjects(collection, lastItem, userLimit)


def getAuthorByContent(contentId, contentType):
    cursor = collection.find_one({contentType.value: ObjectId(contentId)})
    serialized = dumps(cursor)
    return json.loads(serialized)


def getAuthorByName(name):
    authorInfo, _, _ = helper.getObjectsByField(
        collection, None, 1, 'name', name)
    if authorInfo is not None and len(authorInfo) == 1:
        return authorInfo[0]
    return []

#  Expects a dictionary right now like below
#  authorInfo = {
#        "name": "कलजुगी",
#        "dohe": [ObjectId("5a589b4274ad3522fbfd2cdc"), ObjectId("5a589b4274ad3522fbfd2cdf")]
#    }
#
#  Need to make it work with a db object like below
#  {
#     '_id': {'$oid': '5b05955936178aa452dc0606'},
#     'name': 'Kabir',
#     'dohe': [{'$oid': '5a589b4274ad3522fbfd2cdc'}, {'$oid': '5a589b4274ad3522fbfd2cdf'}]
#  }


def getContentForAuthor(author, contentType):
    contentKey = contentType.value
    contentIdListToFetch = author[contentKey]
    contentColection = collectionByType[contentType]
    return helper.getObjectsByIds(contentColection, contentIdListToFetch)


def featuredAuthors():
    return helper.featured(collection, "featuredAuthors.json", "featuredAuthors")
