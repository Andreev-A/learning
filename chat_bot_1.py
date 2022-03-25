# -*- coding: utf-8 -*-
"""Копия блокнота "ChatBot - Day 3.ipynb"

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lfKqEmqClswr2Rn_bhNPX_Z5JeOdQpfx
"""

# pip install python - telegram - bot - -upgrade

import random
import nltk
import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import logging
# from telegram import Update, ForceReply
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# BOT_CONFIG = {
#     'intents': {
#         'hello': {
#             'examples': ['Привет!', 'Здарова', 'Хей-хей!!'],
#             'responses': ['Хай', 'Добрый вечер!', 'Здравствуйте!']
#         },
#         'bye': {
#             'examples': ['Пока', 'Увидимся!', 'Покеда'],
#             'responses': ['До свидания', 'Прощайте', 'Сайонара!']
#         }
#     }
# }

with open('D:\\BOT_CONFIG.json', encoding='utf-8') as f:
    BOT_CONFIG = json.load(f)

# with open('D:\\BOT_CONFIG.json', 'r') as input_file: # encoding='utf-8'
#     BOT_CONFIG = json.load(input_file)

# with open('D:\\BOT_CONFIG1.json', 'w') as input_file:
#     json.dump(BOT_CONFIG, input_file, ensure_ascii=False, indent=3)

"""# День 1"""

def clean(text):
    text = text.lower()
    cleaned_text = ''
    for ch in text:
        if ch in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ':
            cleaned_text = cleaned_text + ch
    return cleaned_text

def get_intent(text):
    for intent in BOT_CONFIG['intents'].keys():
        for example in BOT_CONFIG['intents'][intent]['examples']:
            w1 = clean(example)
            w2 = clean(text)
            if nltk.edit_distance(w1, w2) / max(len(w1), len(w2)) < 0.4:
                return intent
    return 'интент не найден'

"""# День 2"""

X = []
y = []

for intent in BOT_CONFIG['intents'].keys():
    try:
        for example in BOT_CONFIG['intents'][intent]['examples']:
            X.append(example)
            y.append(intent)
    except:
        pass

print(len(X), len(y), len(set(y)))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
print(len(X_train), len(X_test))

vectorizer = CountVectorizer(preprocessor=clean, analyzer='char', ngram_range=(2, 3))
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

print(len(vectorizer.get_feature_names_out()))

log_reg = LogisticRegression(C=0.2)
log_reg.fit(X_train_vect, y_train)
print(log_reg.score(X_train_vect, y_train))

print(log_reg.score(X_test_vect, y_test))

def get_intent_by_model(text):
    return log_reg.predict(vectorizer.transform([text]))[0]

def bot(question):
    intent = get_intent_by_model(question)
    return random.choice(BOT_CONFIG['intents'][intent]['responses'])

question = ''
while True:
    question = input()
    if question != 'стоп':
        answer = bot(question)
        print(answer)
    else:
        break

# """# День 3"""
#
# # Enable logging
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
# )
#
# logger = logging.getLogger(__name__)
#
#
# # Define a few command handlers. These usually take the two arguments update and
# # context.
# def start(update: Update, context: CallbackContext) -> None:
#     """Send a message when the command /start is issued."""
#     user = update.effective_user
#     update.message.reply_markdown_v2(
#         fr'Hi {user.mention_markdown_v2()}\!',
#         reply_markup=ForceReply(selective=True),
#     )
#
#
# def help_command(update: Update, context: CallbackContext) -> None:
#     """Send a message when the command /help is issued."""
#     update.message.reply_text('Help!')
#
#
# def echo(update: Update, context: CallbackContext) -> None:
#     """Echo the user message."""
#     question = update.message.text
#     try:
#         answer = bot(question)
#     except:
#         answer = 'Извините, что-то сломалось =('
#
#     update.message.reply_text(answer)
#
#
# def main() -> None:
#     """Start the bot."""
#     # Create the Updater and pass it your bot's token.
#     updater = Updater("1971454798:AAHLLbwzKp8hXfHLNo_KHg23c7420dsbstc")
#
#     # Get the dispatcher to register handlers
#     dispatcher = updater.dispatcher
#
#     # on different responses - answer in Telegram
#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(CommandHandler("help", help_command))
#
#     # on non command i.e message - echo the message on Telegram
#     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
#
#     # Start the Bot
#     updater.start_polling()
#
#     # Run the bot until you press Ctrl-C or the process receives SIGINT,
#     # SIGTERM or SIGABRT. This should be used most of the time, since
#     # start_polling() is non-blocking and will stop the bot gracefully.
#     updater.idle()
#
# main()

