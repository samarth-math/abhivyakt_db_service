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
        return processGetRequest(request)


@routes.route('/rachnakar/<objectId>', methods=['GET'])
def rachnakar_object(objectId):
    if request.method == 'GET':
        return helper.createJSONDataOnlyResponse(Rachnakar.getRachnakarById(objectId))


def processGetRequest(request):
    nextItemURL = '/rachnakarjs?'
    logger.info("in processGetRequest")
    limit, nextItem, _, _, _, startCharacter = helper.getRequestParams(request)
    if startCharacter is not None:
        data, hasMore, lastItem = Rachnakar.getRachnakarByNamePrefix(
            limit, nextItem, startCharacter)
    else:
        data, hasMore, lastItem = Rachnakar.getAllRachnakar(limit, nextItem)

    return helper.createJSONResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL)
