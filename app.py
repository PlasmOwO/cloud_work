from flask import Flask,render_template,Flask, render_template, redirect, url_for,request
from urllib.parse import urlparse
from urllib.parse import parse_qs
import sys

from moteur_search import train_search


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search() :
    resultat = train_search(str(request.args.get("fname")))
    return "resultat : " + str(resultat) 



if __name__ == "__main__" :
    app.run(host='0.0.0.0',debug=True)