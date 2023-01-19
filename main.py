#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
import time
from datetime import datetime
from telebot import types
import src.questions
from src.config import settings

bot = telebot.TeleBot(settings['token'])
currentTime0 = datetime.now()
currentTime = currentTime0.strftime("%d/%m/%Y - %H:%M:%S")


@bot.message_handler(content_types = ['text'])
def get_text_messages(message):
    global msg
    if message.text == '/start':
        dayTime = ['Доброй ночи.', 'Доброе утро.', 'Добрый день.', 'Добрый вечер.']
        dayTimeNow = dayTime[0]
        if currentTime0.hour >= 0 and currentTime0.hour <= 3:
            dayTimeNow = dayTime[0]
        elif currentTime0.hour >= 4 and currentTime0.hour <= 11:
            dayTimeNow = dayTime[1]
        elif currentTime0.hour >= 12 and currentTime0.hour <= 17:
            dayTimeNow = dayTime[2]
        else:
            dayTimeNow = dayTime[3]
        start = types.KeyboardButton(text = '✅ Начать')
        about = types.KeyboardButton(text = '💡 О чем этот бот?')
        keyboard_m = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(start).add(about)
        msg = bot.send_message(message.from_user.id, text = dayTimeNow + ' Начать анкетирование?', reply_markup = keyboard_m)
        bot.delete_message(message.from_user.id, message.id)

    elif message.text == '✅ Начать':
        bot.delete_message(message.from_user.id, msg.id)
        img = open('./src/img/anketa.jpg', 'rb')
        startmsg = bot.send_photo(message.from_user.id, photo = img, caption = '♋️ Начало анкеты.')
        #startmsg = bot.send_message(message.from_user.id, text = '♋️ Начало анкеты.')
        bot.delete_message(message.from_user.id, message.id)
        time.sleep(1)
        global result
        global npresult
        result = 0.0
        npresult = 0.0
        time.sleep(1)
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text = 'Плохое', callback_data = 'badfirst')
        key_2 = types.InlineKeyboardButton(text = 'Неудовлетворительное', callback_data = 'neudfirst')
        key_3 = types.InlineKeyboardButton(text = 'Среднее', callback_data = 'sosofirst')
        key_4 = types.InlineKeyboardButton(text = 'Отличное', callback_data = 'goodfirst')
        keyboard.add(key_1)
        keyboard.add(key_2)
        keyboard.add(key_3)
        keyboard.add(key_4)
        bot.send_message(message.from_user.id, text = 'Как Вы оцениваете состояние Вашего здоровья?', reply_markup = keyboard)
        bot.delete_message(message.from_user.id, startmsg.id)

    elif message.text == '✅ Пройти анкетирование снова':
        bot.delete_message(message.from_user.id, msg.id)
        img = open('./src/img/anketa.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo = img, caption = '♋️ Начало анкеты.')
        bot.delete_message(message.from_user.id, message.id)
        time.sleep(1)
        result = 0.0
        npresult = 0.0
        time.sleep(1)
        keyboard = types.InlineKeyboardMarkup()
        key_1 = types.InlineKeyboardButton(text = 'Плохое', callback_data = 'badfirst')
        key_2 = types.InlineKeyboardButton(text = 'Неудовлетворительное', callback_data= 'neudfirst')
        key_3 = types.InlineKeyboardButton(text = 'Среднее', callback_data= 'sosofirst')
        key_4 = types.InlineKeyboardButton(text = 'Отличное', callback_data= 'goodfirst')
        keyboard.add(key_1)
        keyboard.add(key_2)
        keyboard.add(key_3)
        keyboard.add(key_4)
        bot.send_message(message.from_user.id, text = 'Как Вы оцениваете состояние своего здоровья?',reply_markup=keyboard)
        bot.delete_message(message.from_user.id, startmsg.id)

    elif message.text == '💡 О чем этот бот?':
        start = types.KeyboardButton(text = '✅ Начать')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(start)
        bot.delete_message(message.from_user.id, msg.id)
        img = open('./src/img/cvvk.png', 'rb')
        msg = bot.send_photo(message.from_user.id, photo = img, caption = '💡 О чем этот бот?\n\n💊 Он позволяет сопоставить симптомы с диагнозами, которые подходят для получении отсрочки от призыва на военную службу и освобождения от нее на законных основаниях. Попробуйте!', reply_markup = keyboard)
        #msg = bot.send_message(message.from_user.id, text = '💡 О чем этот бот?\n\n💊 Он позволяет сопоставить симптомы с диагнозами, которые подходят для получении отсрочки от призыва на военную службу и освобождения от нее на законных основаниях. Попробуйте!', reply_markup = keyboard)
        bot.delete_message(message.from_user.id, message.id)

    else:
        bot.send_message(message.from_user.id, text = 'Неизвестная команда')

@bot.callback_query_handler(func = lambda call: True)
def callback_worker(call):
    global result
    global npresult

#===================================================================================

    if call.data == 'badfirst':
        npresult += 1
        src.questions.secondquestion(call)
    elif call.data == 'neudfirst':
        npresult += 0.66
        src.questions.secondquestion(call)
    elif call.data == 'sosofirst':
        npresult += 0.33
        src.questions.secondquestion(call)
    elif call.data == 'goodfirst':
        npresult += 0
        src.questions.secondquestion(call)

#--------------------------------------------------------------

    elif call.data == 'badsecond':
        npresult += 1
        src.questions.thirdquestion(call)
    elif call.data == 'sososecond':
        npresult += 0.5
        src.questions.thirdquestion(call)
    elif call.data == 'goodsecond':
        npresult += 0
        src.questions.thirdquestion(call)

#--------------------------------------------------------------

    elif call.data == 'badthird':
        npresult += 1
        src.questions.fourthquestion(call)
    elif call.data == 'sosothird':
        npresult += 0.5
        src.questions.fourthquestion(call)
    elif call.data == 'goodthird':
        npresult += 0
        src.questions.fourthquestion(call)

#--------------------------------------------------------------

    elif call.data == 'badfourth':
        npresult += 1
        src.questions.fifthquestion(call)
    elif call.data == 'neudfourth':
        npresult += 0.66
        src.questions.fifthquestion(call)
    elif call.data == 'sosofourth':
        npresult += 0.33
        src.questions.fifthquestion(call)
    elif call.data == 'goodfourth':
        npresult += 0
        src.questions.fifthquestion(call)

#--------------------------------------------------------------

    elif call.data == 'badfifth':
        npresult += 1
        src.questions.sixquestion(call)
    elif call.data == 'sosofifth':
        npresult += 0.5
        src.questions.sixquestion(call)
    elif call.data == 'goodfifth':
        npresult += 0
        src.questions.sixquestion(call)

#--------------------------------------------------------------

    elif call.data == 'badsix':
        npresult += 1
        src.questions.sevenquestion(call)
    elif call.data == 'neudsix':
        npresult += 0.66
        src.questions.sevenquestion(call)
    elif call.data == 'sososix':
        npresult += 0.33
        src.questions.sevenquestion(call)
    elif call.data == 'goodsix':
        npresult += 0
        src.questions.sevenquestion(call)

#--------------------------------------------------------------

    elif call.data == 'badseven':
        npresult += 1
        src.questions.eightsquestion(call)
    elif call.data == 'sososeven':
        npresult += 0.5
        src.questions.eightsquestion(call)
    elif call.data == 'goodseven':
        npresult += 0
        src.questions.eightsquestion(call)

#--------------------------------------------------------------

    elif call.data == 'badeights':
        npresult += 1
        src.questions.ninesquestion(call)
    elif call.data == 'sosoeights':
        npresult += 0.5
        src.questions.ninesquestion(call)
    elif call.data == 'goodeights':
        npresult += 0
        src.questions.ninesquestion(call)

#--------------------------------------------------------------

    elif call.data == 'badnines':
        npresult += 1
        src.questions.tensquestion(call)
    elif call.data == 'sosonines':
        npresult += 0.5
        src.questions.tensquestion(call)
    elif call.data == 'goodnines':
        npresult += 0
        src.questions.tensquestion(call)

#--------------------------------------------------------------

    elif call.data == 'badtens':
        npresult += 1
        src.questions.elevensquestion(call)
    elif call.data == 'sosotens':
        npresult += 0.5
        src.questions.elevensquestion(call)
    elif call.data == 'goodtens':
        npresult += 0
        src.questions.elevensquestion(call)

#--------------------------------------------------------------

    elif call.data == 'badelevens':
        npresult += 1
        src.questions.twelfesquestion(call)
    elif call.data == 'sosoelevens':
        npresult += 0.5
        src.questions.twelfesquestion(call)
    elif call.data == 'goodelevens':
        npresult += 0
        src.questions.twelfesquestion(call)

#--------------------------------------------------------------

    elif call.data == 'badtwelfes':
        npresult += 1
        src.questions.thirdteensquestion(call)
    elif call.data == 'sosotwelfes':
        npresult += 0.5
        src.questions.thirdteensquestion(call)
    elif call.data == 'goodtwelfes':
        npresult += 0
        src.questions.thirdteensquestion(call)

#--------------------------------------------------------------

    elif call.data == 'badthirdteens':
        npresult += 1
        src.questions.fourteensquestion(call)
    elif call.data == 'goodthirdteens':
        npresult += 0
        src.questions.fourteensquestion(call)

#--------------------------------------------------------------

    elif call.data == 'badfourteens':
        npresult += 1
        src.questions.fiveteensquestion(call)
    elif call.data == 'sosofourteens':
        npresult += 0.5
        src.questions.fiveteensquestion(call)
    elif call.data == 'goodfourteens':
        npresult += 0
        src.questions.fiveteensquestion(call)

#--------------------------------------------------------------

    elif call.data == 'badfiveteens':
        npresult += 1
        src.questions.sixteensquestion(call)
    elif call.data == 'sosofiveteens':
        npresult += 0.5
        src.questions.sixteensquestion(call)
    elif call.data == 'goodfiveteens':
        npresult += 0
        src.questions.sixteensquestion(call)

#--------------------------------------------------------------

    elif call.data == 'badsixteens':
        npresult += 1
        src.questions.knowresults(call)
    elif call.data == 'neudsixteens':
        npresult += 0.66
        src.questions.knowresults(call)
    elif call.data == 'sososixteens':
        npresult += 0.33
        src.questions.knowresults(call)
    elif call.data == 'goodsixteens':
        npresult += 0
        src.questions.knowresults(call)

#===================================================================================

    elif call.data == 'finish':
        img = open('./src/img/anketa.jpg', 'rb')
        endmsg = bot.send_photo(call.message.id, photo = img, caption = '♋️ Завершение анкеты.')
        #endmsg = bot.send_message(call.message.chat.id, text = '♋️ Завершение анкеты.')
        bot.delete_message(call.message.chat.id, call.message.id)
        time.sleep(1)
        result = npresult / 16 * 100
        stresult = ('Что это значит?\n\nЭто значит, что с огромной вероятностью Вы попадете в армию.\nИ даже с таким здоровьем Вы можете быть негодным к службе, в случае, если по специальности Вы работаете в производстве с электричеством свыше 1000 вольт.\nЕсли Вы также являетесь студентом дневного обучения, обязательно получите подтверждающий документ из Вашего УО, который позволит получить отсрочку от срочной службы в армии.', 'Что это значит?\n\nЭто значит, что с большей вероятностью Вы попадете в армию.\nИ даже с таким здоровьем Вы можете быть негодным к службе, в случае, если по специальности Вы работаете в производстве с электричеством свыше 1000 вольт.\nКроме того, с подобным результатом возможно откосить от срочной службы, либо получить отсрочку. Попробуйте пройти тест снова и ознакомьтесь со всеми вопросами, верно ответив на которое Вы можете получить отсрочку.', 'Что это значит?\n\nЭто значит, что с большей вероятностью Вы не попадете в армию.\nИ даже с таким здоровьем Вы можете быть годным к службе, в случае, если Вы работаете по специальности, небходимой в армии.\nВы можете пройти тест снова, чтобы ознакомиться со всеми вопросами и ответами, которые помогут Вам получить отсрочку от срочной службы в армии.', 'Что это значит?\n\nЭто значит, что с огромной вероятностью Вы не попадете в армию.\nИ даже с таким здоровьем Вы можете быть годным к службе, в случае, если Вы работаете по специальности, небходимой в армии.\nВы можете пройти тест снова, чтобы ознакомиться со всеми вопросами и ответами, которые помогут Вам получить отсрочку от срочной службы в армии.', 'Что это значит?\n\nМои поздравления, как не крути, в армию Вас не возьмут!')
        time.sleep(1)
        bot.send_message(call.message.chat.id, text = f'Процент Вашей негодности к армии: {result}%')
        bot.delete_message(call.message.chat.id, endmsg.id)
        key = types.KeyboardButton('✅ Пройти анкетирование снова')
        keyboard = types.ReplyKeyboardMarkup().add(key)
        global msg

        if result < 30:
            text = stresult[0]
        elif result < 50:
            text = stresult[1]
        elif result < 70:
            text = stresult[2]
        elif result < 100:
            text = stresult[3]
        else:
            text = stresult[4]
        
        img = open('./src/img/army.jpg', 'rb')
        msg = bot.send_photo(call.message.chat.id, photo = img, caption = text, reply_markup = keyboard)
        #msg = bot.send_message(call.message.chat.id, text = text, reply_markup = keyboard)

print(f'[{currentTime}] Bot is ready!')
bot.polling(none_stop = True, interval = 0)