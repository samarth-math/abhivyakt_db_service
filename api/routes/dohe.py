from api.models import dohe as Dohe
from flask import render_template
from . import routes
from flask import request
from .helpers import routeHelper as helper
from flask import jsonify


@routes.route('/dohejs', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_dohe_json():
    if request.method == 'GET':
        return processGetRequest(request)


def processGetRequest(request):
    nextItemURL = '/dohejs?'

    limit, nextItem, content, author, _, _ = helper.getRequestParams(request)

    if author is not None:
        data, hasMore, lastItem = Dohe.getDoheByAuthor(
            author, limit, nextItem)
        return helper.createJSONResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL,
                                     'author',
                                     author)

    if content is not None:
        data, hasMore, lastItem = Dohe.getDoheByContent(
            content, limit, nextItem)
        return helper.createJSONResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL,
                                     'content',
                                     content)

    else:
        data, hasMore, lastItem = Dohe.getAllDohe(
            limit, nextItem)
        return helper.createJSONResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL)
