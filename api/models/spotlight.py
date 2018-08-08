# -*- coding: utf-8 -*-
import json
import os
import threading
from api.globalHelpers.constants import FEATURED_FILE_PATH
from api.globalHelpers.constants import Art
from api.globalHelpers.validationUtils import validateNotNone
from api.models.helpers.collections import collectionByType
from api.models.helpers.modelHelper import getObjectById
from api.models.helpers.modelHelper import getObjectByMultifieldSearch

FILE_NAME ="spotlightArts.json"


def spotlight():
    artEnums = [Art.kavita, Art.kahani]
    lock = threading.Lock()
    with lock:
        with open(os.path.join(FEATURED_FILE_PATH, FILE_NAME), "r+") as fp:
            jsonDataFromFile = json.load(fp)
            featuredObjects = []
            retrievedArtItem = {}
            for artEnum in artEnums:
                artType = artEnum.name
                collection = collectionByType[artEnum]
                if artType in jsonDataFromFile:
                    for artItem in jsonDataFromFile[artType]:
                        if 'objectId' in artItem and artItem['objectId'] != "":
                            objectId = artItem['objectId']
                            retrievedArtItem = getObjectById(collection, objectId)
                        else:
                            retrievedArtItem = getObjectByMultifieldSearch(
                                collection, artItem)
                            validateNotNone(retrievedArtItem)
                            artItem["objectId"] = retrievedArtItem["_id"]["$oid"]
                            rewriteFileWithJsonObject(jsonDataFromFile, fp)
                        retrievedArtItem["type"] = artEnum.value
                        featuredObjects.append(retrievedArtItem)
    return featuredObjects

def rewriteFileWithJsonObject(jsonObject, filePointer):
    filePointer.seek(0)
    json.dump(jsonObject, filePointer, ensure_ascii=False, indent=4)
    filePointer.truncate()