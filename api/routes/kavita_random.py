from ..resources import kavita as Kavita
from flask import Flask, url_for,render_template
from . import routes
import json

@routes.route('/kavita_random',methods=['GET'])
def api_kavita_random():
    data, hasMore, lastItem = Kavita.getAllKavita(1, None)
    js = data
    data = json.loads(js)
    return render_template('kavita.html',poem = data)