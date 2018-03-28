from ..resources import kavita as Kavita
from flask import Flask, url_for,render_template
from . import routes
from flask import request
import json
import commonHelperFunctions as helper



@routes.route('/kavita_random',methods=['GET'])
def api_kavita_random():
    nextItemURL = 'http://127.0.0.1:5000/kavita?'
    data, hasMore, lastItem = Kavita.getAllKavita(1, None)
    dataObject = helper.createReturnObject(data,
                                           hasMore,
                                           lastItem,
                                           nextItemURL)
    poems = json.loads(dataObject.get('content'))
    error = dataObject.get('error')
    return render_template('kavita.html', poems=poems, error=error)


@routes.route('/kavita', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kavita():
    if request.method == 'GET':
        dataObject = parseGetRequest(request)
        poems = json.loads(dataObject.get('content'))
        error = dataObject.get('error')
        return render_template('kavita.html', poems=poems, error=error)


def parseGetRequest(request):
    nextItemURL = 'http://127.0.0.1:5000/kavita?'
    limit, nextItem, title, author, content = getParams(request)

    if title is not None:
        data, hasMore, lastItem = Kavita.getKavitaByTitle(
            title, limit, nextItem)
        return helper.createReturnObject(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL,
                                         'title',
                                         title)

    if author is not None:
        data, hasMore, lastItem = Kavita.getKavitaByAuthor(
            author, limit, nextItem)
        return helper.createReturnObject(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL,
                                         'author',
                                         author)

    if content is not None:
        data, hasMore, lastItem = Kavita.getKavitaByContent(
            content, limit, nextItem)
        return helper.createReturnObject(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL,
                                         'content',
                                         content)

    else:
        data, hasMore, lastItem = Kavita.getAllKavita(
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
