# -*- coding: utf-8 -*-
from .helpers import databaseHelperFunctions as db
from .helpers import modelHelper as helper


collection = db.initializeDB('literature', 'kavita')
TAG = "In Kavita.py file"


def getKavitaByTitle(title, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, "title", title)


def getKavitaByAuthor(author, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, "authorName", author)


def getKavitaByContent(content, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, "content", content)


def getAllKavita(userLimit, lastItem):
    return helper.getAllObjects(collection, lastItem, userLimit)


def featuredKavita():
    return helper.featured(collection, "featuredKavitas.json", "featuredKavitas")
