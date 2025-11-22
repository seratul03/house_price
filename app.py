from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow cross-origin requests (dev); restrict in production

@app.route('/predict', methods=['POST'])
def predict():
    payload = request.get_json(force=True, silent=True) or {}
    # simple dummy response — replace with your model logic
    area = payload.get('area', 0)
    bounded_prediction = max(1000, area * 2000)  # example
    return jsonify({
        "bounded_prediction": int(bounded_prediction),
        "message": f"₹{int(bounded_prediction)} (≈ ₹{bounded_prediction/100000:.2f} lakh)"
    })
