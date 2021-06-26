from flask import Flask, render_template, request
from joblib import dump, load
import tensorflow as tf
import keras
from keras.models import load_model
import pandas as pd
import os

app = Flask(__name__)

fire_data = pd.read_csv("WildfireData.csv", na_values="NaN")
magnitude_svm_model = load('svm.joblib')
magnitude_elnt_model = load('elnt.joblib')
magnitude_xgb_model = load('xgb.joblib')
putout_model = load_model('putout.h5')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/detect')
def about():
    return render_template('detect.html')


@app.route('/localize', methods=['GET', 'POST'])
def localize():
    return render_template('localize.html', output="")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if(request.method == 'POST'):
        output = "Unknown error"
        try:
            latitude = float(request.form.get("latitude"))
            longitude = float(request.form.get("longitude"))
            month = int(request.form.get("month"))
            remoteness = float(request.form.get("remoteness"))
            temperature = float(request.form.get("temperature"))
            wind = float(request.form.get("wind"))
            humidity = float(request.form.get("humidity"))
            precipitation = float(request.form.get("precipitation"))
            vegetation = int(request.form.get("vegetation"))
            
            assert (longitude >= -90)
            assert (longitude <= 90)
            assert (latitude >= -180)
            assert (latitude <= 180)
            assert (month >= 1)
            assert (month <= 12)
            assert (remoteness >= 0)
            assert (temperature >= -274)
            assert (wind >= 0)
            assert (humidity >= 0)
            assert (humidity <= 100)
            assert (precipitation >= 0)
            assert (vegetation >= 1)
            assert (vegetation <= 28)

            magnitude_data = fire_data[['fire_size', 'latitude', 'longitude', 'discovery_month', 'Vegetation', 'Temp_pre_7', 'Hum_pre_7', 'Prec_pre_7', 'Wind_pre_7']]

            # fire size: 'latitude', 'longitude', 'discovery_month', 'Vegetation', 'Temp_pre_7', 'Hum_pre_7', 'Prec_pre_7', 'Wind_pre_7'
            # putout: 'fire_size', 'remoteness', 'discovery_month', 'Vegetation'
            
            output = "Output"
        except:
            output = "Invalid parameters"
        return render_template('predict.html', output=output)
    else:
        return render_template('predict.html', output="")


@app.route('/visualize')
def portfolio():
    return render_template('visualize.html')

@app.route('/visualize-map')
def visualize_map():
    return render_template('visualize-map.html')

@app.route('/visualize-map2')
def visualize_map2():
    return render_template('visualize-map2.html')

if __name__ == "__main__":
    app.run(debug=True)