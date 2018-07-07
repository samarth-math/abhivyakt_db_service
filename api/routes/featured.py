from api.models import kahani as Kahani
from api.models import kavita as Kavita
from api.models import dohe as Dohe
from api.models import muhavare as Muhavare
from api.models import author as Author
from . import routes
from flask import jsonify
from api.globalHelpers.constants import Art
from api.globalHelpers.utilities import logger
from api.routes.helpers.routeHelper import customError

# without () is a pointer to the function
fetchedContent = {
    Art.dohe.value : Dohe.featuredDohe,
    Art.kahani.value : Kahani.featuredKahani,
    Art.kavita.value : Kavita.featuredKavita,
    Art.muhavare.value : Muhavare.featuredMuhavare,
    Art.author.value : Author.featuredAuthors
}

@routes.route('/featured/<artType>', methods=['GET'])
def api_featured(artType):
    if artType in fetchedContent:
        content=fetchedContent[artType]()
    else:
        return customError(statusCode=404, message=artType + " is not a valid object")
    return jsonify(content=content)
