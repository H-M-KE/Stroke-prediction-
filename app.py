from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the model
model = joblib.load('stroke_prediction.pkl')

# LabelEncoder for categorical features like gender, marital_status, etc.
label_encoders = {
    'gender': LabelEncoder(),
    'marital_status': LabelEncoder(),
    'work_type': LabelEncoder(),
    'residence_type': LabelEncoder(),
    'smoke': LabelEncoder()
}

# 
label_encoders['gender'].fit(['male', 'female'])
label_encoders['marital_status'].fit(['married', 'single', 'divorced'])
label_encoders['work_type'].fit(['self-employed', 'employed', 'unemployed'])
label_encoders['residence_type'].fit(['urban', 'rural'])
label_encoders['smoke'].fit(['no', 'yes'])
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
    hypertension = 1 if hypertension == 'yes' else 0
    heart_disease = 1 if heart_disease == 'yes' else 0
    
    # Handle categorical data using LabelEncoder
    gender = label_encoders['gender'].transform([gender])[0]
    marital_status = label_encoders['marital_status'].transform([marital_status])[0]
    work_type = label_encoders['work_type'].transform([work_type])[0]
    residence_type = label_encoders['residence_type'].transform([residence_type])[0]
    smoke = label_encoders['smoke'].transform([smoke])[0]

    # Convert numeric inputs to floats
    age = float(age)
    bmi = float(bmi)
    glucose = float(glucose)
    hypertension = int(hypertension)  # Assuming hypertension is either 0 or 1
    heart_disease = int(heart_disease)  # Same for heart_disease

    # Create the input array for the model
    input_array = np.array([[gender, age, hypertension, heart_disease, marital_status, work_type, residence_type, glucose, bmi, smoke]])

    # Make the prediction
    pred_stroke = model.predict(input_array)
    result = int(pred_stroke[0])

    # Prepare the result message
    if result == 0:
        result_message = f"{name}, you will not get stroke."
    else:
        result_message = f"{name}, you will get stroke."

    return render_template('predict.html', a=result_message)

if __name__ == '__main__':
    app.run(debug=True)