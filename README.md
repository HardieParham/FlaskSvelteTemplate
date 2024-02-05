# Svelte.js + Flask
A super simple example of using Flask as a backend server to serve a fronted Svelte app.

This example just queries the Flask server for a random number.

## Run the following for development:
- `python -m venv venv` to create a virtual environment.
- `pip install -r requirements.txt` to install dependencies.
- `python server.py` to start the Flask server.
- `cd client; npm install; npm run autobuild` to automatically build and reload the Svelte frontend when it's changed.