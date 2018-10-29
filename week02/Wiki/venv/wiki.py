import wikipedia
import wikipediaapi
from flask import Flask, render_template, jsonify, json, url_for, request
from flask_wtf import FlaskForm
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from methods import *
app = Flask(__name__)

# mit csinál az app: ha beírsz egy énekest, kiadja a wiki leírását, azt, hogy kötődött-e a
#Chess Records-hoz, és, ha igen, kiadja a kapcsolódó url-eket
#valamint kiadja a wiki-n fellelhető linkeket

@app.route("/", methods=["GET"])
def main_page():

    return render_template("main.html")

@app.route("/info", methods=["POST"])
def info_page():
    target = request.form["target"]
    description = wikipedia.summary(target)
    all_info = wikipedia.page(target)
    links = all_info.links
    related = ""
    for link in links:
        if link == 'Chess Records':
            related = target + " was related to Chess Records"
            my_page = opening_page(target)
            break
        else:
            related = target + " wasn't related to Chess Records"
            my_page = []


    return render_template("info.html", target = target, description = description,links = links, related = related, my_page = my_page)


if __name__ == '__main__':
    app.run(debug=True)