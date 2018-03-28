from ..resources import dohe as Dohe
from flask import Flask, url_for,render_template
from . import routes
from flask import request
from flask import jsonify
import commonHelperFunctions as helper
import json

nextItemURL = 'http://127.0.0.1:5000/dohe?'


@routes.route('/dohe', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_dohe():
    if request.method == 'GET':
        dataObject = parseGetRequest(request)
        dohe = json.loads(dataObject.get('content'))
        error = dataObject.get('error')
        return render_template('dohe.html', dohe=dohe, error=error)

def parseGetRequest(request):
    limit, nextItem, author, content = getParams(request)

    if author is not None:
        data, hasMore, lastItem = Dohe.getDoheByAuthor(
            author, limit, nextItem)
        return helper.createReturnObject(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL,
                                         'author',
                                         author)

    if content is not None:
        data, hasMore, lastItem = Dohe.getDoheByContent(
            content, limit, nextItem)
        return helper.createReturnObject(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL,
                                         'content',
                                         content)

    else:
        data, hasMore, lastItem = Dohe.getAllDohe(
            limit, nextItem)
        return helper.createReturnObject(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL)

def getParams(request):
    nextItem = request.args.get('nextItem')
    author = request.args.get('author')
    content = request.args.get('content')
    limit = request.args.get('limit')
    if limit is None:
        limit = 0
    return limit, nextItem, author, content
