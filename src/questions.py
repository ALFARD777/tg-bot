import telebot
from telebot import types
from src.config import settings

bot = telebot.TeleBot(settings['token'])

def firstquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Плохое', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Неудовлетворительное', callback_data = 'neud')
	key_3 = types.InlineKeyboardButton(text = 'Среднее', callback_data = 'soso')
	key_4 = types.InlineKeyboardButton(text = 'Отличное', callback_data = 'good')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	keyboard.add(key_4)
	bot.send_message(call.message.chat.id, text = 'Как Вы оцениваете состояние Вашего здоровья?', reply_markup = keyboard)

def secondquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Редко', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'У Вас есть боли в области спины?', reply_markup = keyboard)

def thirdquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Редко', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Затекает ли у Вас спина, если сидите более 30 минут?', reply_markup = keyboard)

def fourthquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'После физической нагрузки', callback_data = 'neud')
	key_3 = types.InlineKeyboardButton(text = 'Редко', callback_data = 'soso')
	key_4 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	keyboard.add(key_4)
	bot.send_message(call.message.chat.id, text = 'Болят ли у Вас суставы?', reply_markup = keyboard)

def fifthquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Редко', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Ощущаете ли Вы дискомфорт стоп при ношении обуви?', reply_markup = keyboard)

def sixquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Если резко встать', callback_data = 'neud')
	key_3 = types.InlineKeyboardButton(text = 'Редко', callback_data = 'soso')
	key_4 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	keyboard.add(key_4)
	bot.send_message(call.message.chat.id, text = 'Кружится ли у Вас голова?', reply_markup = keyboard)

def sevenquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто не могу заснуть', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Иногда не могу заснуть', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Хорошо', callback_data = 'good')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Хорошо ли Вы спите?', reply_markup = keyboard)

def eightsquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Редко', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Не бывает', callback_data = 'good')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Как часто у Вас бывает заложен нос?', reply_markup = keyboard)

def ninesquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Редко', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Бывает ли у Вас изжога?', reply_markup = keyboard)

def tensquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Редко', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Бывает ли у Вас тошнота?', reply_markup = keyboard)

def elevensquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Редко', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Бывают ли у Вас боли в животе?', reply_markup = keyboard)

def twelfesquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Крупные', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Небольшие', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Есть ли у Вас родинки на голове, шее, плечах, поясе в местах соприкосновения с одеждой?', reply_markup = keyboard)

def thirdteensquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Крупные', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Небольшие', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Есть ли у Вас родинки на голове, шее, плечах, поясе в местах соприкосновения с одеждой?', reply_markup = keyboard)

def fourteensquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Да', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Небольшие', callback_data = 'soso')
	key_3 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Есть ли у Вас прыщи на коже?', reply_markup = keyboard)

def fiveteensquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Да', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Не обращал внимания', callback_data = 'good')
	key_3 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'good')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Есть ли у Вас высыпания или пятна на коже?', reply_markup = keyboard)

def sixteensquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Ужасное', callback_data = 'bad')
	key_2 = types.InlineKeyboardButton(text = 'Плохое', callback_data = 'neud')
	key_3 = types.InlineKeyboardButton(text = 'Среднее', callback_data = 'soso')
	key_4 = types.InlineKeyboardButton(text = 'Хорошее', callback_data = 'good')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	keyboard.add(key_4)
	bot.send_message(call.message.chat.id, text = 'Какое у Вас зрение?', reply_markup = keyboard)

def callAllQuestions(call):
	firstquestion(call)
	secondquestion(call)
	thirdquestion(call)
	fourthquestion(call)
	fifthquestion(call)
	sixquestion(call)
	sevenquestion(call)
	eightsquestion(call)
	ninesquestion(call)
	tensquestion(call)
	elevensquestion(call)
	twelfesquestion(call)
	thirdteensquestion(call)
	fourteensquestion(call)
	fiveteensquestion(call)
	sixteensquestion(call)