from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend is Live on Render!"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_data = request.json
        user_message = user_data.get('message', '')
        api_key = "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"
        
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": "deepseek-r1-distill-llama-70b",
                "messages": [{"role": "user", "content": user_message}]
            }
        )
        return jsonify({"status": "success", "reply": response.json()['choices'][0]['message']['content']})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
