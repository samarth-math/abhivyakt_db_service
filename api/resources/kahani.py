# -*- coding: utf-8 -*-
from . import databaseHelperFunctions as db
from . import commonHelperFunctions as helper

collection = db.initializeDB('literature', 'kahani')
TAG = "In kahani.py file"


def getKahaniByTitle(title, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'title', title)

def getKahaniByAuthor(author, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'author', author)


def getKahaniByContent(content, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'kahaniText', content)


def getAllKahani(userLimit, lastItem):
    return helper.getAllObjects(collection, lastItem, userLimit)
