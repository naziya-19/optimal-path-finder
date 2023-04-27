from flask import Flask, render_template, request
from flask_cors import CORS,cross_origin
import optimalPath.pathGenerator

app = Flask(__name__)

#cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/form", methods=['POST','GET'])
def form():
    return render_template("form2.html")

CORS(app,resources={r"/result": {"origins": "*"}})

@cross_origin(origin='*')

@app.route("/result",methods=['POST','GET'])
#@cross_origin(origin='*',headers=['Content- Type','Authorization'])
#@crossdomain(origin='*',headers=['access-control-allow-origin','Content-Type'])

def output():
    country = request.form.get("country")
    city = request.form.get("city")
    state = request.form.get("state")
    placesString = request.form.get("places")
    placeslist,orderstring,orderlist = optimalPath.pathGenerator.pathGenerator(country,city,state,placesString)
    #return render_template("result.html",city=city,country=country,orderList=placeslist)
    return render_template("map.html")


# MG Road , 411001 , Sarasbaug , 411030 , Shaniwar Wada , 411011 , Magarpatta city , 411013