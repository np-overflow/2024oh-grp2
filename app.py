import os
from flask import Flask, request, send_from_directory
from Render.imagen import _generate
from uuid import uuid4 as uuid

app = Flask(__name__)

print(os.getcwd())


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/generate_image", methods=["POST"])
def generate_image():
    body = request.get_json()
    try:
        prompt = body["prompt"]
    except KeyError:
        return "Missing prompt", 400

    save_path = "temp/"
    rng = str(uuid())
    print(save_path+rng)
    return _generate(prompt, save_path+rng)


@app.route("/images/<path:path>")
def get_image(path):
    return send_from_directory("temp", path)
