from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.form

    input_data = pd.DataFrame([{
        "age": float(data["age"]),
        "sex": int(data["sex"]),
        "cp": int(data["cp"]),
        "trestbps": float(data["trestbps"]),
        "chol": float(data["chol"]),
        "fbs": int(data["fbs"]),
        "restecg": int(data["restecg"]),
        "thalach": float(data["thalach"]),
        "exang": int(data["exang"]),
        "oldpeak": float(data["oldpeak"]),
        "slope": int(data["slope"]),
        "ca": int(data["ca"]),
        "thal": int(data["thal"])
    }])

    prediction = model.predict(input_data)[0]

    result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

    return render_template("index.html", prediction=result)


@app.route("/predict_api", methods=["POST"])
def predict_api():

    data = request.get_json(force=True)

    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data)[0]

    result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

    return jsonify({"prediction": result})


if __name__ == "__main__":
    app.run(debug=True)