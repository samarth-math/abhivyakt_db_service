from bson.objectid import ObjectId


def validateNotNone(object):
    if object is None:
        raise TypeError("Unexpected None object")

def validateObjectId(objectId):
    validateNotNone(objectId)
    try:
        ObjectId(objectId)
    except:
        raise TypeError ("invalid ObjectId")
