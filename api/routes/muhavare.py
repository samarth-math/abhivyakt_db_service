from ..resources import muhavare as Muhavare
from flask import Flask, url_for,render_template
from . import routes
from flask import request
from flask import jsonify
from flask import Response

@routes.route('/muhavare', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_muhavare():
    if request.method == 'GET':
        nextItemURL = 'http://127.0.0.1:5000/muhavare?'
        limit = 50
        nextItem = None
        if 'limit' in request.args:
            print('You requested limit')
            limit = int(request.args['limit'])
        if 'nextItem' in request.args:
            nextItem = request.args['nextItem']
            print('next item is;', nextItem)

        if 'content' in request.args:
            content = request.args['content']
            data, hasMore, lastItem = Muhavare.getMuhavareByContent(
                content, limit, nextItem)
            js = data
            data, hasMore, lastItem = Muhavare.getMuhavareByContent(
                content, limit, nextItem)
            print('Return type of data from muhavara.py', type(data))
            print('last item: ', lastItem)
            if hasMore is True:
                nextItemURL = nextItemURL + 'muhavara=' + \
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
            data, hasMore, lastItem = Muhavare.getAllMuhavare(limit, nextItem)
            if data==None:
                return render_template('muhavare.html',title = 'test', authorName = 'author', content = 'The database has no muhavare')
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
        response = Response(status=404, mimetype='text')
        return 'This HTTP verb is currently not supported.'
