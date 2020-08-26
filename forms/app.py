from flask import Flask, render_template, request, session
from flask_session import Session


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/hello",methods=["GET","POST"])
def hello():
	if request.method == "GET":
		return render_template('get.html')
	else:	
		name = request.form.get("name")
		return render_template("hello.html",name = name)



@app.route("/notes", methods = ["GET", "POST"])
def notes():
	
	if session.get("notes") is None:
		session["notes"] = []
	if "CLEAR_SLATE" in session["notes"]:
		session["notes"] = []
	
	if request.method == "POST":
		note = request.form.get("note")
		session["notes"].append(note)

	return render_template("notes.html",notes= session["notes"])
