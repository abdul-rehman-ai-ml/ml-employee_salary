# src/lambda_function.py
import json
import joblib
import numpy as np
import os

# Load model update (cached)
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'model.pkl')
model = joblib.load(model_path)

def lambda_handler(event, context):
    try:
        # Parse update input: {"features": [exp, edu, age, hours]}
        body = json.loads(event['body']) if 'body' in event else event
        features = np.array(body['features']).reshape(1, -1)
        
        # Predict update
        prediction = model.predict(features)[0]
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'predicted_salary': round(prediction, 2)})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }