#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, url_for
from flask import request
from flask import Response
from flask import jsonify
import resources.kavita as Res
app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Welcome to the new world of Hindi. You are gonna love it.'


@app.route('/kavita', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kavita():
    if request.method == 'GET':
        nextItemURL = 'http://127.0.0.1:5000/kavita?'
        limit = 50
        nextItem = None
        response = Response(status=404, mimetype='text')
        if 'limit' in request.args:
            print('You requested limit')
            limit = request.args['limit']
        if 'nextItem' in request.args:
            nextItem = request.args['nextItem']
            print('next item is;', nextItem)

        if 'title' in request.args:
            title = request.args['title']
            print('Title:', title)
            data, hasMore, lastItem = Res.getKavitaByTitle(
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
            response = Response(
                jsonify, status=200, mimetype='application/json')
            return response

        elif 'author' in request.args:
            author = request.args['author']
            data, hasMore, lastItem = Res.getKavitaByAuthor(
                author, limit, nextItem)
            js = data
            data, hasMore, lastItem = Res.getKavitaByTitle(
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
            data, hasMore, lastItem = Res.getKavitaByContent(
                content, limit, nextItem)
            js = data
            data, hasMore, lastItem = Res.getKavitaByTitle(
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
            data, hasMore, lastItem = Res.getAllKavita(limit, nextItem)
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


@app.route('/muhavare', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_muhavare():
    if request.method == 'GET':
        nextItemURL = 'http://127.0.0.1:5000/muhavare?'
        limit = 50
        nextItem = None
        if 'limit' in request.args:
            print('You requested limit')
            limit = request.args['limit']
        if 'nextItem' in request.args:
            nextItem = request.args['nextItem']
            print('next item is;', nextItem)

        if 'muhavara' in request.args:
            content = request.args['muhavara']
            data, hasMore, lastItem = Res.getKavitaByContent(
                content, limit, nextItem)
            js = data
            data, hasMore, lastItem = Res.getKavitaByTitle(
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
            data, hasMore, lastItem = Res.getAllKavita(limit, nextItem)
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


@app.route('/kavita/<kavitaid>')
def api_article(kavitaID):
    return 'You are reading ' + kavitaID


if __name__ == '__main__':
    app.run()
