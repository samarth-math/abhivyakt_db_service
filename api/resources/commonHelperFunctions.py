from bson.objectid import ObjectId
from bson.json_util import dumps
import re


API_LIMIT = 50

def hasMore(count, limit):
    if count > limit:
        return True
    else:
        return False

def getLimit(userLimit):
    return userLimit if (userLimit<API_LIMIT) else API_LIMIT

def getAllObjects(collection, lastItem, userLimit):
    if collection is None:#TODO throw exception
        print('Collection is None')

    limit = getLimit(userLimit)
    if lastItem is not None:
        cursor = collection.find(
            {'_id': {'$gt': ObjectId(lastItem)}}).limit(limit)
    else:
        cursor = collection.find({}).limit(limit)
    count = cursor.count()
    last_index = max(0, min(limit, count) - 1)
    print('last_index is: ', last_index)
    last_id = cursor.__getitem__(last_index).get("_id")
    print('last_index is: ', last_index, ' last_id is: ', str(last_id))
    serializedData = dumps(cursor)
    more = hasMore(count, limit)
    print('count: ', count, ' userLimit: ', userLimit, ' hasMore ', more)
    return serializedData, more, str(last_id)


def getObjectsByField(collection, lastItem, userLimit, fieldName, searchTerm,):
    if collection is None:#TODO throw exception
        print('Collection is None')

    limit = getLimit(userLimit)
    regx = re.compile(".*" + searchTerm + ".*", re.IGNORECASE)
    if lastItem is not None:
        print(lastItem, " is not None")
        cursor = collection.find(
            {fieldName: regx, '_id': {'$gt': ObjectId(lastItem)}}).limit(limit)
    else:
        cursor = collection.find({fieldName: regx}).limit(limit)
    count = cursor.count()
    last_index = max(0, min(limit, count) - 1)
    print('last_index is: ', last_index)
    if count == 0:
        return None, False, str(0)
    last_id = cursor.__getitem__(last_index).get("_id")
    print('last_index is: ', last_index, ' last_id is: ', str(last_id))
    serializedData = dumps(cursor)
    more = hasMore(count, limit)
    print('count: ', count, ' hasMore ', more)
    return serializedData, more, str(last_id)

