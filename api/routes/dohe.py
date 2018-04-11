from ..resources import dohe as Dohe
from flask import Flask, url_for, render_template
from . import routes
from flask import request
import commonHelperFunctions as helper
import json


@routes.route('/dohe', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_dohe():
    if request.method == 'GET':
        dataObject = parseGetRequest(request)
        dohe = json.loads(dataObject.get('content'))
        error = dataObject.get('error')
        return render_template('dohe.html', dohe=dohe, error=error)


@routes.route('/dohejs', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_dohe_json():
    if request.method == 'GET':
        return parseGetRequest(request, True)


def parseGetRequest(request, isJson=False):
    nextItemURL = 'http://127.0.0.1:5000/dohe?'

    limit, nextItem, content, author, _ = helper.getParams(request)

    if author is not None:
        data, hasMore, lastItem = Dohe.getDoheByAuthor(
            author, limit, nextItem)
        return helper.createResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL,
                                     'author',
                                     author,
                                     isJson)

    if content is not None:
        data, hasMore, lastItem = Dohe.getDoheByContent(
            content, limit, nextItem)
        return helper.createResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL,
                                     'content',
                                     content,
                                     isJson)

    else:
        data, hasMore, lastItem = Dohe.getAllDohe(
            limit, nextItem)
        return helper.createResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL,
                                     isJson=isJson)
