import telebot
from telebot import types
from src.config import settings

bot = telebot.TeleBot(settings['token'])
ans3 = {'ch':'Часто', 'rk':'Редко', 'no':'Нет', 'ys':'Да'}

def secondquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = ans3['ch'], callback_data = 'badsecond')
	key_2 = types.InlineKeyboardButton(text = ans3['rk'], callback_data = 'sososecond')
	key_3 = types.InlineKeyboardButton(text = ans3['no'], callback_data = 'goodsecond')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'У Вас есть боли в области спины?', reply_markup = keyboard)
	bot.delete_message(call.message.chat.id, call.message.id)

def thirdquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = ans3['ch'], callback_data = 'badthird')
	key_2 = types.InlineKeyboardButton(text = ans3['rk'], callback_data = 'sosothird')
	key_3 = types.InlineKeyboardButton(text = ans3['no'], callback_data = 'goodthird')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Затекает ли у Вас спина, если сидите более 30 минут?', reply_markup = keyboard)
	bot.delete_message(call.message.chat.id, call.message.id)
	

def fourthquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = ans3['ch'], callback_data = 'badfourth')
	key_2 = types.InlineKeyboardButton(text = 'После физической нагрузки', callback_data = 'neudfourth')
	key_3 = types.InlineKeyboardButton(text = ans3['rk'], callback_data = 'sosofourth')
	key_4 = types.InlineKeyboardButton(text = ans3['no'], callback_data = 'goodfourth')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	keyboard.add(key_4)
	bot.send_message(call.message.chat.id, text = 'Болят ли у Вас суставы?', reply_markup = keyboard)
	bot.delete_message(call.message.chat.id, call.message.id)
	

def fifthquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = ans3['ch'], callback_data = 'badfifth')
	key_2 = types.InlineKeyboardButton(text = ans3['rk'], callback_data = 'sosofifth')
	key_3 = types.InlineKeyboardButton(text = ans3['no'], callback_data = 'goodfifth')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Ощущаете ли Вы дискомфорт стоп при ношении обуви?', reply_markup = keyboard)
	bot.delete_message(call.message.chat.id, call.message.id)
	

def sixquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = ans3['ch'], callback_data = 'badsix')
	key_2 = types.InlineKeyboardButton(text = 'Если резко встать', callback_data = 'neudsix')
	key_3 = types.InlineKeyboardButton(text = ans3['rk'], callback_data = 'sososix')
	key_4 = types.InlineKeyboardButton(text = ans3['no'], callback_data = 'goodsix')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	keyboard.add(key_4)
	bot.send_message(call.message.chat.id, text = 'Кружится ли у Вас голова?', reply_markup = keyboard)
	bot.delete_message(call.message.chat.id, call.message.id)
	

def sevenquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Часто не могу заснуть', callback_data = 'badseven')
	key_2 = types.InlineKeyboardButton(text = 'Иногда не могу заснуть', callback_data = 'sososeven')
	key_3 = types.InlineKeyboardButton(text = 'Хорошо', callback_data = 'goodseven')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Хорошо ли Вы спите?', reply_markup = keyboard)
	bot.delete_message(call.message.chat.id, call.message.id)
	

def eightsquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = ans3['ch'], callback_data = 'badeights')
	key_2 = types.InlineKeyboardButton(text = ans3['rk'], callback_data = 'sosoeights')
	key_3 = types.InlineKeyboardButton(text = 'Не бывает', callback_data = 'goodeights')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Как часто у Вас бывает заложен нос?', reply_markup = keyboard)
	bot.delete_message(call.message.chat.id, call.message.id)
	

def ninesquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = ans3['ch'], callback_data = 'badnines')
	key_2 = types.InlineKeyboardButton(text = ans3['rk'], callback_data = 'sosonines')
	key_3 = types.InlineKeyboardButton(text = ans3['no'], callback_data = 'goodnines')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Бывает ли у Вас изжога?', reply_markup = keyboard)
	bot.delete_message(call.message.chat.id, call.message.id)
	

def tensquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = ans3['ch'], callback_data = 'badtens')
	key_2 = types.InlineKeyboardButton(text = ans3['rk'], callback_data = 'sosotens')
	key_3 = types.InlineKeyboardButton(text = ans3['no'], callback_data = 'goodtens')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Бывает ли у Вас тошнота?', reply_markup = keyboard)
	bot.delete_message(call.message.chat.id, call.message.id)
	

def elevensquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = ans3['ch'], callback_data = 'badelevens')
	key_2 = types.InlineKeyboardButton(text = ans3['rk'], callback_data = 'sosoelevens')
	key_3 = types.InlineKeyboardButton(text = ans3['no'], callback_data = 'goodelevens')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Бывают ли у Вас боли в животе?', reply_markup = keyboard)
	bot.delete_message(call.message.chat.id, call.message.id)
	

def twelfesquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Крупные', callback_data = 'badtwelfes')
	key_2 = types.InlineKeyboardButton(text = 'Небольшие', callback_data = 'sosotwelfes')
	key_3 = types.InlineKeyboardButton(text = ans3['no'], callback_data = 'goodtwelfes')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Есть ли у Вас родинки на голове, шее, плечах, поясе в местах соприкосновения с одеждой?', reply_markup = keyboard)
	bot.delete_message(call.message.chat.id, call.message.id)
	

def thirdteensquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = ans3['ys'], callback_data = 'badthirdteens')
	key_3 = types.InlineKeyboardButton(text = ans3['no'], callback_data = 'goodthirdteens')
	keyboard.add(key_1)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Есть ли у Вас хронические заболевания?', reply_markup = keyboard)
	bot.delete_message(call.message.chat.id, call.message.id)
	

def fourteensquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = ans3['ys'], callback_data = 'badfourteens')
	key_2 = types.InlineKeyboardButton(text = 'Небольшие', callback_data = 'sosofourteens')
	key_3 = types.InlineKeyboardButton(text = ans3['no'], callback_data = 'goodfourteens')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Есть ли у Вас прыщи на коже?', reply_markup = keyboard)
	bot.delete_message(call.message.chat.id, call.message.id)
	

def fiveteensquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = ans3['ys'], callback_data = 'badfiveteens')
	key_2 = types.InlineKeyboardButton(text = 'Не обращал внимания', callback_data = 'goodfiveteens')
	key_3 = types.InlineKeyboardButton(text = ans3['no'], callback_data = 'goodfiveteens')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	bot.send_message(call.message.chat.id, text = 'Есть ли у Вас высыпания или пятна на коже?', reply_markup = keyboard)
	bot.delete_message(call.message.chat.id, call.message.id)
	

def sixteensquestion(call):
	keyboard = types.InlineKeyboardMarkup()
	key_1 = types.InlineKeyboardButton(text = 'Ужасное', callback_data = 'badsixteens')
	key_2 = types.InlineKeyboardButton(text = 'Плохое', callback_data = 'neudsixteens')
	key_3 = types.InlineKeyboardButton(text = 'Среднее', callback_data = 'sososixteens')
	key_4 = types.InlineKeyboardButton(text = 'Хорошее', callback_data = 'goodsixteens')
	keyboard.add(key_1)
	keyboard.add(key_2)
	keyboard.add(key_3)
	keyboard.add(key_4)
	bot.send_message(call.message.chat.id, text = 'Какое у Вас зрение?', reply_markup = keyboard)
	bot.delete_message(call.message.chat.id, call.message.id)

def knowresults(call):
	end = types.InlineKeyboardButton(text = ans3['ys'], callback_data = 'finish')
	keyboard = types.InlineKeyboardMarkup().add(end)
	bot.send_message(call.message.chat.id, text = 'Завершить анкету?', reply_markup = keyboard)
	bot.delete_message(call.message.chat.id, call.message.id)