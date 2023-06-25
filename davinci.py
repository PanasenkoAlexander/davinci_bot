import openai
import telebot
import os
import dotenv

dotenv.load_dotenv()
openai.api_key = os.environ.get('api_key')
token = os.environ['bot_token']
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет, я твой gpt-бот! Буду рад общению.')


@bot.message_handler(func=lambda message: True)
def user_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])


print("Бот запущен")
bot.polling(none_stop=True)
