#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, url_for
from flask import request
from flask import Response
from flask import jsonify
import resources.kavita as Res
from bson import json_util, ObjectId
import json
app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Welcome to the new world of Hindi. You are gonna love it.'


@app.route('/kavita', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_kavita():
    if request.method == 'GET':
        nextItemURL = 'http://127.0.0.1:5000/kavita?'
        limit = 50
        offset = 0
        nextItem = None
        response = Response(status=404, mimetype='text')
        if 'limit' in request.args:
            print('You requested limit')
            limit = request.args['limit']
        if 'offset' in request.args:
            print('You requested list of all kavitas')
            offset = request.args['offset']
        if 'nextItem' in request.args:
            nextItem = request.args['nextItem']
            print('next item is;', nextItem)
        if 'title' in request.args:
            title = request.args['title']
            print('Title:', title)
            data, hasMore, lastItem = Res.getKavitaByTitle(
                title, limit, offset, nextItem)
            js = data
            print('Return type of data from kavita.py', type(data))
            print('last item: ', lastItem)
            if hasMore is True:
                nextItemURL = nextItemURL + 'title=' + title + '&nextItem=' + lastItem
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
            author = request.args['autho']
            response = Res.getKavitaByAuthor(author, limit, offset, nextItem)
            js = data
            response = Response(
                js, status=200, mimetype='application/json')
            return jsonify(
                data=js
            )
        elif 'content' in request.args:
            content = request.args['content']
            data = Res.getKavitaByContent(content, limit, offset, nextItem)
            js = data
            response = Response(
                js, status=200, mimetype='application/json')
            return jsonify(
                data=js
            )
        else:
            # getKavita('all')
            print('You requested list of all kavitas')
            return response
    else:
        return 'This HTTP verb is currently not supported.'


@app.route('/kavita/<kavitaid>')
def api_article(kavitaID):
    return 'You are reading ' + kavitaID


if __name__ == '__main__':
    app.run()
