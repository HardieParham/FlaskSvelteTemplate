import random

from flask import Flask, send_from_directory

from .blueprints.financials import bp_financials

FRONTEND_PATH = '../frontend/dist'



def create_app():
    app=Flask(__name__)
    app.register_blueprint(bp_financials)
    
    # @app.route('/')
    # def index():
    #     return '<h1>Hello</h1>'
    

    @app.route("/")
    def base():
        return send_from_directory(FRONTEND_PATH, 'index.html')

    # Path for all the static files (compiled JS/CSS, etc.)
    @app.route("/<path:path>")
    def home(path):
        return send_from_directory(FRONTEND_PATH, path)


    @app.route("/rand")
    def hello():
        return str(random.randint(0, 100))
        
    return app