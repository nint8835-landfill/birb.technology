import json
import random
import os

from flask import Blueprint, jsonify

api = Blueprint("api", __name__)

images = []

for filename in os.listdir("images"):
    with open(os.path.join("images", filename), "r") as f:
        images += json.load(f)


@api.route("/get")
def get_image():
    return jsonify(random.choice(images))
