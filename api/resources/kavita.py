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
        with open(os.path.join(FEATURED_FILE_PATH, "featuredKavitas.json"), "r+") as fp:
            d = json.load(fp)
            featuredKavitas = []
            for kavita in d["featuredKavitas"]:
                if 'objectId' in kavita and kavita['objectId']!="":
                    objectId = kavita['objectId']
                    featuredKavitas.append(helper.getObjectById(collection, objectId))
                else:
                    retrievedKavita = helper.getObjectByMultifieldSearch(collection, kavita)
                    kavita["objectId"] = retrievedKavita["_id"]["$oid"]
                    featuredKavitas.append(retrievedKavita)
                    fp.seek(0)
                    json.dump(d, fp, ensure_ascii=False, indent=4)
                    fp.truncate()
            fp.close()

    return featuredKavitas
