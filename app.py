from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load("sleep_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['csv_file']
    if not file:
        return render_template('index.html', prediction_text="No file uploaded")

    df = pd.read_csv(file, encoding='latin1')
    if df.shape[1] != 23:
        return render_template('index.html', prediction_text=f"Error: Expected 23 features, got {df.shape[1]}")

    prediction = model.predict(df)[0]
    return render_template('index.html', prediction_text=f"Predicted Sleep Quality: {prediction:.2f}")

if __name__ == '__main__':
    app.run(debug=True)
