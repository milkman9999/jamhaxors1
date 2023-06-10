from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/")
def hello_world():
    return render_template("index.html")


# run
#   flask --app server run 
# to start the website