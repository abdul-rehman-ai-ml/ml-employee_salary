#!/bin/bash

# Exit on any error
set -e

echo "📦 Installing dependencies locally for Lambda..."
pip install -r requirements.txt -t .

echo "🗜️ Creating deployment package..."
# Create ZIP excluding unnecessary files
zip -r deploy.zip . \
  -x "*.git*" \
  -x "__pycache__/*" \
  -x "*.md" \
  -x ".github/*" \
  -x "tests/*" \
  -x "*.sh" \
  -x "data/*" \
  -x "*.pdf" \
  -x "venv/*" \
  -x ".env"

echo "🚀 Deploying to AWS Lambda..."
aws lambda update-function-code \
  --function-name salary-predictor \
  --zip-file fileb://deploy.zip

echo "✅ Deployment complete!"