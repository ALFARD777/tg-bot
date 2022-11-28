import telebot
import pytz
from config import settings
from datetime import datetime
from telebot import types

bot = telebot.TeleBot(settings['token'])
currentTime = datetime.now()

def firstquestion(call):
	firstq = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Плохое', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Неудовлетворительное', callback_data = 'neud')
	key_3 = types.InlineKeyboardButton(text = 'Среднее', callback_data = 'soso')
	key_4 = types.InlineKeyboardButton(text = 'Отличное', callback_data = 'good')
	firstq.add(key_1)
	firstq.add(key_2)
	firstq.add(key_3)
	firstq.add(key_4)
	bot.send_message(call.message.chat.id, text = 'Как Вы оцениваете состояние Вашего здоровья?', reply_markup = firstq)

def secondquestion(call):
	secondq = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Редко', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	secondq.add(key_1)
	secondq.add(key_2)
	secondq.add(key_3)
	bot.send_message(call.message.chat.id, text = 'У Вас есть боли в области спины?', reply_markup = secondq)

def thirdquestion(call):
	thirdq = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Редко', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	thirdq.add(key_1)
	thirdq.add(key_2)
	thirdq.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Затекает ли у Вас спина, если сидите более 30 минут?', reply_markup = thirdq)

def fourthquestion(call):
	fourthq = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'После физической нагрузки', callback_data = 'neud')
	key_3 = types.InlineKeyboardButton(text = 'Редко', callback_data = 'soso')
	key_4 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	fourthq.add(key_1)
	fourthq.add(key_2)
	fourthq.add(key_3)
	fourthq.add(key_4)
	bot.send_message(call.message.chat.id, text = 'Болят ли у Вас суставы?', reply_markup = fourthq)

def fifthquestion(call):
	fifthq = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Редко', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	fifthq.add(key_1)
	fifthq.add(key_2)
	fifthq.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Ощущаете ли Вы дискомфорт стоп при ношении обуви?', reply_markup = fifthq)

def sixquestion(call):
	sixq = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Если резко встать', callback_data = 'neud')
	key_3 = types.InlineKeyboardButton(text = 'Редко', callback_data = 'soso')
	key_4 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	sixq.add(key_1)
	sixq.add(key_2)
	sixq.add(key_3)
	sixq.add(key_4)
	bot.send_message(call.message.chat.id, text = 'Кружится ли у Вас голова?', reply_markup = sixq)

def sevenquestion(call):
	sevenq = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто не могу заснуть', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Иногда не могу заснуть', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Хорошо', callback_data = 'good')
	sevenq.add(key_1)
	sevenq.add(key_2)
	sevenq.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Хорошо ли Вы спите?', reply_markup = sevenq)

def eightsquestion(call):
	eightsq = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Редко', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Не бывает', callback_data = 'good')
	eightsq.add(key_1)
	eightsq.add(key_2)
	eightsq.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Как часто у Вас бывает заложен нос?', reply_markup = eightsq)

def ninesquestion(call):
	ninesq = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Редко', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	ninesq.add(key_1)
	ninesq.add(key_1)
	ninesq.add(key_1)
	bot.send_message(call.message.chat.id, text = 'Бывает ли у Вас изжога?', reply_markup = ninesq)


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
		firstquestion(call)
		secondquestion(call)

	
	elif call.data == 'about':
		keyboard_start = types.InlineKeyboardMarkup()
		keyboard_startb = types.InlineKeyboardButton(text = 'Начать', callback_data = 'start')
		keyboard_start.add(keyboard_startb)
		img = open(".\\src\\img\\cvvk.png", 'rb')
		bot.send_photo(call.message.chat.id, photo = img, caption = '💡 О чем этот бот?\n\n💊 Он позволяет сопоставить симптомы с диагнозами, которые подходят для получении отсрочки от призыва на военную службу и освобождения от нее на законных основаниях. Попробуйте!', reply_markup = keyboard_start)

	#elif call.data == ''

bot.polling(none_stop = True, interval = 0)