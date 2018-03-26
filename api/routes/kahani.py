from ..resources import kahani as Kahani
from flask import Flask, url_for,render_template
from . import routes
from flask import request
from flask import jsonify

@routes.route('/kahani', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kahani():
    if request.method == 'GET':
        nextItemURL = 'http://127.0.0.1:5000/kahani?'
        limit = 50
        nextItem = None
        if 'limit' in request.args:
            print('You requested limit')
            limit = int(request.args['limit'])
        if 'nextItem' in request.args:
            nextItem = request.args['nextItem']
            print('next item is;', nextItem)

        if 'title' in request.args:
            content = request.args['title']
            data, hasMore, lastItem = Kahani.getKahaniByTitle(
                content, limit, nextItem)
            js = data
            data, hasMore, lastItem = Kahani.getKahaniByTitle(
                content, limit, nextItem)
            print('Return type of data from kahani.py', type(data))
            print('last item: ', lastItem)
            if hasMore is True:
                nextItemURL = nextItemURL + 'kahani=' + \
                    content + '&nextItem=' + lastItem
                return jsonify(
                    data=js,
                    hasMore=True,
                    nextItem=nextItemURL
                )
            else:
                return jsonify(
                    data=js,
                    hasMore=False
                )
        elif 'content' in request.args:
            content = request.args['content']
            data, hasMore, lastItem = Kahani.getKahaniByContent(
                content, limit, nextItem)
            js = data
            data, hasMore, lastItem = Kahani.getKahaniByContent(
                content, limit, nextItem)
            print('Return type of data from kahani.py', type(data))
            print('last item: ', lastItem)
            if hasMore is True:
                nextItemURL = nextItemURL + 'kahani=' + \
                    content + '&nextItem=' + lastItem
                return jsonify(
                    data=js,
                    hasMore=True,
                    nextItem=nextItemURL
                )
            else:
                return jsonify(
                    data=js,
                    hasMore=False
                )

        else:
            data, hasMore, lastItem = Kahani.getAllKahani(limit, nextItem)
            if hasMore is False:
                return jsonify(
                    data=data,
                    hasMore=False
                )
            else:
                nextItemURL = nextItemURL + '&nextItem=' + lastItem
                return jsonify(
                    data=data,
                    hasMore=hasMore,
                    nextItem=nextItemURL)
    else:
        return 'This HTTP verb is currently not supported.'
