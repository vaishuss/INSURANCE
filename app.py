from flask import Flask, request, jsonify, render_template
from joblib import load
import numpy as np

app = Flask(__name__)

# Load the model
model = load('my_first_project.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = np.array(int_features).reshape(1, -1)
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text=f'Predicted Charges: ${output}')

if __name__ == "__main__":
    app.run(debug=True)
