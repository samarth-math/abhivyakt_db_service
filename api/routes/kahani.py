from api.models import kahani as Kahani
from flask import render_template
from api.routes import routes
from flask import request
from api.routes.helpers import routeHelper as helper
from flask import jsonify


@routes.route('/kahanijs', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kahani_json():
    if request.method == 'GET':
        return processGetRequest(request)


@routes.route('/kahani/<objectId>', methods=['GET'])
def kahani_object(objectId):
    if request.method == 'GET':
        return helper.createJSONDataOnlyResponse(Kahani.getKahaniById(objectId))


def processGetRequest(request):
    nextItemURL = '/kahanijs?'
    limit, nextItem, content, author, title = helper.getRequestParams(
        request)

    if title is not None:
        data, hasMore, lastItem = Kahani.getKahaniByTitle(
            title, limit, nextItem)
        return helper.createJSONResponse(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL,
                                         'title',
                                         title)

    if author is not None:
        data, hasMore, lastItem = Kahani.getKahaniByAuthor(
            author, limit, nextItem)
        return helper.createJSONResponse(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL,
                                         'author',
                                         author)

    if content is not None:
        data, hasMore, lastItem = Kahani.getKahaniByContent(
            content, limit, nextItem)
        return helper.createJSONResponse(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL,
                                         'content',
                                         content)

    else:
        data, hasMore, lastItem = Kahani.getAllKahani(
            limit, nextItem)
        return helper.createJSONResponse(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL)
