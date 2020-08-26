from flask import Flask, render_template
import datetime
app = Flask(__name__)


"""
program will always look for html file in dir templates
"""

@app.route("/index")
def index():
	head = "hiya homie!"
	butt = "THis is HI button"
	return render_template("index.html", headline=head, button=butt)

@app.route("/bye")
def bye():
	head = "byebyeya homie!"
	butt = "This is bye button"
	return render_template("index.html", headline=head, button=butt)

@app.route("/time")
def time():
	now = datetime.datetime.now()
	day = '-'.join(map(str,[now.day,now.month,now.year]))
	time = str(now.hour)+'-'+str(now.minute)
	head = "this is time!"
	return render_template("index.html", headline=head, button=day +'\n' +time)

@app.route("/cond")
def cond():
	now =  datetime.datetime.now()
	bolean = (now.day == 27)
	head = "this is time!"
	return render_template("bool2.html",bolean = bolean)


@app.route("/loop")
def loop():
	names = ['kaka','papa','lala']
	return render_template('loop.html', names = names)

@app.route("/")
def base():
	links = ['loop','cond','time']
	return render_template('linking.html',links=links)