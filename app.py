from flask import Flask, render_template, request
from joblib import dump, load
import tensorflow as tf
import keras
from keras.models import load_model
import pandas as pd
import os
import xgboost as xgb

app = Flask(__name__)

fire_data = pd.read_csv("WildfireData.csv", na_values="NaN")
svm = load('svm.joblib')
elnt = load('elnt.joblib')
#model_xgb = xgb.Booster()
# model_xgb.load_model('xgb.json')
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
        # try:
        latitude = float(request.form.get("latitude"))
        longitude = float(request.form.get("longitude"))
        month = int(request.form.get("month"))
        remoteness = float(request.form.get("remoteness"))
        temperature = float(request.form.get("temperature"))
        wind = float(request.form.get("wind"))
        humidity = float(request.form.get("humidity"))
        precipitation = float(request.form.get("precipitation"))
        vegetation = int(request.form.get("vegetation"))

        assert (latitude >= -90)
        assert (latitude <= 90)
        assert (longitude >= -180)
        assert (longitude <= 180)
        assert (month >= 1)
        assert (month <= 12)
        assert (remoteness >= 0)
        assert (temperature >= -274)
        assert (wind >= 0)
        assert (humidity >= 0)
        assert (humidity <= 100)
        assert (precipitation >= 0)
        assert (vegetation == 0 or vegetation == 4 or vegetation == 9 or vegetation ==
                12 or vegetation == 14 or vegetation == 15 or vegetation == 16)

        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month = months[month - 1]

        # Create data
        columns = ['latitude', 'longitude', 'discovery_month',
                   'Vegetation', 'Temp_pre_7', 'Hum_pre_7', 'Prec_pre_7', 'Wind_pre_7']
        mag_data = fire_data[columns]
        mag_data = mag_data.dropna()

        X_data = {
            'latitude': [latitude],
            'longitude': [longitude],
            'discovery_month': [month],
            'Vegetation': [vegetation],
            'Temp_pre_7': [temperature],
            'Hum_pre_7': [humidity],
            'Prec_pre_7': [precipitation],
            'Wind_pre_7': [wind]
        }

        X_dataf = pd.DataFrame(data=X_data)
        X_dataf = X_dataf.append(mag_data)

        # One Hot Encodings
        non_dummy_cols = ['latitude', 'longitude',
                          'Temp_pre_7', 'Hum_pre_7', 'Prec_pre_7', 'Wind_pre_7']
        dummy_cols = list(set(X_dataf.columns) - set(non_dummy_cols))
        X_dataf = pd.get_dummies(X_dataf, columns=dummy_cols)

        X_dataf = X_dataf.iloc[:1]
        y_elastic = elnt.predict(X_dataf)
        y_elastic = y_elastic[0]
        #y_svm = svm.predict(X_dataf)
        #y_xgb = xgb.predict(X_dataf)
        #result = (y_svm + y_xgb + y_elastic)/3
        #result = (y_svm + y_elastic) / 2
        result = y_elastic

        # result is the final answer in acres (fire burn area)

        # fire size: 'latitude', 'longitude', 'discovery_month', 'Vegetation', 'Temp_pre_7', 'Hum_pre_7', 'Prec_pre_7', 'Wind_pre_7'
        # putout: 'fire_size', 'remoteness', 'discovery_month', 'Vegetation'

        result_rounded = round(result)
        if(result_rounded > 1000000):
            result_rounded = 1000000
        result_float = float(result_rounded)

        # Create data
        columns1 = ['fire_size', 'discovery_month',
                    'Vegetation', 'remoteness']
        putout_data = fire_data[columns1]
        putout_data = putout_data.dropna()

        X_data1 = {
            'fire_size': [result_float],
            'discovery_month': [month],
            'Vegetation': [vegetation],
            'remoteness': [remoteness]
        }

        X_dataf1 = pd.DataFrame(data=X_data1)
        X_dataf1 = X_dataf1.append(putout_data)

        # One Hot Encodings
        non_dummy_cols1 = ['fire_size', 'remoteness']
        dummy_cols1 = list(set(X_dataf1.columns) - set(non_dummy_cols1))
        X_dataf1 = pd.get_dummies(X_dataf1, columns=dummy_cols1)

        X_dataf1 = X_dataf1.iloc[:1]

        # Predict
        result1 = putout_model.predict(X_dataf1)[0][0]
        result1_rounded = round(result1)
        if(result1_rounded > 365):
            result1_rounded = 365
        output = f"Burn Area: {result_rounded} Acres\nPutout Time: {result1_rounded} Days"
        # except Exception as e:
        #    print(e)
        #    output = "Invalid parameters"

        

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
