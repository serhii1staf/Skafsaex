import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Вставленный ключ API
openai.api_key = "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"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=150
        )
        bot_message = response.choices[0].text.strip()
        return jsonify({"response": bot_message})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if name == '__main__':
    app.run(debug=True)
