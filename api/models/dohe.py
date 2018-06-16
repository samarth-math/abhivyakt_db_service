# -*- coding: utf-8 -*-
from api.models.helpers import modelHelper as helper
from api.models.helpers.collections import doheCollection as collection

TAG = "In dohe.py file"


def getDoheByAuthor(author, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'author', author)


def getDoheByContent(content, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'doha', content)


def getAllDohe(userLimit, lastItem):
    return helper.getAllObjects(collection, lastItem, userLimit)


def featuredDohe():
    return helper.featured(collection, "featuredDohe.json", "featuredDohe")
