from ..resources import kahani as Kahani
from flask import render_template
from . import routes
from flask import request
import commonHelperFunctions as helper
import json

@routes.route('/kahani', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kahani():
    if request.method == 'GET':
        dataObject = parseGetRequest(request)
        stories = json.loads(dataObject.get('content'))
        error = dataObject.get('error')
        return render_template('kahani.html', stories=stories, error=error)

def parseGetRequest(request):
    nextItemURL = 'http://127.0.0.1:5000/kahani?'

    limit, nextItem, title, author, content = getParams(request)

    if title is not None:
        data, hasMore, lastItem = Kahani.getKahaniByTitle(
            title, limit, nextItem)
        return helper.createReturnObject(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL,
                                         'title',
                                         title)

    if author is not None:
        data, hasMore, lastItem = Kahani.getKahaniByAuthor(
            author, limit, nextItem)
        return helper.createReturnObject(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL,
                                         'author',
                                         author)

    if content is not None:
        data, hasMore, lastItem = Kahani.getKahaniByContent(
            content, limit, nextItem)
        return helper.createReturnObject(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL,
                                         'content',
                                         content)

    else:
        data, hasMore, lastItem = Kahani.getAllKahani(
            limit, nextItem)
        return helper.createReturnObject(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL)


def getParams(request):
    nextItem = request.args.get('nextItem')
    title = request.args.get('title')
    author = request.args.get('author')
    content = request.args.get('content')
    limit = request.args.get('limit')
    if limit is None:
        limit = 0
    return limit, nextItem, title, author, content
