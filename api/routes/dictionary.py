from ..resources import dictionary as Dictionary
from flask import Flask, url_for,render_template
from . import routes
from flask import request
from flask import jsonify
import json
import pdb
@routes.route('/dictionary', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_dictionary():
    if request.method == 'GET':
        return render_template('dictionary.html')
    elif request.method == 'POST':
        default_word= '0'
        word = request.form.get('word', default_word)
        print('word:', word)
        limit = 50
        nextItem = None
        content = word
        data, hasMore, lastItem = Dictionary.getWord(content, limit, nextItem)
	data = json.loads(data)
	data_render = {}
	data_render["key"] = data[0]["key"]
	data_render["meanings"] = data[0]["meanings"]
	return render_template('dictionary_2.html',poem=data_render)
#        return jsonify(
#            data = data,
#            hasMore = hasMore
#        )
    else:
        return 'This HTTP verb is currently not supported.'
