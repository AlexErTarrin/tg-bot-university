import json

import telebot
from telebot import types

config = json.load(open('config.json', encoding="utf-8"))
bot = telebot.TeleBot(config["token"])


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    for state in config["states"]:
        if message.text in state["keys"]:
            set_state(message, state)
            return
    # если не нашли подходящее состояние, то пишем тсандартный текст
    bot.send_message(message.from_user.id, config["default_text"])


def set_state(message, state):
    is_keyboard = "keyboard" in state
    markup = None

    if is_keyboard:
        markup = types.ReplyKeyboardMarkup()
        for key in state["keyboard"]:
            button = types.KeyboardButton(str(key))
            markup.row(button)

    bot.send_message(
        chat_id=message.chat.id,
        text=state["text"],
        reply_markup=markup
    )


print("Бот запущен!")
bot.polling(none_stop=True, interval=0)
