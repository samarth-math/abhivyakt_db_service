from api.models import dictionary as Dictionary
from flask import render_template
from . import routes
from flask import request
from api.routes.helpers import routeHelper as helper
from api.globalHelpers.constants import Error


@routes.route('/dictionary', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_dictionary():
    if request.method == 'GET':
        return render_template('dictionary.html')
    elif request.method == 'POST':
        default_word = '0'
        word = request.form.get('word', default_word)
        data, hasMore, lastItem = Dictionary.getWord(
            word)  # get content from model
        dataObject = createResponseObjectForTemplate(
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
        return helper.createJSONResponse(data, hasMore, lastItem)


## Temporarily replicated code, till we figure out how to tackle dictionary
# probably need vuejs apis to call the json endpoint
def validateNotNull(object):
    if object is None:
        raise ("ValidationERROR : Unexpected null object found")


def createResponseObjectForTemplate(data, hasMore, lastItem, nextItemURL='', fieldName=None, fieldValue=None):
    if data is None:
        obj = {'content': "{}", 'error': Error.END_OF_CONTENT, 'hasMore': False}
        return obj

    if hasMore is False:
        obj = {'content': data, 'error': "", 'hasMore': False}
        return obj

    validateNotNull(lastItem)
    if fieldName is not None:
        nextItemURL = nextItemURL + fieldName + fieldValue + '&nextItem=' + lastItem
    else:
        nextItemURL = nextItemURL + '&nextItem=' + lastItem
    obj = {'content': data, 'hasMore': True, 'nextItem': nextItemURL}
    return obj
