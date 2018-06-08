# -*- coding: utf-8 -*-
from .helpers import databaseHelperFunctions as db
from .helpers import modelHelper as helper
from .helpers.modelHelper import FEATURED_FILE_PATH
from api.globalHelpers.utilities import logger
import threading
import os
import json

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


def featuredKahani():
    return helper.featured(collection, "featuredKahanis.json", "featuredKahanis")
