import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, r2_score

# Load your dataset
data = pd.read_csv("stroke_prediction_dataset.csv")

# # new
# print(data.dtypes)

# categorical_columns =['Gender', 'Smoking_Status']

# data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)
# # //////

# Display the first few rows of the dataset
print(data.head())

# Select features for training
X = data[[x for x in data.columns if x != 'Diagnosis']]  # Relevant features
y = data['Diagnosis']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)



# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate and print the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}")

# Calculate and print the R squared value
r_squared = r2_score(y_test, y_pred)
print(f"R squared value: {r_squared:.2f}")


# Find and print feature importances
feature_importances = model.feature_importances_
features = X.columns
importance_dict = dict(zip(features, feature_importances))

print("Feature importances:")
for feature, importance in importance_dict.items():
    print(f"{feature}: {importance * 100:.4f}")

# Save the trained model to a file
# joblib.dump(model, 'stroke_prediction.pkl')
# joblib.dump(LabelEncoder, 'label_encoders.pkl')
# print("Model trained and saved as 'stroke_prediction_model.pkl'")
# print("Encoder saved as 'label_encoders.pkl'" )

# Save the trained model to a file with compression
joblib.dump(model, 'stroke_prediction.pkl', compress=3)
print("Model trained and saved as 'stroke_prediction.pkl' with compression level 3")

# Save the LabelEncoder
joblib.dump(model, 'label_encoders.pkl', compress=3)
print("LabelEncoder saved as 'label_encoders.pkl' with compression level 3")


# print(data.columns)