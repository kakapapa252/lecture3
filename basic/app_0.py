from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return("Hello kakapapa!! :)\n gg")
"""
export FLASK_APP=app.py
export FLASK_DEBUG=1
"""

@app.route("/kaka")
def kaka():
	return("you reached the next level")

#can use html tags

@app.route("/<string:name>")
def hello(name):
	return(f"<h1>you reached the next level {name}</h1>")