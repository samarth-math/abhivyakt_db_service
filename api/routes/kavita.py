from api.models import kavita as Kavita
from flask import render_template
from . import routes
from flask import request
from .helpers import routeHelper as helper
from flask import jsonify


@routes.route('/kavita', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kavita():
    if request.method == 'GET':
        return render_template('kavita.html')


@routes.route('/kavitah', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kavita_home():
    if request.method == 'GET':
        return render_template('kavitahome.html')


@routes.route('/kavitajs', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kavita_json():
    if request.method == 'GET':
        return parseGetRequest(request)


@routes.route('/featuredkavitas', methods=['GET'])
def api_featured_kavita():
    content = Kavita.featuredKavita()
    return jsonify(content=content)


def parseGetRequest(request):
    nextItemURL = '/kavitajs?'
    limit, nextItem, content, author, title = helper.getParams(request)

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
