from ..resources import dohe as Dohe
from flask import Flask, url_for,render_template
from . import routes
from flask import request
from flask import jsonify

@routes.route('/dohe', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_dohe():
    if request.method == 'GET':
        nextItemURL = 'http://127.0.0.1:5000/dohe?'
        limit = 50
        nextItem = None
        if 'limit' in request.args:
            limit = int(request.args['limit'])
            print('You requested limit, new limit is: ', limit)
        if 'nextItem' in request.args:
            nextItem = request.args['nextItem']
            print('next item is;', nextItem)

        if 'author' in request.args:
            author = request.args['author']
            data, hasMore, lastItem = Dohe.getDoheByAuthor(
                author, limit, nextItem)
            js = data
            data, hasMore, lastItem = Dohe.getDoheByAuthor(
                author, limit, nextItem)
            print('Return type of data from dohe.py', type(data))
            print('last item: ', lastItem)
            if hasMore is True:
                nextItemURL = nextItemURL + 'author=' + \
                    author + '&nextItem=' + lastItem
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
            data, hasMore, lastItem = Dohe.getDoheByContent(
                content, limit, nextItem)
            js = data
            data, hasMore, lastItem = Dohe.getDoheByContent(
                content, limit, nextItem)
            print('Return type of data from dohe.py', type(data))
            print('last item: ', lastItem)
            if hasMore is True:
                nextItemURL = nextItemURL + 'content=' + \
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
            data, hasMore, lastItem = Dohe.getAllDohe(limit, nextItem)
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