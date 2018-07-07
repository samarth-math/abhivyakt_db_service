import databaseHelperFunctions as db
from enum import Enum


class Art(Enum):
    dohe = 'dohe'
    kavita = 'kavita'
    kahani = 'kahani'
    muhavare = 'muhavare'

# Helper to populate all authors from all content
#
# Usage:
# To use import 'utilities' like so => from . import utilities
#                          and call => utilities.populateAllAuthors()


def populateAllAuthors():
    kavitaCollection = db.initialize_db('literature', 'kavita')
    kahaniCollection = db.initialize_db('literature', 'kahani')
    doheCollection = db.initialize_db('literature', 'dohe')

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

    authorCollection = db.initialize_db('literature', 'author')
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
