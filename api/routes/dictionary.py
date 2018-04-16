from ..resources import dictionary as Dictionary
from flask import render_template
from . import routes
from flask import request
import commonHelperFunctions as helper


@routes.route('/dictionary', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_dictionary():
    if request.method == 'GET':
        return render_template('dictionary.html')
    elif request.method == 'POST':
        default_word = '0'
        word = request.form.get('word', default_word)
        data, hasMore, lastItem = Dictionary.getWord(
            word)  # get content from model
        dataObject = helper.createResponse(
            data, hasMore, lastItem)  # create a response out of it
        # store data from the response in an object
        data = dataObject.get('content')
        # get error if there's any from the response
        error = dataObject.get('error')
        # render
        return render_template('dictionary.html', dictionary=data, error=error)


@routes.route('/dictionaryjs', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_dictionary_json():
    if request.method == 'GET':
        return render_template('dictionary.html')
    elif request.method == 'POST':
        default_word = '0'
        word = request.form.get('word', default_word)
        data, hasMore, lastItem = Dictionary.getWord(
            word)  # get content from model
        # return json response
        return helper.createResponse(data, hasMore, lastItem, isJson=True)
