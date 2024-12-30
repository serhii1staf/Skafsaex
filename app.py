import openai
from flask import Flask, request, render_template

app = Flask(__name__)

# Вставленный ключ API OpenAI
openai.api_key = "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"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    
    # Отправка запроса в OpenAI API
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Ты можешь использовать другие модели OpenAI
            prompt=user_message,        # Сообщение пользователя
            max_tokens=150              # Максимальное количество токенов для ответа
        )
        bot_message = response.choices[0].text.strip()  # Ответ бота
        return render_template('chatbot.html', bot_message=bot_message)
    except Exception as e:
        return str(e)

if name == '__main__':
    app.run(debug=True)
