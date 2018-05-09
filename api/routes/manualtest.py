from . import routes
from flask import request, jsonify

@routes.route('/manualtest', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_manual_test():
    if request.method == 'GET':
        # call any function, and put the result in the content = line below
        return jsonify(
            content="Replace this line with a value returned by the function you're trying to test"
        )