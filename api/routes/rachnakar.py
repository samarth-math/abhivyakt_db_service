from api.models import rachnakar as Rachnakar
from flask import render_template
from . import routes
from flask import request
from .helpers import routeHelper as helper
from flask import jsonify
from api.globalHelpers.utilities import logger


@routes.route('/rachnakarjs', methods=['GET'])
def api_rachnakar_json():
    if request.method == 'GET':
        nextItemURL = '/rachnakarjs?'
        limit, nextItem = extractRequestParams(request)
        data, hasMore, lastItem = Rachnakar.getAllRachnakar(limit, nextItem)
        return helper.createJSONResponse(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL)


@routes.route('/rachnakar/<objectId>', methods=['GET'])
def rachnakar_object(objectId):
    if request.method == 'GET':
        return helper.createJSONDataOnlyResponse(Rachnakar.getRachnakarById(objectId))

@routes.route('/rachnakar/homeAuthor', methods=['GET'])
def rachnakar_home_author():
    if request.method == 'GET':
        return helper.createJSONDataOnlyResponse(Rachnakar.homePageRachnakar())


@routes.route('/rachnakar/startCharacter/<character>', methods=['GET'])
def rachnakar_start_char(character):
    if request.method == 'GET':
        nextItemURL = '/rachnakar/startCharacter/' + character + '?'
        limit, nextItem = extractRequestParams(request)
        data, hasMore, lastItem = Rachnakar.getRachnakarByNamePrefix(limit, nextItem, character)
        return helper.createJSONResponse(data, hasMore, lastItem, nextItemURL)


def extractRequestParams(request):
    limit, nextItem, _, _, _ = helper.getRequestParams(request)
    return limit, nextItem
