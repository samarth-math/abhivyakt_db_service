from ..resources import muhavare as Muhavare
from flask import Flask, url_for, render_template
from . import routes
from flask import request
from flask import jsonify
from flask import Response
import json
import commonHelperFunctions as helper

@routes.route('/muhavare', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_muhavare():
    if request.method == 'GET':
        dataObject = parseGetRequest(request)
        muhavare = json.loads(dataObject.get('content'))
        error = dataObject.get('error')
        return render_template('muhavare.html', muhavare=muhavare, error=error)


def parseGetRequest(request):
    nextItemURL = 'http://127.0.0.1:5000/muhavare?'
    limit, nextItem, content = getParams(request)

    if content is not None:
        data, hasMore, lastItem = Muhavare.getMuhavareByContent(
            content, limit, nextItem)
        return helper.createReturnObject(data,
                                  hasMore,
                                  lastItem,
                                  nextItemURL,
                                  'content',
                                  content)

    else:
        data, hasMore, lastItem = Muhavare.getAllMuhavare(
            limit, nextItem)
        return helper.createReturnObject(data,
                                         hasMore,
                                         lastItem,
                                         nextItemURL)


def getParams(request):
    nextItem = request.args.get('nextItem')
    content = request.args.get('content')
    limit = request.args.get('limit')
    if limit is None:
        limit = 0
    return limit, nextItem, content
