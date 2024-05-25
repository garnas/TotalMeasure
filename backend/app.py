import os

from flask import Flask, send_from_directory

_static_folder = os.path.join("..", "frontend", "dist")
app = Flask(__name__, static_folder=_static_folder)


@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/assets/<path:path>")
def assets(path):
    directory_from_content_root = os.path.join("frontend", "dist", "assets")
    directory = os.path.abspath(directory_from_content_root)
    return send_from_directory(directory, path)
