from flask import Flask, request, jsonify
import numpy as np
import joblib
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load the trained model and preprocessing scaler
model = load_model('model.h5')
minmax_scaler = joblib.load('minmax_scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data as JSON from request
        data = request.get_json(force=True)

        # Extract the features to be scaled
        scaled_features = [
            data['cmc_rank'],
            data['self_reported_circulating_supply'],
            data['self_reported_market_cap'],
            data['total_supply'],
            data['circulating_supply'],
            data['max_supply'],
            data['num_market_pairs']
        ]

        # Convert scaled features to numpy array and reshape for scaling
        input_data_scaled = np.array(scaled_features).reshape(1, -1)

        # Normalize input data using the saved scaler
        input_data_scaled = minmax_scaler.transform(input_data_scaled)

        # Create the complete input data including missing features
        input_data_full = np.array([
            data['cmc_rank'],
            data['self_reported_circulating_supply'],
            data['self_reported_market_cap'],
            data['added_year'],
            data['added_month'],
            data['last_updated_year'],
            data['last_updated_month'],
            data['total_supply'],
            data['circulating_supply'],
            data['max_supply'],
            data['num_market_pairs']
        ]).reshape(1, -1)

        # Copy missing features from scaled to full input data
        input_data_full[:, [0,1,2,7,8,9,10]] = input_data_scaled[:, [0,1,2,3,4,5,6]]

        # Make predictions using the loaded model on the full input data
        predictions = model.predict(input_data_full)

        # Prepare response with predicted values
        response = {
            'predicted_price': float(predictions[0][0]),
            'predicted_percent_change': float(predictions[0][1])
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
