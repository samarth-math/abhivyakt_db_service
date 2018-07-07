from api.models import author as Author
from flask import render_template
from . import routes
from flask import request
from .helpers import routeHelper as helper
from flask import jsonify

# @routes.route('/author', methods=['GET'])
# def api_author():
#     if request.method == 'GET':
#         return render_template('author.html')

@routes.route('/authorjs', methods=['GET'])
def api_author_json():
    if request.method == 'GET':
        return processGetRequest(request)


def processGetRequest(request):
    nextItemURL = '/authorjs?'

    limit, nextItem, _ , _ , _ = helper.getRequestParams(request)

    data, hasMore, lastItem = Author.getAllAuthors(limit, nextItem)
    return helper.createJSONResponse(data,
                                hasMore,
                                lastItem,
                                nextItemURL)
