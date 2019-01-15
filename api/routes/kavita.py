from api.models import kavita as Kavita
from flask import render_template
from api.routes import routes
from flask import request
from api.routes.helpers import routeHelper as helper
from flask import jsonify
from api.globalHelpers.utilities import logger



@routes.route('/kavitajs', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kavita_json():
    if request.method == 'GET':
        nextItemURL = '/kavitajs?'
        limit, nextItem, content, author, title = helper.getRequestParams(
            request)

        if title is not None:
            data, hasMore, lastItem = Kavita.getKavitaByTitle(
                title, limit, nextItem)
            return helper.createJSONResponse(data,
                                            hasMore,
                                            lastItem,
                                            nextItemURL,
                                            'title',
                                            title)

        if author is not None:
            data, hasMore, lastItem = Kavita.getKavitaByAuthor(
                author, limit, nextItem)
            return helper.createJSONResponse(data,
                                            hasMore,
                                            lastItem,
                                            nextItemURL,
                                            'author',
                                            author)

        if content is not None:
            data, hasMore, lastItem = Kavita.getKavitaByContent(
                content, limit, nextItem)
            return helper.createJSONResponse(data,
                                            hasMore,
                                            lastItem,
                                            nextItemURL,
                                            'content',
                                            content)

        else:
            data, hasMore, lastItem = Kavita.getAllKavita(
                limit, nextItem)
            return helper.createJSONResponse(data,
                                            hasMore,
                                            lastItem,
                                            nextItemURL)


# There maybe benefit to going the route way with APIs, instead of
# adding arguments to the request, especially since we aren't using
# multiple arguments together for filtering, so just leaving a sample here
@routes.route('/kavita/author/<authorName>', methods=['GET'])
def kavita_by_author(authorName):
    nextItemURL = '/kahani/author/' + authorName + '?'
    limit, nextItem, _, _, _ = extractRequestParams(request)
    data, hasMore, lastItem = Kavita.getKavitaByAuthor(
        authorName, limit, nextItem)
    return helper.createJSONResponse(data, hasMore, lastItem, nextItemURL)


@routes.route('/kavita/startCharacter/<character>', methods=['GET'])
def kavita_start_char(character):
    nextItemURL = '/kavita/startCharacter/' + character + '?'
    limit, nextItem, _, _, _ = extractRequestParams(request)
    logger.info(limit)
    logger.info(nextItem)
    data, hasMore, lastItem = Kavita.getKavitaByTitlePrefix(
        limit, nextItem, character)
    return helper.createJSONResponse(data, hasMore, lastItem, nextItemURL)


@routes.route('/kavita/<objectId>', methods=['GET'])
def kavita_object(objectId):
    if request.method == 'GET':
        return helper.createJSONDataOnlyResponse(Kavita.getKavitaById(objectId))


def extractRequestParams(request):
    limit, nextItem, content, author, title = helper.getRequestParams(request)
    return limit, nextItem, content, author, title
