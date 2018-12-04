# -*- coding: utf-8 -*-
from .routes import routes
from flask import Flask, render_template, send_from_directory
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
    return " The Python server is running, but / is not a valid route. for trial use /featured/kavita"


if __name__ == '__main__':
    app.run(threaded=True)