#######################################################################################################################

# https://t.me/apower_bot
# 1961796256:AAGeSMjx2sO8hGQq8biD_8ZAInuj3dOe4II    @Apower_TODO_bot
# 5268671568:AAF9DTbcJZkWcdJVhAHJR0BqhhAakInDhAI    t.me/apower_bot.

# Сами разработчики telebot'а предлагают не мудрить и тупо запхнуть polling в вечный цикл и ловить ошибку подключения:
#
# while True:
#     try:
#         bot.polling(none_stop=True)
#
#     except Exception as e:
#         logger.error(e)  # или просто print(e) если у вас логгера нет,
#         # или import traceback; traceback.print_exc() для печати полной инфы
#         time.sleep(15)
# UPD: с многопоточностью (которая по умолчанию) обнаружились проблемы (при перезапуске polling падало в can't start
# thread), можно их обойти, переключившись на однопоточную версию (в простых случаях подойдёт):
#
# bot = telebot.TeleBot(extras.token, threaded=False)

# Есть еще один вариант:
# вместо bot.polling(none_stop=True) написать bot.infinity_polling(True).

# bot.infinity_polling(), True в этом случае лишнее (оно прилетает в timeout=, если его оставить).

####################################################################################################################

# import telebot


# TOKEN = '5268671568:AAF9DTbcJZkWcdJVhAHJR0BqhhAakInDhAI'
#
# bot = telebot.TeleBot(TOKEN, parse_mode=None)  # Вы можете установить parse_mode по умолчанию. HTML или MARKDOWN

# memory
# from collections import defaultdict
#
# START, TITLE, PRICE, CONFIRMATION = range(4)
# USER_STATE = defaultdict(lambda: START)
#
#
# def get_state(message):
#     return USER_STATE[message.chat.id]
#
#
# def update_state(message, state):
#     USER_STATE[message.chat.id] = state
#
# @bot.message_handler(func=lambda message: get_state(message) == START)
# def handle_message(message):
#     bot.send_message(message.chat.id, text='Напишите название')
#     update_state(message, TITLE)
#
#
# @bot.message_handler(func=lambda message: get_state(message) == TITLE)
# def handle_title(message):
#     # название
#     update_product(message.chat.id, 'title', message.text)
#     bot.send_message(message.chat.id, text='Укажи цену')
#     update_state(message, PRICE)
#
#
# @bot.message_handler(func=lambda message: get_state(message) == PRICE)
# def handle_price(message):
#     update_product(message.chat.id, 'price', message.text)
#     product = get_product(message.chat.id)
#     bot.send_message(message.chat.id, text='Опубликовать объявление? {}'.format(product))
#     update_state(message, CONFIRMATION)
#
#
# @bot.message_handler(func=lambda message: get_state(message) == CONFIRMATION)
# def handle_confirmation(message):
#     if 'да' in message.text.lower():
#         bot.send_message(message.chat.id, text='Объявление опубликовано')
#     update_state(message, START)
#
#
# PRODUCTS = defaultdict(lambda: {})
#
# def update_product(user_id, key, value):
#     PRODUCTS[user_id][key] = value
#
# def get_product(user_id):
#     return PRODUCTS[user_id]
#

