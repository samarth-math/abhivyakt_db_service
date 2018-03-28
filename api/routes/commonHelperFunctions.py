from flask import jsonify
import json

DATABASE_END = "Oops, looks like we are out of content"


def validateNotNull(object):
    if object is None:  # TODO throw exception
        print (object + " is None")


def createReturnJSONResponse(data, hasMore, lastItem, nextItemURL, fieldName=None, fieldValue=None):
    if data is None:
        return jsonify(
            error=DATABASE_END,
            hasMore=False
        )

    if hasMore is False:
        return jsonify(
            content=data,
            hasMore=False
        )
    validateNotNull(lastItem)
    if fieldName is not None:
        nextItemURL = nextItemURL + fieldName + fieldValue + '&nextItem=' + lastItem
    else:
        nextItemURL = nextItemURL + '&nextItem=' + lastItem
    print("returning here")
    return jsonify(
        content=data,
        hasMore=True,
        nextItem=nextItemURL
    )


def createReturnObject(data, hasMore, lastItem, nextItemURL, fieldName=None, fieldValue=None):
    if data is None:
        obj = {'content': "{}", 'error': DATABASE_END, 'hasMore': False}
        return obj

    if hasMore is False:
        obj = {'content': data, 'error':"", 'hasMore': False}
        return obj

    validateNotNull(lastItem)
    if fieldName is not None:
        nextItemURL = nextItemURL + fieldName + fieldValue + '&nextItem=' + lastItem
    else:
        nextItemURL = nextItemURL + '&nextItem=' + lastItem
    obj = {'content': data, 'hasMore': True, 'nextItem': nextItemURL}
    return obj
