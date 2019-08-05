from api.models.helpers import databaseHelperFunctions as db
from api.globalHelpers.constants import Art

doheCollection = db.initializeDB('literature', 'dohe')
kahaniCollection = db.initializeDB('literature', 'kahani')
kavitaCollection = db.initializeDB('literature', 'kavita')
muhavareCollection = db.initializeDB('literature', 'muhavare')
rachnakarCollection = db.initializeDB('literature', 'author')

collectionByType = {
    Art.dohe: doheCollection,
    Art.kahani: kahaniCollection,
    Art.kavita: kavitaCollection,
    Art.muhavare: muhavareCollection
}


def getArtTypesAsStrings():
    return map(lambda x: x.name, collectionByType.keys())


def collectionByTypeString(artType: str):
    return collectionByType[Art[artType]]
