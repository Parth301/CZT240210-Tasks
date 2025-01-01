from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and label encoders
model = joblib.load('Car_sales_model.pkl')
label_encoders = joblib.load('label_encoders.pkl')

def normalize_input(value):
    # Normalize input to lowercase for case-insensitive matching
    if isinstance(value, str):
        return value.strip().lower()
    return value

def handle_unseen_labels(value, encoder, default_value=0):
    # Handle unseen labels by checking if the value is in the encoder's classes
    try:
        if value in encoder.classes_:
            return encoder.transform([value])[0]
        else:
            return default_value  # Return a default value for unseen labels
    except Exception as e:
        print(f"Error with label encoding: {e}")
        return default_value  # Fallback for errors

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from JSON
        data = request.get_json()

        # Normalize input to handle case differences
        name = normalize_input(data['name'])
        fuel = normalize_input(data['fuel'])
        seller_type = normalize_input(data['seller_type'])
        transmission = normalize_input(data['transmission'])
        owner = normalize_input(data['owner'])

        # Handle unseen labels
        name_encoded = handle_unseen_labels(name, label_encoders['name'])
        fuel_encoded = handle_unseen_labels(fuel, label_encoders['fuel'])
        seller_type_encoded = handle_unseen_labels(seller_type, label_encoders['seller_type'])
        transmission_encoded = handle_unseen_labels(transmission, label_encoders['transmission'])
        owner_encoded = handle_unseen_labels(owner, label_encoders['owner'])

        features = [
            name_encoded,  # Encoded 'name'
            int(data['year']),
            int(data['km_driven']),
            label_encoders['fuel'].transform([data['fuel']])[0],
            label_encoders['seller_type'].transform([data['seller_type']])[0],
            label_encoders['transmission'].transform([data['transmission']])[0],
            label_encoders['owner'].transform([data['owner']])[0]
        ]

        # Predict the selling price
        prediction = model.predict([features])[0]

        # Return the prediction
        return jsonify({"predicted_price": round(prediction, 2)})
    except Exception as e:
        print("Error during prediction:", str(e))
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
