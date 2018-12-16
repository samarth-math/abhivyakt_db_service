from api.models import kavita as Kavita
from flask import render_template
from api.routes import routes
from flask import request
from api.routes.helpers import routeHelper as helper
from flask import jsonify


@routes.route('/kavitajs', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kavita_json():
    if request.method == 'GET':
        return processGetRequest(request)


@routes.route('/kavita/<objectId>', methods=['GET'])
def kavita_object(objectId):
    if request.method == 'GET':
        return helper.createJSONDataOnlyResponse(Kavita.getKavitaById(objectId))


def processGetRequest(request):
    nextItemURL = '/kavitajs?'
    limit, nextItem, content, author, title = helper.getRequestParams(
        request)

    if title is not None:
        data, hasMore, lastItem = Kavita.getKavitaByTitle(
            title, limit, nextItem)
        return helper.createJSONResponse(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL,
                                         'title',
                                         title)

    if author is not None:
        data, hasMore, lastItem = Kavita.getKavitaByAuthor(
            author, limit, nextItem)
        return helper.createJSONResponse(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL,
                                         'author',
                                         author)

    if content is not None:
        data, hasMore, lastItem = Kavita.getKavitaByContent(
            content, limit, nextItem)
        return helper.createJSONResponse(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL,
                                         'content',
                                         content)

    else:
        data, hasMore, lastItem = Kavita.getAllKavita(
            limit, nextItem)
        return helper.createJSONResponse(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL)
