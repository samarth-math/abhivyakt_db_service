from ..resources import kavita as Kavita
from flask import render_template
from . import routes
from flask import request
import commonHelperFunctions as helper


@routes.route('/kavita', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kavita():
    if request.method == 'GET':
        return render_template('kavita.html')


@routes.route('/kavitajs', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kavita_json():
    if request.method == 'GET':
        return parseGetRequest(request, True)


@routes.route('/kavita_randomjs', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kavita_random_json():
    if request.method == 'GET':
        nextItemURL = '/kavita?'
        data, hasMore, lastItem = Kavita.getAllKavita(1, None)
        return helper.createResponse(data, hasMore, lastItem, nextItemURL, isJson=True)


def parseGetRequest(request, isJson=False):
    nextItemURL = '/kavita?'
    if (isJson):
        nextItemURL = '/kavitajs?'
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
