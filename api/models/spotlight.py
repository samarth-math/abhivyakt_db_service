import json
import os
import threading
from api.globalHelpers.constants import FEATURED_FILE_PATH
from api.globalHelpers.constants import Art
from api.models.helpers.collections import collectionByType
from api.models.helpers.modelHelper import getObjectById
from api.models.helpers.modelHelper import getObjectByMultifieldSearch

FILE_NAME ="spotlightArts.json"


def spotlight():
    objectNames = [Art.kavita, Art.kahani]
    lock = threading.Lock()
    with lock:
        with open(os.path.join(FEATURED_FILE_PATH, FILE_NAME), "r+") as fp:
            d = json.load(fp)
            featuredObjects = []
            retrievedItem = {}
            for objectEnum in objectNames:
                objectName = objectEnum.value
                collection = collectionByType[objectEnum]
                if objectName in d:
                    for item in d[objectName]:
                        if 'objectId' in item and item['objectId'] != "":
                            objectId = item['objectId']
                            retrievedItem = getObjectById(collection, objectId) 
                        else:
                            retrievedItem = getObjectByMultifieldSearch(
                                collection, item)
                            try:
                                item["objectId"] = retrievedItem["_id"]["$oid"]
                                fp.seek(0)
                                json.dump(d, fp, ensure_ascii=False, indent=4)
                                fp.truncate()
                            except:
                                if retrievedItem is None:
                                    raise ValueError("Did not find the object you specified in the featured file spotlightArts.json")
                                else:
                                    raise
                        retrievedItem["type"] = objectName
                        featuredObjects.append(retrievedItem)
            fp.close()
    return featuredObjects
