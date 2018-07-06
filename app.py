#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


app.run(debug=False, host='0.0.0.0', port=5000, threaded=True)
