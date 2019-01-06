from flask import Flask, render_template
app = Flask(__name__)

from birbtechnology.api import api
app.register_blueprint(api, url_prefix="/api")


@app.route("/")
def root():
    return render_template("index.html")
