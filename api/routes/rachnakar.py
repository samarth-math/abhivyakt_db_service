from api.models import rachnakar as Rachnakar
from flask import render_template
from . import routes
from flask import request
from .helpers import routeHelper as helper
from flask import jsonify

@routes.route('/rachnakarjs', methods=['GET'])
def api_rachnakar_json():
    if request.method == 'GET':
        return processGetRequest(request)


def processGetRequest(request):
    nextItemURL = '/rachnakarjs?'

    limit, nextItem, _ , _ , _ = helper.getRequestParams(request)

    data, hasMore, lastItem = Rachnakar.getAllRachnakar(limit, nextItem)
    return helper.createJSONResponse(data,
                                hasMore,
                                lastItem,
                                nextItemURL)
