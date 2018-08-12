# -*- coding: utf-8 -*-
from .helpers import modelHelper as helper
from api.models.helpers.collections import muhavareCollection as collection

TAG = "In muhavare.py file"


def getMuhavareByContent(content, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'muhavara', content)


def getAllMuhavare(userLimit, lastItem):
    return helper.getAllObjects(collection, lastItem, userLimit)


def featuredMuhavare():
    return helper.featured(collection, "featuredMuhavare.json", "muhavare")
