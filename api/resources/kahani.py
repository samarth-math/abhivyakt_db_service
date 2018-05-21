# -*- coding: utf-8 -*-
from . import databaseHelperFunctions as db
from . import commonHelperFunctions as helper
from ..routes.utilities import logger

import threading
import os
import json

collection = db.initializeDB('literature', 'kahani')
TAG = "In kahani.py file"

FEATURED_FILE_PATH = os.path.join(helper.CURRENT_DIR, 'featuredContent')


def getKahaniByTitle(title, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'title', title)


def getKahaniByAuthor(author, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'author', author)


def getKahaniByContent(content, userLimit, lastItem):
    return helper.getObjectsByField(collection, lastItem, userLimit, 'kahaniText', content)


def getAllKahani(userLimit, lastItem):
    return helper.getAllObjects(collection, lastItem, userLimit)


def featured():
    lock = threading.Lock()
    with lock:
        with open(os.path.join(FEATURED_FILE_PATH, "featuredKahanis.json"), "r+") as fp:
            d = json.load(fp)
            featuredKahanis = []
            for kahani in d["featuredKahanis"]:
                if 'objectId' in kahani and kahani['objectId'] != "":
                    objectId = kahani['objectId']
                    featuredKahanis.append(
                        helper.getObjectById(collection, objectId))
                else:
                    retrievedStory = helper.getObjectByMultifieldSearch(
                        collection, kahani)
                    if (retrievedStory is None or retrievedStory == ""):
                        logger.error("Found no kahani for " + str(kahani))
                        continue
                    kahani["objectId"] = retrievedStory["_id"]["$oid"]
                    featuredKahanis.append(retrievedStory)
                    fp.seek(0)
                    json.dump(d, fp, ensure_ascii=False, indent=4)
                    fp.truncate()
            fp.close()

    return featuredKahanis
