from flask import Flask, render_template, request, jsonify
# from flask_CORS import CORS
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)
# CORS(app)

model = joblib.load('stroke_prediction.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/bmi')
def bmi():
    return render_template('bmi.html')

@app.route('/predict', methods=['POST'])
def predictAction():
    name = request.form['name']
    age = request.form['age']
    marital_status = request.form['marital_status']
    work_type = request.form['work_type']
    residence_type = request.form['residence_type']
    gender = request.form['gender']
    bmi = request.form['bmi']
    glucose = request.form['glucose']
    smoke = request.form['smoke']
    hypertension = request.form['hypertension']
    heart_disease = request.form['heart_disease']
    
    # Add your prediction logic here

    model=pd.read_pickle('strokenew.pkl')
    

    array = [[gender,age,hypertension,heart_disease,marital_status,work_type,residence_type,glucose,bmi,smoke]]

    array = [np.array(array[0],dtype = 'float64')]
    pred_stroke = model.predict(array)
    result = int(pred_stroke[0])
    str=""
    if result==0:
        str = name + ", you will not get stroke 😀"
    else:
        str = name + ", you will get stroke 😔"
    return render_template('predict.html',a = str)

if __name__ == '__main__':
    app.run(debug=True)