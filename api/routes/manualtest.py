# -*- coding: UTF-8 -*-
from . import routes
from flask import request, jsonify
from api.models import kavita as Kavita
from api.models import kahani as Kahani

from api.models.helpers import modelHelper as model_helper
from api.models.helpers import databaseHelperFunctions as db
import json

collection = db.initializeDB('literature', 'kavita')


@routes.route('/manual_test', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_manual_test():
    if request.method == 'GET':
        # call any function, and put the result in the content = line below like shown
        content = featured()
        return jsonify(
            content=content
        )


def featured():
    content = Kavita.featuredKavita()
    return content


def resourceTestById():
    poem = {
        "title": "कलजुगी दोहे",
        "authorName": "अंसार कम्बरी",
        "objectId": "5a53058e74ad350ba00ae68b"
    }
    content = model_helper.getObjectById(collection, poem['objectId'])
    return content


def resourceTest():
    poem = {
        "title": "कलजुगी दोहे",
        "authorName": "अंसार कम्बरी"
    }
    content = model_helper.getObjectByMultifieldSearch(collection, poem)
    return content
