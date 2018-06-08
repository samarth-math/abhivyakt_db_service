import logging
import os

##### Logger #####

logfolder = "logs"
if not os.path.exists(logfolder):
    os.makedirs(logfolder)
    print('Log folder created')

logpath = os.path.join("logs", "server.log")
try:
    open(logpath, 'a').close()
except:
    # TODO add this to server logging
    raise

logger = logging.getLogger('log')
logger.setLevel(logging.INFO)

handler = logging.FileHandler(logpath)
handler.setFormatter(logging.Formatter(
    '%(levelname)s | %(filename)s | %(lineno)s | %(asctime)s :: %(message)s'))
logger.addHandler(handler)

##################

##### Populate authors #####

from api.models.helpers import databaseHelperFunctions as db
from enum import Enum


class Art(Enum):
    dohe = 'dohe'
    kavita = 'kavita'
    kahani = 'kahani'

# Helper to populate all authors from all content
#
# Usage:
# To use import 'utilities' like so => from . import utilities
#                          and call => utilities.populateAllAuthors()


def populateAllAuthors():
    kavitaCollection = db.initializeDB('literature', 'kavita')
    kahaniCollection = db.initializeDB('literature', 'kahani')
    doheCollection = db.initializeDB('literature', 'dohe')

    populateAuthors(Art.kavita, kavitaCollection)
    populateAuthors(Art.kahani, kahaniCollection)
    populateAuthors(Art.dohe, doheCollection)
    return


def populateAuthors(artType, artCollection):
    print('####### Populating authors for ' + artType.value + ' ########')

    if artCollection is None:
        print('Source collection is None! Abort!')
        return

    authorFieldName = 'author'
    if artType is Art.kavita:
        authorFieldName = 'authorName'

    authorCollection = db.initializeDB('literature', 'author')
    contents = artCollection.find({})

    for content in contents:
        print('current content id ' + str(content['_id']))
        try:
            contentAuthor = content[authorFieldName]
        except:
            contentAuthor = "गुमनाम"

        existingContentIdList = []
        existingAuthor = authorCollection.find_one({'name': contentAuthor})

        if existingAuthor is not None:
            existingContents = existingAuthor[artType.value]
            if existingContents is not None:
                if isinstance(existingContents, list):
                    existingContentIdList = existingContents
                else:
                    existingContentIdList += existingContents

        authorCollection.find_one_and_update(
            {'name': contentAuthor},
            {'$set': {artType.value: existingContentIdList +
                      [content['_id']]}},
            upsert=True)
    return

##################
