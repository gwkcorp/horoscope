# -*- coding: utf-8 -*-
import random
import telebot
from telebot import types

bot = telebot.TeleBot('1710220788:AAE9WXCZQU9IUR8SX_iIPdQ2HukXEws6Lr0')

first = ['идеальный день для новых начинаний.',  'неплохой день для того, чтобы решиться на смелый поступок!', 'оптимальное время, чтобы привести в порядок некоторые финансовые вопросы.', 'лучшее время для того, чтобы начать новые отношения или разобраться со старыми.',  'плодотворный день для того, чтобы разобраться с накопившимися делами.']
second = ['следует быть остророжными при соврешении загородных поездок и обртить ванимение на вопросы, отвечающие за', 'следует обратить внимание на свое здоровье и такие вопросы как', 'следует учитывать риски, которые могут повлиять в таких вопросах как', 'следует учитывать обстоятельства, которые могут оказать влияние на такие вопросы как']
second_add = ['финансовое состояние.', 'здоровье.', 'отношения с родителями.', 'отношения с детьми.', 'отношения с коллегами.', 'отношения с начальством.', 'отношения с оргнами государственной власти.', 'отношения с вашими домашними животными.']
third = ['злые языки могут говорить вам обратное, но слушать их не следует.',' успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.', 'сегодня вам неплохо посвятить немного времени вашему физическому развитию.', 'именно сегодня вам неплохо посвятить изучению новых знаний в вашей профессиональной области.', 'сегодня вам неплохо посвятить домашним делам.']

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == '/start':
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")

        keyboard = types.InlineKeyboardMarkup()
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='oven')
        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='telec')
        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='bliznecy')
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='rak')
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='lev')
        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='deva')
        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='vesy')
        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='scorpion')
        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='strelec')
        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='kozerog')
        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='vodoley')
        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='ryby')

        keyboard.add(key_oven, key_telec, key_bliznecy, key_rak, key_lev, key_deva, key_vesy, key_scorpion, key_strelec, key_kozerog, key_vodoley, key_ryby)

        bot.send_message(message.from_user.id, "Выбери свой знак зодиака", reply_markup=keyboard)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши слово гороскоп")
    else:
        bot.send_message(message.from_user.id, "Моя твоя не понимать. Напиши /start")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    keyboard = types.InlineKeyboardMarkup()
    key_oven = types.InlineKeyboardButton(text='Овен', callback_data='oven')
    key_telec = types.InlineKeyboardButton(text='Телец', callback_data='telec')
    key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='bliznecy')
    key_rak = types.InlineKeyboardButton(text='Рак', callback_data='rak')
    key_lev = types.InlineKeyboardButton(text='Лев', callback_data='lev')
    key_deva = types.InlineKeyboardButton(text='Дева', callback_data='deva')
    key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='vesy')
    key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='scorpion')
    key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='strelec')
    key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='kozerog')
    key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='vodoley')
    key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='ryby')

    if call.data == "oven":
        msg = 'Овенам ' + '♈' + ' сегодня звезды предвещают ' + random.choice(first) + ' Но сегодня овенам ' +  random.choice(second) + ' ' + random.choice(second_add) + ' Овены' + 'помните, что сегодня ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)
        keyboard.add(key_oven, key_telec, key_bliznecy, key_rak, key_lev, key_deva, key_vesy, key_scorpion, key_strelec, key_kozerog, key_vodoley, key_ryby)
        bot.send_message(call.from_user.id, "Выбери свой знак зодиака", reply_markup=keyboard)
    elif call.data == "telec":
        msg = 'Тельцам ' + '♉' + ' сегодня звезды предвещают ' + random.choice(first) + ' Но сегодня тельцам ' + random.choice(second) + ' ' + random.choice(second_add) + ' Тельцы' + 'помните, что сегодня ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)
        keyboard.add(key_oven, key_telec, key_bliznecy, key_rak, key_lev, key_deva, key_vesy, key_scorpion, key_strelec, key_kozerog, key_vodoley, key_ryby)
        bot.send_message(call.from_user.id, "Выбери свой знак зодиака", reply_markup=keyboard)
    elif call.data == "bliznecy":
        msg = 'Близнецам ' + '♊' + ' сегодня звезды предвещают ' + random.choice(first) + ' Но сегодня близнецам ' + random.choice(second) + ' ' + random.choice(second_add) + ' Близнецы' + 'помните, что сегодня ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)
        keyboard.add(key_oven, key_telec, key_bliznecy, key_rak, key_lev, key_deva, key_vesy, key_scorpion, key_strelec, key_kozerog, key_vodoley, key_ryby)
        bot.send_message(call.from_user.id, "Выбери свой знак зодиака", reply_markup=keyboard)
    elif call.data == "rak":
        msg = 'Ракам ' + '♋' + ' сегодня звезды предвещают ' + random.choice(first) + ' Но сегодня ракам ' + random.choice(second) + ' ' + random.choice(second_add) + ' Раки' + 'помните, что сегодня ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)
        keyboard.add(key_oven, key_telec, key_bliznecy, key_rak, key_lev, key_deva, key_vesy, key_scorpion, key_strelec, key_kozerog, key_vodoley, key_ryby)
        bot.send_message(call.from_user.id, "Выбери свой знак зодиака", reply_markup=keyboard)
    elif call.data == "lev":
        msg = 'Львам ' + '♌' + ' сегодня звезды предвещают ' + random.choice(first) + ' Но сегодня львам ' + random.choice(second) + ' ' + random.choice(second_add) + ' Львы' + 'помните, что сегодня ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)
        keyboard.add(key_oven, key_telec, key_bliznecy, key_rak, key_lev, key_deva, key_vesy, key_scorpion, key_strelec, key_kozerog, key_vodoley, key_ryby)
        bot.send_message(call.from_user.id, "Выбери свой знак зодиака", reply_markup=keyboard)
    elif call.data == "deva":
        msg = 'Девам ' + '♍' + ' сегодня звезды предвещают ' + random.choice(first) + ' Но сегодня девам ' + random.choice(second) + ' ' + random.choice(second_add) + ' Девы' + 'помните, что сегодня ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)
        keyboard.add(key_oven, key_telec, key_bliznecy, key_rak, key_lev, key_deva, key_vesy, key_scorpion, key_strelec, key_kozerog, key_vodoley, key_ryby)
        bot.send_message(call.from_user.id, "Выбери свой знак зодиака", reply_markup=keyboard)
    elif call.data == "vesy":
        msg = 'Весам ' + '♎' + ' сегодня звезды предвещают ' + random.choice(first) + ' Но сегодня весам ' + random.choice(second) + ' ' + random.choice(second_add) + ' Весы' + 'помните, что сегодня ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)
        keyboard.add(key_oven, key_telec, key_bliznecy, key_rak, key_lev, key_deva, key_vesy, key_scorpion, key_strelec, key_kozerog, key_vodoley, key_ryby)
        bot.send_message(call.from_user.id, "Выбери свой знак зодиака", reply_markup=keyboard)
    elif call.data == "scorpion":
        msg = 'Скорпионам ' + '♏' + ' сегодня звезды предвещают ' + random.choice(first) + ' Но сегодня скорпионам ' + random.choice(second) + ' ' + random.choice(second_add) + ' Скорпионы' + 'помните, что сегодня ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)
        keyboard.add(key_oven, key_telec, key_bliznecy, key_rak, key_lev, key_deva, key_vesy, key_scorpion, key_strelec, key_kozerog, key_vodoley, key_ryby)
        bot.send_message(call.from_user.id, "Выбери свой знак зодиака", reply_markup=keyboard)
    elif call.data == "strelec":
        msg = 'Стрельцам' + '♐' + ' сегодня звезды предвещают ' + random.choice(first) + ' Но сегодня стрельцам ' + random.choice(second) + ' ' + random.choice(second_add) + ' Стрельцы' + 'помните, что сегодня ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)
        keyboard.add(key_oven, key_telec, key_bliznecy, key_rak, key_lev, key_deva, key_vesy, key_scorpion, key_strelec, key_kozerog, key_vodoley, key_ryby)
        bot.send_message(call.from_user.id, "Выбери свой знак зодиака", reply_markup=keyboard)
    elif call.data == "kozerog":
        msg = 'Козерогам' + '♑' + ' сегодня звезды предвещают ' + random.choice(first) + ' Но сегодня козерогам ' + random.choice(second) + ' ' + random.choice(second_add) + ' Козероги' + 'помните, что сегодня ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)
        keyboard.add(key_oven, key_telec, key_bliznecy, key_rak, key_lev, key_deva, key_vesy, key_scorpion, key_strelec, key_kozerog, key_vodoley, key_ryby)
        bot.send_message(call.from_user.id, "Выбери свой знак зодиака", reply_markup=keyboard)
    elif call.data == "vodoley":
        msg = 'Водолеям' + '♒' + ' сегодня звезды предвещают ' + random.choice(first) + ' Но сегодня водолеям ' + random.choice(second) + ' ' + random.choice(second_add) + ' Водолеи' + 'помните, что сегодня ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)
        keyboard.add(key_oven, key_telec, key_bliznecy, key_rak, key_lev, key_deva, key_vesy, key_scorpion, key_strelec, key_kozerog, key_vodoley, key_ryby)
        bot.send_message(call.from_user.id, "Выбери свой знак зодиака", reply_markup=keyboard)
    elif call.data == "ryby":
        msg = 'Рыбам' + '♓' + ' сегодня звезды предвещают ' + random.choice(first) + ' Но сегодня рыбам ' + random.choice(second) + ' ' + random.choice(second_add) + ' Рыбы' + 'помните, что сегодня ' + random.choice(third)
        bot.send_message(call.message.chat.id, msg)
        keyboard.add(key_oven, key_telec, key_bliznecy, key_rak, key_lev, key_deva, key_vesy, key_scorpion, key_strelec, key_kozerog, key_vodoley, key_ryby)
        bot.send_message(call.from_user.id, "Выбери свой знак зодиака", reply_markup=keyboard)



bot.polling(none_stop=True, interval=0)