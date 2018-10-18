from flask import Flask, render_template, jsonify, json, url_for, request
import json
import pandas as pd
import requests
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)

key = "b732f35a4c2771732be3cd3f9acd84b2"

@app.route("/", methods=["GET"])
def home_page():

    return render_template("main.html")

@app.route("/weather", methods=["POST"])
def redirect():
    chosen_city = request.form["chosen_city"]
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + chosen_city + ",hu&units=metric&appid=" + key
    response = requests.get(url)
    data = json.loads(response.content)
    temperature = data["main"]["temp"]
    temp = "the temperature in %s is : %d" % (chosen_city, data["main"]["temp"])
    pressure = "the pressure in %s is : %d" % (chosen_city, data["main"]["pressure"])
    hum = "the humidity in %s is : %d" % (chosen_city, data["main"]["humidity"])
    temp_min = "the minimum temperature in %s is : %d" % (chosen_city, data["main"]["temp_min"])
    temp_max = "the maximum temperature in %s is : %d" % (chosen_city, data["main"]["temp_max"])
    return render_template("weather.html", temperature = temperature, temp=temp, pressure=pressure, hum=hum, temp_min=temp_min, temp_max=temp_max)






if __name__ == '__main__':
    app.run(debug=True)