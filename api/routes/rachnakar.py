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


def processGetRequest(request):
    nextItemURL = '/rachnakarjs?'
    logger.info("in processGetRequest")
    limit, nextItem, _, _, _, startCharacter = helper.getRequestParams(request)
    logger.info("startChar in processGetRequest " + startCharacter + "..")
    if startCharacter is not None or True:
        data, hasMore, lastItem = Rachnakar.getRachnakarByNamePrefix(
            limit, nextItem, startCharacter)
    else:
        data, hasMore, lastItem = Rachnakar.getAllRachnakar(limit, nextItem)

    return helper.createJSONResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL)
