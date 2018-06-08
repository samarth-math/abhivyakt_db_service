# -*- coding: utf-8 -*-
from .helpers import databaseHelperFunctions as db
from .helpers import modelHelper as helper

collection = db.initializeDB('literature', 'muhavare')
TAG = "In muhavare.py file"


def getMuhavareByContent(content, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'muhavara', content)


def getAllMuhavare(userLimit, lastItem):
    return helper.getAllObjects(collection, lastItem, userLimit)


def featuredMuhavare():
    return helper.featured(collection, "featuredMuhavare.json", "featuredMuhavare")
