from ..resources import kahani as Kahani
from flask import render_template
from . import routes
from flask import request
import commonHelperFunctions as helper


@routes.route('/kahani', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kahani():
    if request.method == 'GET':
        dataObject = parseGetRequest(request)
        stories = dataObject.get('content')
        error = dataObject.get('error')
        return render_template('kahani.html', stories=stories, error=error)


@routes.route('/kahanijs', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kahani_json():
    if request.method == 'GET':
        return parseGetRequest(request, True)


def parseGetRequest(request, isJson=False):
    nextItemURL = 'http://127.0.0.1:5000/kahani?'
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
