import telebot
import time
from datetime import datetime
from telebot import types
import src.questions
from src.config import settings

bot = telebot.TeleBot(settings['token'])
currentTime = datetime.now()

@bot.message_handler(content_types = ['text'])
def get_text_messages(message):
	if message.text == '/start':
		dayTime = ['Доброй ночи.', 'Доброе утро.', 'Добрый день.', 'Добрый вечер.']
		dayTimeNow = dayTime[0]
		if currentTime.hour >= 0 and currentTime.hour <= 3:
			dayTimeNow = dayTime[0]
		elif currentTime.hour >= 4 and currentTime.hour <= 11:
			dayTimeNow = dayTime[1]
		elif currentTime.hour >= 12 and currentTime.hour <= 17:
			dayTimeNow = dayTime[2]
		else:
			dayTimeNow = dayTime[3]
		keyboard_menu = types.InlineKeyboardMarkup()
		key_start = types.InlineKeyboardButton(text = '✅ Начать', callback_data = 'start')
		keyboard_menu.add(key_start)
		key_about = types.InlineKeyboardButton(text = '💡 О чем этот бот?', callback_data = 'about')
		keyboard_menu.add(key_about)
		bot.send_message(message.from_user.id, text = dayTimeNow + ' Начать анкетирование?', reply_markup = keyboard_menu)

@bot.callback_query_handler(func = lambda call: True)
def callback_worker(call):
	if call.data == 'start':
		bot.send_message(call.message.chat.id, text = '♋️ Начало анкеты.')
		time.sleep(1)
		result = 0.0
		time.sleep(1)
		src.questions.callAllQuestions(call)
		bot.send_message(call.message.chat.id, text = 'Ваш результат: ' + result)
	
	elif call.data == 'about':
		keyboard_start = types.InlineKeyboardMarkup()
		keyboard_startb = types.InlineKeyboardButton(text = 'Начать', callback_data = 'start')
		keyboard_start.add(keyboard_startb)
		img = "https://www.mil.by/ru/health/cvvk/cvvk.png"
		bot.send_photo(call.message.chat.id, photo = img, caption = '💡 О чем этот бот?\n\n💊 Он позволяет сопоставить симптомы с диагнозами, которые подходят для получении отсрочки от призыва на военную службу и освобождения от нее на законных основаниях. Попробуйте!', reply_markup = keyboard_start)

	elif call.data == 'bad':
		result += 1
	elif call.data == 'neud':
		result += 0.33
	elif call.data == 'soso':
		result += 0.33
	elif call.data == 'good':
		result += 0

bot.polling(none_stop = True, interval = 0)