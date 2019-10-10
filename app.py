from flask import Flask
from flask import  render_template, url_for, request, session, redirect
import numpy as np
import pandas as pd


app = Flask(__name__, template_folder= "templates")


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/dash.html')
def dash():
    return render_template("dash.html")
@app.route('/data.html')
def data():
	return render_template('data.html')
@app.route('/maxtemp')
def maxtemp():
	return render_template('maxtemp.html')
@app.route('/humidity')
def humidity():
	return render_template('humidity.html')
@app.route('/cloudiness')
def cloudiness():
	return render_template('cloudiness.html')
@app.route('/windspeed')
def windspeed():
	return render_template('windspeed.html')	


if __name__ == '__main__':
    app.run(debug=True)