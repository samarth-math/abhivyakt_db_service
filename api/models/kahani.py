# -*- coding: utf-8 -*-
from api.models.helpers import modelHelper as helper
from api.models.helpers.collections import kahaniCollection as collection

TAG = "In kahani.py file"


def getKahaniByTitle(title, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'title', title)


def getKahaniByTitlePrefix(userLimit, lastItem, startCharacter):
    return helper.getObjectsByStartCharacter(collection, lastItem, userLimit,
                                             'title', startCharacter)


def getKahaniByAuthor(author, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'author', author)


def getKahaniByContent(content, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'kahaniText', content)


def getAllKahani(userLimit, lastItem):
    return helper.getAllObjects(collection, lastItem, userLimit)


def featuredKahani():
    return helper.featured(collection, "featuredKahanis.json", "kahani")


def getKahaniById(objectId):
    return helper.getObjectById(collection, objectId)
