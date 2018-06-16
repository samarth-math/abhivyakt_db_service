from api.models.helpers import databaseHelperFunctions as db
from api.globalHelpers.utilities import Art

doheCollection = db.initializeDB('literature', 'dohe')
kahaniCollection = db.initializeDB('literature', 'kahani')
kavitaCollection = db.initializeDB('literature', 'kavita')
muhavareCollection = db.initializeDB('literature', 'muhavare')

authorCollection = db.initializeDB('literature', 'author')

collectionByType = {
    Art.dohe : doheCollection,
    Art.kahani : kahaniCollection,
    Art.kavita : kavitaCollection,
    Art.muhavare : muhavareCollection
}