# # keyboard
# from telebot import types  # для меню
#
# def create_keyboard():
#     keyboard = types.InlineKeyboardMarkup(row_width=2)
#     buttons = [types.InlineKeyboardButton(text=c, callback_data=c) for c in currencies]
#     keyboard.add(*buttons)
#     return keyboard
# @bot.callback_query_handler(func=lambda x: True)
# def callback_handler(callback_query):
#     message = callback_query.message
#     text = callback_query.data
#     currency, value = check_currency_value(text)
#     if currency:
#         bot.answer_callback_query(callback_query.id, text='Курс {} равен {}.'.format(currency, value))  # всплывает
#         # bot.send_message(chat_id=message.chat.id, text='Курс {} равен {}.'.format(currency, value))  # печатается
#     else:
#         bot.send_message(chat_id=message.chat.id, text='Узнай курс валют +')
#
# # message
# currencies = ['евро', 'доллар']
#
# def check_currency(message):
#     for c in currencies:
#         if c in message.text.lower():
#             return True
#     return False
#
#
# def check_currency_value(text):
#     currency_values = {'евро': 70, 'доллар': 60}
#     for currency, value in currency_values.items():
#         if currency in text.lower():
#             return currency, value
#     return None, None
#
#
# @bot.message_handler(commands=['rate'])  # список команд, которые будут обработаны
# @bot.message_handler(func=check_currency)  # фильтр по функции
# def handle_currency(message):
#     print(message.text)
#     currency, value = check_currency_value(message.text)
#     keyboard = create_keyboard()
#     if currency:
#         bot.send_message(chat_id=message.chat.id, text='Курс {} равен {}.'.format(currency, value),
#                          reply_markup=keyboard)
#     else:
#         bot.send_message(chat_id=message.chat.id, text='Узнай курс валют +')
#
# @bot.message_handler()
# def handle_message(message):
#     print(message.text)
#     bot.send_message(message.chat.id, text='Узнай курс валют')
#
#
# # location
# def closest_bank(location):
#     lat = location.latitude
#     lon = location.longitude
#     bank_address = 'Боровичи'
#     bank_lat, bank_lon = 58.687352, 33.958809
#     return bank_address, bank_lat, bank_lon
#
# @bot.message_handler(content_types=['location'])
# def handle_location(message):
#     print(message.location)
#     bank_address, bank_lat, bank_lon = closest_bank(message.location)
#     image = open('sort.png', 'rb')
#     bot.send_photo(message.chat.id, image, caption='Ближайший банк {}'.format(bank_address))
#     # bot.send_message(message.chat.id, text='Ближайший банк {}'.format(bank_address))
#     bot.send_location(message.chat.id, bank_lat, bank_lon)


# bot.polling()


# # -*- coding: utf-8 -*-
# import telebot
#
# token = telebot.TeleBot('1465814143:AAEkiDByuv_ktremloFjYwLxRp7-9jxmucA')
# bot = telebot.TeleBot(token)
#
# @bot.message_handler(commands=['start'])
# def qwe(message):
#   bot.send_message(message.chat.id, 'Привет я бот')
#   bot.send_message(message.chat.id, 'Пока что я раздатчик ролей для игры в мафию!')
#   bot.send_message(message.chat.id, 'Скажи сколько игроков с тобой будет играть (только числами! И от 5 до 10
#   игроков)?')
#
#
# @bot.message_handler(content_types=['text'])
# def igroki(message):
#     if message.text == '11':
#         bot.send_message('Я не могу взять больше 10 игроков !!')
#     else:
#         bot.send_message('Эммм... Я вас не понял!')
#
#
#
# if __name__ == '__main__':
#      bot.polling(none_stop=True)

##################################################################################
#
# from pathlib import Path
#
#
# # Сохраним изображение, которое отправил пользователь в папку `/files/%ID пользователя/photos`
# @bot.message_handler(content_types=['photo'])
# def save_photo(message):
#     # создадим папку если её нет
#     Path(f'files/{message.chat.id}/photos').mkdir(parents=True, exist_ok=True)
#
#     # сохраним изображение
#     file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
#     downloaded_file = bot.download_file(file_info.file_path)
#     src = f'files/{message.chat.id}/' + file_info.file_path
#     with open(src, 'wb') as new_file:
#         new_file.write(downloaded_file)
#
#     # явно указано имя файла!
#     # откроем файл на чтение  преобразуем в base64
#     with open(f'files/{message.chat.id}/photos/file_0.jpg', "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#
#     # откроем БД и запишем информацию (ID пользователя, base64, подпись к фото)
#     conn = sqlite3.connect("test.db")
#     cursor = conn.cursor()
#     cursor.execute('INSERT INTO users VALUES (?, ?, ?)', (message.chat.id, encoded_string, str(message.caption)))
#     conn.commit()
#
#
# # при получении команды /img от пользователя
# @bot.message_handler(commands=['img'])
# def ext_photo(message):
#     # откроем БД и по ID пользователя извлечём данные base64
#     conn = sqlite3.connect("test.db")
#     img = conn.execute('SELECT img FROM users WHERE tlgrm_id = ?', (message.chat.id,)).fetchone()
#     if img is None:
#         conn.close()
#         return None
#     else:
#         conn.close()
#
#         # сохраним base64 в картинку и отправим пользователю
#         with open("files/imageToSave.jpg", "wb") as fh:
#             fh.write(base64.decodebytes(img[0]))
#             bot.send_photo(message.chat.id, open("files/imageToSave.jpg", "rb"))
