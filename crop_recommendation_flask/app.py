from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load trained model and label encoder
model = joblib.load("decision_tree_model.pkl")  # or decision_tree_model.pkl / neural_network_model.pkl
label_encoder = joblib.load("label_encoder.pkl")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get user input
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])   # NEW
        rainfall = float(request.form["rainfall"])
        ph = float(request.form["ph"])
        n = float(request.form["nitrogen"])
        p = float(request.form["phosphorus"])
        k = float(request.form["potassium"])

        # Feature array must match training order
        features = np.array([[n, p, k, temperature, humidity, ph, rainfall]])

        # Predict crop
        prediction = model.predict(features)[0]
        crop_name = label_encoder.inverse_transform([prediction])[0]

        return render_template("index.html", prediction_text=f"🌱 Recommended Crop: {crop_name}")

if __name__ == "__main__":
    app.run(debug=True)
