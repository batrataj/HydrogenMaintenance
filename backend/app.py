from flask import Flask, jsonify, request
import pickle
import pandas as pd

app = Flask(__name__)

# هنا الموديل يرفع عندهم
model = pickle.load(open('../model/hydrogen_model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
