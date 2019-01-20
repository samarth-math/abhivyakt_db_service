# -*- coding: utf-8 -*-
import sentry_sdk
from .routes import routes
from flask import Flask, render_template, send_from_directory
from sentry_sdk.integrations.flask import FlaskIntegration
# This file is where the program starts
# but each API has it's own file in the routes
# sub directory.
# any new APIs should be added as a separate file in the
# routes sub directory
#
# We will only keep the route API here, and eventually
# remove all others

# Refer url: https://docs.sentry.io/error-reporting/quickstart/?platform=python#configure-the-sdk
# for configuration and additional parameter supported. Here we are
# initializing the Sentry sdk with Data Source Name linked to Abhivyakt
# account. If we migrate to a different id or account, only this value
# needs to be changed.
sentry_sdk.init(
    dsn="https://2f37e9c5248c451392bd9956dad14444@sentry.io/1375493",
    integrations=[FlaskIntegration()]
)
app = Flask(__name__)
app.register_blueprint(routes)


@app.route("/")
def main():
    return " The Python server is running, but / is not a valid route. for trial use /featured/kavita"


if __name__ == '__main__':
    app.run(threaded=True)
