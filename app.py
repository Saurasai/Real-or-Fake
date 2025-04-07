from flask import Flask, request, jsonify
from flask_cors import CORS  # Enable CORS
from transformers import pipeline


from flask import render_template

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return render_template('index.html')

# Load Hugging Face model for zero-shot classification
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

@app.route('/classify', methods=['POST'])
def classify():
    try:
        content = request.json.get('content') if request.json else None  # Safely get the content

        if not content:
            return jsonify({"error": "No content provided"}), 400

        result = classifier(content, candidate_labels=["AI-generated", "Human-generated"])
        return jsonify({"category": result['labels'][0], "confidence": result['scores'][0]})
    except Exception as e:
        return jsonify({"error": "Invalid request or server error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    
    