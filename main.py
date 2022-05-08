import telebot
from telebot import types

bot = telebot.TeleBot('1972729545:AAEMT7FgTquvxMEtAf2StNe91bk2Gz4iCe0')


# constants

# Кнопки
back_button = types.KeyboardButton('В начало')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start" or message.text == 'В начало':
        start_keyboard(message)
    elif message.text == 'Абитуриент':
        abiturient_keyboard(message)
    elif message.text == 'Студент':
        student_keyboard(message)
    elif message.text == 'Вопрос 1':
        bot.send_message(message.from_user.id, 'Ответ для первого вопроса')
    elif message.text == 'Вопрос 2':
        bot.send_message(message.from_user.id, 'Ответ для второго вопроса')
    elif message.text == 'Вопрос 3':
        bot.send_message(message.from_user.id, 'Ответ для третьего вопроса')
    elif message.text == 'Вопрос 4':
        bot.send_message(message.from_user.id, 'Ответ для четвертого вопроса')
    elif message.text == "/help":
        # тут можно написать инструкцию если захочешь как то это использовать
        bot.send_message(message.from_user.id, "Какой то текст")
    else:
        bot.send_message(message.from_user.id, "Напишите /start для Начала пользования")


# Стартовая клавиатура (вынес создание в отдельную функцию, для переиспользования)
def start_keyboard(message):
    markup = types.ReplyKeyboardMarkup()
    first_button = types.KeyboardButton('Абитуриент')
    second_button = types.KeyboardButton('Студент')

    markup.row(first_button)
    markup.row(second_button)
    bot.send_message(message.chat.id, text='Кто вы?', reply_markup=markup)


# Клавиатура для абитуриентов
def abiturient_keyboard(message):
    markup = types.ReplyKeyboardMarkup()
    first_button = types.KeyboardButton('Вопрос 1')
    second_button = types.KeyboardButton('Вопрос 2')

    markup.row(first_button)
    markup.row(second_button)
    markup.row(back_button)

    bot.send_message(message.chat.id, text='Выберите вопрос', reply_markup=markup)


# Клавиатура для студентов
def student_keyboard(message):
    markup = types.ReplyKeyboardMarkup()
    first_button = types.KeyboardButton('Вопрос 3')
    second_button = types.KeyboardButton('Вопрос 4')

    markup.row(first_button)
    markup.row(second_button)
    markup.row(back_button)

    bot.send_message(message.chat.id, text='Выберите вопрос',  reply_markup=markup)


bot.polling(none_stop=True, interval=0)
