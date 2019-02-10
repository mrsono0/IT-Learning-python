import sys
import model
from khaiii import KhaiiiApi
from flask_batch import add_batch_route
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    message = "Hello World from Flask in a uWSGI Nginx Docker container with Python {} on Alpine (default)".format(
        version
    )
    return message

@app.route("/khaiii")
def khaiii():
    api = KhaiiiApi()
    words = __name__
    for word in api.analyze('안녕, 세상.'):
        words += ", " + word
    return words

@app.route("/batch")
def batch():
    add_batch_route(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
