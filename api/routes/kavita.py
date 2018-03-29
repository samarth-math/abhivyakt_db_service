from ..resources import kavita as Kavita
from flask import Flask, url_for, render_template
from . import routes
from flask import request
import json
import commonHelperFunctions as helper


@routes.route('/kavita_random', methods=['GET'])
def api_kavita_random():
    nextItemURL = 'http://127.0.0.1:5000/kavita?'
    data, hasMore, lastItem = Kavita.getAllKavita(1, None)
    dataObject = helper.createResponseObjectForTemplate(data,
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


@routes.route('/kavitajs', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kavita_json():
    if request.method == 'GET':
        return parseGetRequest(request, True)


def parseGetRequest(request, isJson=False):
    nextItemURL = 'http://127.0.0.1:5000/kavita?'
    limit, nextItem, content, author, title = helper.getParams(request)

    if title is not None:
        data, hasMore, lastItem = Kavita.getKavitaByTitle(
            title, limit, nextItem)
        return helper.createResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL,
                                     'title',
                                     title,
                                     isJson)

    if author is not None:
        data, hasMore, lastItem = Kavita.getKavitaByAuthor(
            author, limit, nextItem)
        return helper.createResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL,
                                     'author',
                                     author,
                                     isJson)

    if content is not None:
        data, hasMore, lastItem = Kavita.getKavitaByContent(
            content, limit, nextItem)
        return helper.createResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL,
                                     'content',
                                     content,
                                     isJson)

    else:
        data, hasMore, lastItem = Kavita.getAllKavita(
            limit, nextItem)
        return helper.createResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL,
                                     isJson=isJson)
