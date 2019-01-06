import json
import random
import os

from flask import Blueprint, jsonify

api = Blueprint("api", __name__)

images = []

for filename in os.listdir("images"):
    with open(os.path.join("images", filename), "r") as f:
        collection = filename.replace(".json", "")
        collection_images = json.load(f)
        for image in collection_images:
            image["collection"] = collection
        images += collection_images


@api.route("/get")
def get_image():
    return jsonify(random.choice(images))
