import json
from flask import Flask, request, render_template, jsonify
import sys
import api_interact.ApiHandler

app = Flask(__name__)

@app.route("/main")
def initialize_main():
    print('[MAIN] initailizing MAIN')
    return render_template("index.html")
    

@app.post("/main/form")
def get_form():
    if request.method == "POST":
       print('[FORM] POST request logged to /main/form')
       # getting inputs from html form index
       age = request.form.get("age")
       weight = request.form.get("weight")
       sex = request.form.get("sex")
       daysavailable = request.form.get("daysavailable")
       time = request.form.get("time")
       equipment = request.form.get("equipment")
       print(age)
       print(weight)
       print(time)
       print(equipment)
       responseJSON = jsonify({'age':age, 'weight':weight, 'sex':sex, 'days available':daysavailable, 'time':time, 'equipment':equipment})
       responseStr = responseJSON.get_data(as_text=True)
       openResponse=(api_interact.ApiHandler.gen_from_prompt(("Create a personalized workout plan for an individual of {}".format(responseStr)), 0.5, 1000))
    #    if(api_interact.ApiHandler.response_check(openResponse, 0.5, 5)):
    #           print(openResponse)
    #           print("Response contains list")
    #           return openResponse
    # else:
    #             print("Model failed to generate list")
    #             return "Error while generating, please retry."
       return openResponse

@app.get("/main/form")
def initialize_form():
    print('[FORM] initailize FORM')
    return render_template("about.html")
       
 
if __name__=='__main__':
   print('running app...', file=sys.stdout)
   app.run(debug = True)

# run
#   flask --app server run 
# to start the website