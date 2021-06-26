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
def detect():
    return render_template('detect.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/visualize')
def visualize():
    return render_template('visualize.html')
 
if __name__ == "__main__":
    app.run(debug=True)