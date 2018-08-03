from api.models import spotlight as Spotlight
from . import routes
from api.routes.helpers.routeHelper import customError
from flask import jsonify
from api.globalHelpers.utilities import ValidationError
from api.globalHelpers.constants import Error
from flask import request


@routes.route('/spotlight', methods=['GET'])
def api_spotlight():
    content = Spotlight.spotlight()
    if content is None:
        raise ValidationError(Error.UNEXPECTED_NULL)
    return jsonify(content=content)