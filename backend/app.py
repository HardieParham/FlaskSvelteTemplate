import random

from flask import Flask, send_from_directory


FRONTEND_PATH = '../frontend/dist'

def create_app():
    """Main Flask factory function. Will spin up an instance of the site.

    Returns:
        Flask: The running flask instance.
    """
    app=Flask(__name__)

    @app.route("/")
    def base():
        return send_from_directory(FRONTEND_PATH, 'index.html')

    @app.route("/<path:path>") # Path for all the static files (JS, CSS, etc.)
    def home(path):
        return send_from_directory(FRONTEND_PATH, path)


    @app.route("/rand")
    def hello():
        return str(random.randint(0, 100))
        
    return app