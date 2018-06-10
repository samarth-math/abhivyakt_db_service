from flask import jsonify
import json
from api.globalHelpers.utilities import logger
from api.globalHelpers.constants import END_OF_CONTENT


def validateNotNull(object):
    if object is None:
        raise ("ValidationERROR : Unexpected null object found")


def getParams(request):
    # sample server side logging..
    logger.info("Making request " + request.url + "..")
    nextItem = request.args.get('nextItem')
    title = request.args.get('title')
    author = request.args.get('author')
    content = request.args.get('content')
    limit = request.args.get('limit')
    if limit is None:
        limit = -1
    return limit, nextItem, content, author, title


def createResponse(data, hasMore, lastItem, nextItemURL='', fieldName=None, fieldValue=None, isJson=False):
    if isJson:
        return createJSONResponse(data, hasMore, lastItem, nextItemURL, fieldName, fieldValue)
    else:
        return createResponseObjectForTemplate(data, hasMore, lastItem, nextItemURL, fieldName, fieldValue)


def createJSONResponse(data, hasMore, lastItem, nextItemURL, fieldName, fieldValue):
    if data is None:
        return jsonify(
            error=END_OF_CONTENT,
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
    return jsonify(
        content=data,
        hasMore=True,
        nextItem=nextItemURL
    )


def createResponseObjectForTemplate(data, hasMore, lastItem, nextItemURL, fieldName=None, fieldValue=None):
    if data is None:
        obj = {'content': "{}", 'error': END_OF_CONTENT, 'hasMore': False}
        return obj

    if hasMore is False:
        obj = {'content': data, 'error': "", 'hasMore': False}
        return obj

    validateNotNull(lastItem)
    if fieldName is not None:
        nextItemURL = nextItemURL + fieldName + fieldValue + '&nextItem=' + lastItem
    else:
        nextItemURL = nextItemURL + '&nextItem=' + lastItem
    obj = {'content': data, 'hasMore': True, 'nextItem': nextItemURL}
    return obj