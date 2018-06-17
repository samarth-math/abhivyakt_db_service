# -*- coding: UTF-8 -*-
from . import routes
from flask import request, jsonify
from api.models import kavita as Kavita
from api.models import kahani as Kahani
from api.models import author

from api.models.helpers import modelHelper as model_helper
from api.models.helpers import databaseHelperFunctions as db
from api.globalHelpers import utilities as Util
from bson.objectid import ObjectId
import json
from api.globalHelpers.utilities import logger

collection = db.initializeDB('literature', 'kavita')


@routes.route('/manual_test', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_manual_test():
    if request.method == 'GET':
        # call any function, and put the result in the content = line below like shown
        content = testGetContentForAuthor()
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

def testGetObjectsByField():
    contentCollection = db.initializeDB('literature', 'author')
    records = model_helper.getObjectsByField(contentCollection, None, 0, "name", "Kabir" )
    return records

##### Author object tests #####

def testFeaturedAuthor():
    return author.featuredAuthors()

def testGetAllAuthors():
    return author.getAllAuthors(10, None)

def testGetAuthorByName():
    return author.getAuthorByName('प्रेमनन्दन')

def testGetAuthorByDoha():
    doha = {
        "title": "कलजुगी दोहे",
        "authorName": "अंसार कम्बरी",
        "_id": "5a589b4274ad3522fbfd2cdf"
    }
    return author.getAuthorByContent(doha['_id'], Util.Art.dohe)


def testGetContentForAuthor():
    authorInfo = {
        "name": "कलजुगी",
        "dohe": [ObjectId("5a589b4274ad3522fbfd2cdc"), ObjectId("5a589b4274ad3522fbfd2cdf")]
    }
    return author.getContentForAuthor(authorInfo, Util.Art.dohe)
