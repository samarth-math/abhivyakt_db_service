# -*- coding: utf-8 -*-
from . routes import routes
from flask import Flask, render_template

# This file is where the program starts
# but each API has it's own file in the routes
# sub directory.
# any new APIs should be added as a separate file in the
# routes sub directory
#
# We will only keep the route API here, and eventually
# remove all others

app = Flask(__name__)
app.register_blueprint(routes)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/kavita/<kavitaid>')
def api_article(kavitaID):
    return 'You are reading ' + kavitaID


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(threaded=True)
