from ..resources import kavita as Kavita
from flask import Flask, url_for,render_template
from . import routes
from flask import request
from flask import jsonify

@routes.route('/kavita', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kavita():
    if request.method == 'GET':
        nextItemURL = 'http://127.0.0.1:5000/kavita?'
        limit = 50
        nextItem = None
        if 'limit' in request.args:
            print('You requested limit')
            limit = int(request.args['limit'])
        if 'nextItem' in request.args:
            nextItem = request.args['nextItem']
            #print('next item is;', nextItem)

        if 'title' in request.args:
            title = request.args['title']
            print('Title:', title)
            data, hasMore, lastItem = Kavita.getKavitaByTitle(
                title, limit, nextItem)
            js = data
            print('Return type of data from kavita.py', type(data))
            print('last item: ', lastItem)
            if hasMore is True:
                nextItemURL = nextItemURL + 'title=' + \
                    title + '&nextItem=' + lastItem
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

        elif 'author' in request.args:
            author = request.args['author']
            data, hasMore, lastItem = Kavita.getKavitaByAuthor(
                author, limit, nextItem)
            js = data
            data, hasMore, lastItem = Kavita.getKavitaByTitle(
                author, limit, nextItem)
            print('Return type of data from kavita.py', type(data))
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
            data, hasMore, lastItem = Kavita.getKavitaByContent(
                content, limit, nextItem)
            js = data
            data, hasMore, lastItem = Kavita.getKavitaByTitle(
                content, limit, nextItem)
            print('Return type of data from kavita.py', type(data))
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
            data, hasMore, lastItem = Kavita.getAllKavita(limit, nextItem)
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
