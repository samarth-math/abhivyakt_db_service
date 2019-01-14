from api.models import kahani as Kahani
from flask import render_template
from api.routes import routes
from flask import request
from api.routes.helpers import routeHelper as helper
from flask import jsonify


@routes.route('/kahanijs', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kahani_json():
    if request.method == 'GET':
        nextItemURL = '/kahanijs?'
        limit, nextItem, content, author, title = extractRequestParams(request)
        if title is not None:
            data, hasMore, lastItem = Kahani.getKahaniByTitle(
                title, limit, nextItem)
            return helper.createJSONResponse(data,
                                            hasMore,
                                            lastItem,
                                            nextItemURL,
                                            'title',
                                            title)

        if author is not None:
            data, hasMore, lastItem = Kahani.getKahaniByAuthor(
                author, limit, nextItem)
            return helper.createJSONResponse(data,
                                            hasMore,
                                            lastItem,
                                            nextItemURL,
                                            'author',
                                            author)

        if content is not None:
            data, hasMore, lastItem = Kahani.getKahaniByContent(
                content, limit, nextItem)
            return helper.createJSONResponse(data,
                                            hasMore,
                                            lastItem,
                                            nextItemURL,
                                            'content',
                                            content)

        else:
            data, hasMore, lastItem = Kahani.getAllKahani(
                limit, nextItem)
            return helper.createJSONResponse(data,
                                            hasMore,
                                            lastItem,
                                            nextItemURL)



@routes.route('/kahani/startCharacter/<character>', methods=['GET'])
def kahani_start_char(character):
    if request.method == 'GET':
        nextItemURL = '/kahani/startCharacter/' + character + '?'
        limit, nextItem, _, _, _ = extractRequestParams(request)
        data, hasMore, lastItem = Kahani.getKahaniByTitlePrefix(limit, nextItem, character)
        return helper.createJSONResponse(data, hasMore, lastItem, nextItemURL)


@routes.route('/kahani/<objectId>', methods=['GET'])
def kahani_object(objectId):
    if request.method == 'GET':
        return helper.createJSONDataOnlyResponse(Kahani.getKahaniById(objectId))


def extractRequestParams(request):
    limit, nextItem, content, author, title = helper.getRequestParams(request)
    return limit, nextItem, content, author, title
