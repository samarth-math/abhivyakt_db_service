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
        return parseGetRequest(request)


@routes.route('/featuredkahanis', methods=['GET'])
def api_featured_kahani():
    content = Kahani.featuredKahani()
    return jsonify(content=content)


def parseGetRequest(request):
    nextItemURL = '/kahanijs?'
    limit, nextItem, content, author, title = helper.getParams(request)

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
