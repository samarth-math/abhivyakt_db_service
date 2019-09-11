from bson.objectid import ObjectId

from api.models.helpers.collections import getArtTypesAsStringsEnglish, getArtTypesAsStringsHindi
from api.globalHelpers.constants import Art


def validateNotNone(object):
    if object is None:
        raise TypeError("Unexpected None object")
    return object


def validateObjectId(objectId):
    validateNotNone(objectId)
    try:
        ObjectId(objectId)
        return objectId
    except Exception:
        raise TypeError("invalid ObjectId")


def validateArtType(artType: str):
    if artType in getArtTypesAsStringsEnglish():
        return artType
    if artType in getArtTypesAsStringsHindi():
        return Art(artType).name

    raise TypeError("{} is not a valid art type".format(artType))
