from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "ML Model is Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Exercise 3: Add Input Validation
    if "features" not in data:
        return jsonify({"error": "Missing 'features' key in request data"}), 400
    
    input_features = data["features"]

    # Exercise 2: Handle Multiple Inputs
    if not isinstance(input_features, list) or not all(isinstance(feature, list) and len(feature) == 4 and all(isinstance(x, (int, float)) for x in feature) for feature in input_features):
        return jsonify({"error": "Invalid input format. 'features' must be a list of lists, each containing exactly 4 numeric values."}), 400

    input_features = np.array(data["features"])

    predictions = model.predict(input_features).tolist()
    # Exercise 1: Add Confidence Scores
    confidences = model.predict_proba(input_features).max(axis=1).tolist()

    return jsonify({
        "predictions": [int(pred) for pred in predictions],
        "confidences": [round(float(conf), 2) for conf in confidences]
    })

# Exercise 4: Health Check Endpoint
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

# Exercise 5: Dockerize Your Own Model
with open("housing_model.pkl", "rb") as f:
    housing_model = pickle.load(f)

@app.route("/predict_housing", methods=["POST"])
def predict_housing():
    housing_data = request.get_json()

    if not housing_data or "features" not in housing_data:
        return jsonify({"error": "Missing input features"}), 400

    try:
        features = np.array(housing_data["features"]).reshape(1, -1)
        prediction = housing_model.predict(features).tolist()
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000) #check your port number ( if it is in use, change the port number)
