from flask import Flask, render_template, jsonify, json
import json
import pandas as pd
import urllib3
import requests

app = Flask(__name__)


chosen_city= "Budapest"
key = "b732f35a4c2771732be3cd3f9acd84b2"
url = "https://api.openweathermap.org/data/2.5/weather?q=" +chosen_city+ ",hu&units=metric&appid=" + key


response = requests.get(url)
data = json.loads(response.content)

temp = "the temperature in " + "chosen city is : %d" % (data["main"]["temp"])
pressure = "the pressure in " + "chosen city is : %d" % (data["main"]["pressure"])
hum = "the humidity in " + "chosen city is : %d" % (data["main"]["humidity"])
temp_min = "the minimum temperature in " + "chosen city is : %d" % (data["main"]["temp_min"])
temp_may = "the maximum temperature in " + "chosen city is : %d" % (data["main"]["temp_max"])


@app.route("/", methods=["GET"])
def home_page():
    return render_template("main.html")

@app.route("/weather", methods=["GET"])
def print_weather():
    return render_template("weather.html", temp=(temp), pressure=(pressure), hum=(hum), temp_min=(temp_min), temp_max=(temp_max))


if __name__ == '__main__':
    app.run(debug=True)