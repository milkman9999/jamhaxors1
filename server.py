from flask import Flask, request, render_template, jsonify
import sys

app = Flask(__name__)

@app.route("/main/")
def initialize_the_boy():
    print('initailize the boy')
    return render_template("index.html")

@app.route('/form/', methods =["GET", "POST"])
def gfg():
    print('in gfg')
    if request.method == "POST":
       print('in post req')
       # getting inputs from html form index
       age = request.form.get("age")
       weight = request.form.get("weight")
       sex = request.form.get("sex")
       days = request.form.get("days")
       time = request.form.get("time")
       print(age)
       print(weight)
       print(time)
       return jsonify({'age':age, 'weight':weight, 'sex':sex, 'days':days, 'time':time})
    #    return "your info: age ="+age+", weight ="+weight+", sex ="+sex+", days ="+days+", time ="+time
 
if __name__=='__main__':
   print('running app...', file=sys.stdout)
   app.run(debug = True)

# run
#   flask --app server run 
# to start the website