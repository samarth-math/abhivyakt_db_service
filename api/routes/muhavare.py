from ..resources import muhavare as Muhavare
from flask import render_template
from . import routes
from flask import request
import commonHelperFunctions as helper


@routes.route('/muhavare', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_muhavare():
    if request.method == 'GET':
        dataObject = parseGetRequest(request)
        muhavare = dataObject.get('content')
        error = dataObject.get('error')
        return render_template('muhavare.html', muhavare=muhavare, error=error)


@routes.route('/muhavarejs', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_muhavare_json():
    if request.method == 'GET':
        return parseGetRequest(request, True)


def parseGetRequest(request, isJson=False):
    nextItemURL = '/muhavare?'
    if (isJson):
        nextItemURL = '/muhavarejs?'

    limit, nextItem, content, _, _ = helper.getParams(request)

    if content is not None:
        data, hasMore, lastItem = Muhavare.getMuhavareByContent(
            content, limit, nextItem)
        return helper.createResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL,
                                     'content',
                                     content,
                                     isJson)

    else:
        data, hasMore, lastItem = Muhavare.getAllMuhavare(
            limit, nextItem)
        return helper.createResponse(data,
                                     hasMore,
                                     lastItem,
                                     nextItemURL,
                                     isJson=isJson)
