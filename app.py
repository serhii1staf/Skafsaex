from flask import Flask, request, jsonify
import openai

# Установи свой ключ OpenAI API
openai.api_key = "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"

app = Flask(__name__)

# Обработка запросов от фронтенда
@app.route("/", methods=["POST"])
def chatbot():
    data = request.get_json()  # Получение данных из запроса
    user_message = data.get("message")

    if not user_message:
        return jsonify({"response": "Пожалуйста, введите сообщение."})

    try:
        # Отправляем запрос в OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # Укажи нужный движок
            prompt=user_message,
            max_tokens=150,
            temperature=0.7
        )
        bot_reply = response.choices[0].text.strip()
        return jsonify({"response": bot_reply})
    except Exception as e:
        return jsonify({"response": f"Произошла ошибка: {str(e)}"})

if name == "__main__":
    app.run(debug=True)
