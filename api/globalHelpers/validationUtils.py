from bson.objectid import ObjectId
from api.models.helpers.collections import getArtTypesAsStrings


def validateNotNone(object):
    if object is None:
        raise TypeError("Unexpected None object")


def validateObjectId(objectId):
    validateNotNone(objectId)
    try:
        ObjectId(objectId)
    except:
        raise TypeError("invalid ObjectId")


def validateArtType(artType: str):
    if artType not in getArtTypesAsStrings():
        raise TypeError("{} is not a valid art type".format(artType))
