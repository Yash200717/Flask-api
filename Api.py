from flask import Flask,jsonify,request

from Data import data

app = Flask(__name__)
@app.route("/alldata")
def alldata():
    return jsonify({
        "data":data
    }),200
@app.route("/Planet")
def planet():
    name=request.args.get("name")
    planet_data = next(i for i in data if i ["name"]==name)
    return jsonify({
        "data":planet_data
    }),200
app.run()