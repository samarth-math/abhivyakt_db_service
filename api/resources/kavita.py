# -*- coding: utf-8 -*-
from . import databaseHelperFunctions as db
from . import commonHelperFunctions as helper
import json
import os
import threading

FEATURED_FILE_PATH = os.path.join(helper.CURRENT_DIR, 'featuredContent')

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


def featured():
    lock = threading.Lock()
    with lock:
        with open(os.path.join(FEATURED_FILE_PATH, "featured.json"), "r+") as fp:
            d = json.load(fp)
            featuredPoems = []
            for poem in d["featuredPoems"]:
                if 'objectId' in poem and poem['objectId']!="":
                    objectId = poem['objectId']
                    featuredPoems.append(helper.getObjectById(collection, objectId))
                else:
                    retrievedPoem = helper.getObjectByMultifieldSearch(collection, poem)
                    poem["objectId"] = retrievedPoem["_id"]["$oid"]
                    featuredPoems.append(retrievedPoem)
                    fp.seek(0)
                    json.dump(d, fp, ensure_ascii=False, indent=4)
                    fp.truncate()
            fp.close()

    return featuredPoems
