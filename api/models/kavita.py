# -*- coding: utf-8 -*-
from api.models.helpers.collections import kavitaCollection as collection
from api.models.helpers import modelHelper as helper
TAG = "In Kavita.py file"


def getKavitaByTitle(title, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, "title", title)


def getKavitaByTitlePrefix(userLimit, lastItem, startCharacter):
    return helper.getObjectsByStartCharacter(collection, lastItem, userLimit,
                                             'title', startCharacter)


def getKavitaByAuthor(author, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, "authorName", author)


def getKavitaByContent(content, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, "content", content)


def getAllKavita(userLimit, lastItem):
    return helper.getAllObjects(collection, lastItem, userLimit)


def featuredKavita():
    return helper.featured(collection, "featuredKavitas.json", "kavita")


def getKavitaById(objectId):
    return helper.getObjectById(collection, objectId)