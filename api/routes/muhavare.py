from api.models import muhavare as Muhavare
from flask import render_template
from . import routes
from flask import request
from .helpers import routeHelper as helper
from flask import jsonify


@routes.route('/muhavare', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_muhavare():
    if request.method == 'GET':
        return render_template('muhavare.html')


@routes.route('/muhavarejs', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_muhavare_json():
    if request.method == 'GET':
        return processGetRequest(request)


@routes.route('/featuredmuhavare', methods=['GET'])
def api_featured_muhavare():
    content = Muhavare.featuredMuhavare()
    return jsonify(content=content)


def processGetRequest(request):
    nextItemURL = '/muhavarejs?'

    limit, nextItem, content, _, _ = helper.getRequestParams(request)

    if content is not None:
        data, hasMore, lastItem = Muhavare.getMuhavareByContent(
            content, limit, nextItem)
        return helper.createJSONResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL,
                                     'content',
                                     content)

    else:
        data, hasMore, lastItem = Muhavare.getAllMuhavare(
            limit, nextItem)
        return helper.createJSONResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL)
