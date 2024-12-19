from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the model
model = joblib.load('stroke_prediction.pkl')
label_encoders = joblib.load('label_encoders.pkl')

# LabelEncoder for categorical features like gender, marital_status, etc.
label_encoders = {
    'Gender': LabelEncoder(),
    'Marital Status': LabelEncoder(),
    'Work Type': LabelEncoder(),
    'Residence Type': LabelEncoder(),
    'Smoking Status': LabelEncoder()
}

# 
label_encoders['Gender'].fit(['male', 'female'])

label_encoders['Marital Status'].fit(['married', 'single', 'divorced'])
label_encoders['Work Type'].fit(['self-employed', 'employed', 'unemployed'])
label_encoders['Residence Type'].fit(['urban', 'rural'])
label_encoders['Smoking Status'].fit(['no', 'yes'])
# 

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
    # Retrieve form data
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
    # convert 'yes'/'no' to 1/0
    gender = 1 if gender == 'male' else 0
    marital_status =1 if marital_status == 'married' else (2 if marital_status =='divorced' else 0)
    work_type = 1 if work_type == 'self-employment' else ( 2 if work_type == 'unemployed' else 0)
    residence_type =1 if residence_type == 'urban' else 0
    smoke = 1 if smoke == 'yes' else 0
    hypertension = 1 if hypertension == 'yes' else 0
    heart_disease = 1 if heart_disease == 'yes' else 0
    
    
    input_df = pd.DataFrame([{
         'Age': age,
         'Gender': gender,
         'Hypertension': hypertension,
         'Heart Disease': heart_disease,
         'Marital Status': marital_status,
         'Work Type': work_type,
         'Residence Type': residence_type,
         'Average Glucose Level': glucose,
         'Body Mass Index (BMI)': bmi,
         'Smoking Status': smoke
     }])
    
    
    # Make the prediction
    pred_stroke = model.predict(input_df)
    result = int(pred_stroke[0])
    
    # prediction = model.predict(input_features)

    # Prepare the result message
    if result == 0:
        result_message = f"{name}, you will not get stroke."
    else:
        result_message = f"{name}, you will get stroke."

    return render_template('predict.html', a=result_message)
    
    
if __name__ == '__main__':
    app.run(debug=True)