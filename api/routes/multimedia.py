from flask import jsonify, request

from api.globalHelpers.constants import Error
from api.globalHelpers.utilities import ValidationError
from api.models import multimedia
from api.routes.helpers.routeHelper import customError

from . import routes


@routes.route('/img/<imgId>', methods=['GET'])
def api_featured_images(imgId):
    """[Use this endpoint to fetch a file from database stored using gridfs]

    Raises:
        ValidationError -- [If content is none]

    Returns:
        [<class 'bytes'] -- [Returns a file as bytes]
    """

    content = multimedia.getMediaById(imgId)
    if content is None:
        raise ValidationError(Error.NO_MATCH_FOUND)
    return content
