"""If issues with the browser not recognizing the javascript, try below code."""
# import mimetypes
# mimetypes.add_type('application/javascript', '.js')
# mimetypes.add_type('text/css', '.css')


# from flask import Flask, send_from_directory
# import random


# app = Flask(__name__)

# @app.route("/")
# def base():
#     return send_from_directory('frontend/dist', 'index.html')

# # Path for all the static files (compiled JS/CSS, etc.)
# @app.route("/<path:path>")
# def home(path):
#     return send_from_directory('frontend/dist', path)


# @app.route("/rand")
# def hello():
#     return str(random.randint(0, 100))


# if __name__ == "__main__":
#     app.run(debug=True, port=3000)

from backend import create_app


app=create_app()

if __name__ == "__main__":
    app.run(debug=True, port=3000)