from api.models import kahani as Kahani
from flask import render_template
from . import routes
from flask import request
from .helpers import routeHelper as helper
from flask import jsonify


@routes.route('/kahani', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kahani():
    if request.method == 'GET':
        return render_template('kahani.html')


@routes.route('/kahanijs', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kahani_json():
    if request.method == 'GET':
        return parseGetRequest(request, True)


@routes.route('/featuredkahanis', methods=['GET'])
def api_featured_kahani():
    content = Kahani.featuredKahani()
    return jsonify(content=content)


def parseGetRequest(request, isJson=False):
    nextItemURL = '/kahani?'
    if (isJson):
        nextItemURL = '/kahanijs?'
    limit, nextItem, content, author, title = helper.getParams(request)

    if title is not None:
        data, hasMore, lastItem = Kahani.getKahaniByTitle(
            title, limit, nextItem)
        return helper.createResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL,
                                     'title',
                                     title,
                                     isJson)

    if author is not None:
        data, hasMore, lastItem = Kahani.getKahaniByAuthor(
            author, limit, nextItem)
        return helper.createResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL,
                                     'author',
                                     author,
                                     isJson)

    if content is not None:
        data, hasMore, lastItem = Kahani.getKahaniByContent(
            content, limit, nextItem)
        return helper.createResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL,
                                     'content',
                                     content,
                                     isJson)

    else:
        data, hasMore, lastItem = Kahani.getAllKahani(
            limit, nextItem)
        return helper.createResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL,
                                     isJson=isJson)
