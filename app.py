from flask import Flask, render_template, request
import tensorflow as tf
import keras
from keras.models import load_model
import pandas as pd
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/detect')
def about():
    return render_template('detect.html')


@app.route('/detect', methods=['GET', 'POST'])
def detect():
    return render_template('detect.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if(request.method == 'POST'):
        latitude = request.form.get("latitude")
        longitude = request.form.get("longitude")
        month = request.form.get("month")
        remoteness = request.form.get("remoteness")
        temperature = request.form.get("temperature")
        wind = request.form.get("wind")
        humidity = request.form.get("humidity")
        precipitation = request.form.get("precipitation")
        vegetation = request.form.get("vegetation")
        return render_template('predict.html')
    else:
        return render_template('predict.html')


@app.route('/visualize')
def portfolio():
    return render_template('visualize.html')

@app.route('/visualize-map')
def visualize_map():
    return render_template('visualize-map.html')

if __name__ == "__main__":
    app.run(debug=True)