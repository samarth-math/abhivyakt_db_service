# -*- coding: UTF-8 -*-
from . import routes
from flask import request, jsonify
from ..resources import kavita as Kavita
from ..resources import commonHelperFunctions as resource_helper
from ..resources import databaseHelperFunctions as db
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
        


def featured() :
    content = Kavita.featured()
    return content

def resourceTestById() :
    poem = {
    "title":"कलजुगी दोहे",
    "authorName":"अंसार कम्बरी",
    "objectId" : "5a53058e74ad350ba00ae68b"
    }
    content = resource_helper.getObjectById(collection, poem['objectId'])
    return content

def resourceTest() :
    poem = {
    "title":"कलजुगी दोहे",
    "authorName":"अंसार कम्बरी"
    }
    content = resource_helper.getObjectByMultifieldSearch(collection, poem)
    return content
