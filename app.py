from flask import Flask, request, jsonify
import openai  # Убедись, что библиотека OpenAI установлена

app = Flask(__name__)

# Устанавливаем API-ключ OpenAI
openai.api_key = "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"

@app.route('/', methods=['GET'])
def home():
    return "Сервер запущен. Отправляйте POST-запросы для взаимодействия с ботом."

@app.route('/', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_message = data.get("message", "")
    
    try:
        # Запрос к OpenAI API для получения ответа
        response = openai.Completion.create(
            engine="text-davinci-003",  # Используй нужный движок
            prompt=user_message,
            max_tokens=150
        )
        bot_response = response.choices[0].text.strip()
    except Exception as e:
        bot_response = f"Ошибка: {str(e)}"
    
    return jsonify({"response": bot_response})

if name == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
