from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def initialize_the_boy():
    return render_template("index.html")

@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting inputs from html form index
       age = request.form.get("age")
       weight = request.form.get("weight")
       sex = request.form.get("sex")
       days = request.form.get("days")
       time = request.form.get("time")
       return "age ="+age+", weight ="+weight+", sex ="+sex+", days ="+days+", time ="+time
    return render_template("index.html")
 
if __name__=='__main__':
   app.run()

# run
#   flask --app server run 
# to start the website