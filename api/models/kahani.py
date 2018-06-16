# -*- coding: utf-8 -*-
from api.models.helpers import modelHelper as helper
from api.globalHelpers.utilities import logger
from api.models.helpers.collections import kahaniCollection as collection

import threading
import os
import json

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
