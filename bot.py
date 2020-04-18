import telebot
import time
import logging
import telegram
from telebot import types
from telegram import ChatAction
from functools import wraps
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, RegexHandler
bot = telebot.TeleBot('979702529:AAH4qmbfJ-ayV4fzWTgdD53ghpHjsAXysTs')
#C:\Users\Hirata\Desktop\bot.py\bot.py
#cd C:\Users\Hirata\Desktop\bot.py
#git commit -am "make it better"
#git push heroku master
#heroku ps:scale worker=1
#BOT version 0.1.5.(219)
#BOT version 0.1.6.(608)
#BOT version 0.1.7.(587)

@bot.message_handler(content_types=['text'])
#TRAINING
def register(message):
    if message.text == '/reg' or '/start':
        bot.send_message(message.from_user.id,'Выбери свой пол', reply_markup=keyboard1)
        bot.register_next_step_handler(message, get_sex)
    elif message.text == '/eat':
        bot.send_message(message.from_user.id,'Сколько ты в высоту в сантиметрах?')
        bot.register_next_step_handler(message, get_height)
    else:
        bot.send_message(message.from_user.id,'Привет, я помогу тебе составить программу тренировок подходящую тебе, если готов, тыкни /reg. Если нужна программа питания, тыкни /eat.', reply_markup=keyboard7)

def get_sex(message):
    global sex
    sex = message.text
    bot.send_message(message.from_user.id, 'Твоя цель?', reply_markup=keyboard2)
    bot.register_next_step_handler(message, get_aim)

def get_aim(message):
    global aim
    aim = message.text
    bot.send_message(message.from_user.id,'Где ты будешь тренироваться?', reply_markup=keyboard3)
    bot.register_next_step_handler(message, get_placing)

def get_placing(message):
    global placing
    placing = message.text
    bot.send_message(message.from_user.id,'Сколько раз в неделю ты планируешь тренироваться?', reply_markup=keyboard8)
    bot.register_next_step_handler(message, get_time)

def get_time(message):
    global time
    time = message.text
    question = 'Вот что я запомнил: Ты '+sex+', наша цель '+aim+', занятия '+time+' в неделю будут проходить '+placing+', все верно? А если ошибся то тыкни /reg'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard9)
    bot.register_next_step_handler(message, final_training)

#__________________ВЫВОД ТРЕНИРОВКИ__________________#
def final_training(message):
    if sex == 'парень' and aim == 'подсушиться' and placing == 'в зале' and time == '1 раз': #1.1#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n1) '+a+' \n\n2) '+b+'\n'+time20+' \n\n3) '+c+'\n'+up15f20+' \
        \n\n4) '+d+'\n'+up15f20+' \n\n5) '+e+'\n'+up15f20+' \n\n6) '+f+'\n'+up15f20+' \
        \n\n7) '+g+'\n'+up15f20+' \n\n8) '+h+'\n'+up15f20+' \n\n9) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'держать форму' and placing == 'в зале' and time == '1 раз': #1.2#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n1) '+a+' \n\n2) '+b+'\n'+time10+' \n\n3) '+c+'\n'+up10f12+' \
        \n\n4) '+d+'\n'+up10f12+' \n\n5) '+e+'\n'+up10f12+' \n\n6) '+f+'\n'+up10f12+' \
        \n\n7) '+g+'\n'+up10f12+' \n\n8) '+h+'\n'+up10f12+' \n\n9) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'подкачаться' and placing == 'в зале' and time == '1 раз': #1.3#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n1) '+a+' \n\n2) '+b+'\n'+time5+' \n\n3) '+c+'\n'+up8f10+' \
        \n\n4) '+d+'\n'+up8f10+' \n\n5) '+e+'\n'+up8f10+' \n\n6) '+f+'\n'+up8f10+' \
        \n\n7) '+g+'\n'+up8f10+' \n\n8) '+h+'\n'+up8f10+' \n\n9) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')

############################################################################################################################

    elif sex == 'парень' and aim == 'подсушиться' and placing == 'дома' and time == '1 раз': #2.1#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time20+' \n\n3) '+bb+'\n'+up15f20+' \
        \n\n4) '+eee+'\n'+up15f20+' \n\n5) '+cc+'\n'+up15f20+' \n\n6) '+aaa+'\n'+up15f20+' \
        \n\n7) '+ee+'\n'+up15f20+' \n\n8) '+ff+'\n'+up15f20+' \n\n9) '+gg+'\n'+up15f20+' \n\n10) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'держать форму' and placing == 'дома' and time == '1 раз': #2.2#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time10+' \n\n3) '+bb+'\n'+up10f12+' \
        \n\n4) '+eee+'\n'+up10f12+' \n\n5) '+cc+'\n'+up10f12+' \n\n6) '+aaa+'\n'+up10f12+' \
        \n\n7) '+ee+'\n'+up10f12+' \n\n8) '+ff+'\n'+up10f12+' \n\n9) '+gg+'\n'+up10f12+' \n\n10) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'подкачаться' and placing == 'дома' and time == '1 раз': #2.3#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time5+' \n\n3) '+bb+'\n'+up8f10+' \
        \n\n4) '+eee+'\n'+up8f10+' \n\n5) '+cc+'\n'+up8f10+' \n\n6) '+aaa+'\n'+up8f10+' \
        \n\n7) '+ee+'\n'+up8f10+' \n\n8) '+ff+'\n'+up8f10+' \n\n9) '+gg+'\n'+up8f10+' \n\n10) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')

############################################################################################################################

    elif sex == 'парень' and aim == 'подсушиться' and placing == 'в воркаут зоне' and time == '1 раз': #3.1#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time20+' \n\n3) '+bb+'\n'+up15f20+' \
        \n\n4) '+hh+'\n'+up15f20+' \n\n5) '+h+'\n'+up15f20+' \n\n6) '+aaa+'\n'+up15f20+' \
        \n\n7) '+bbb+'\n'+up15f20+' \n\n8) '+ccc+'\n'+up15f20+' \n\n9) '+c+'\n'+up15f20+' \n\n10) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'держать форму' and placing == 'в воркаут зоне' and time == '1 раз': #3.2#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time10+' \n\n3) '+bb+'\n'+up10f12+' \
        \n\n4) '+hh+'\n'+up10f12+' \n\n5) '+h+'\n'+up10f12+' \n\n6) '+aaa+'\n'+up10f12+' \
        \n\n7) '+bbb+'\n'+up10f12+' \n\n8) '+ccc+'\n'+up10f12+' \n\n9) '+c+'\n'+up10f12+' \n\n10) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'подкачаться' and placing == 'в воркаут зоне' and time == '1 раз': #3.3#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time5+' \n\n3) '+bb+'\n'+up8f10+' \
        \n\n4) '+hh+'\n'+up8f10+' \n\n5) '+h+'\n'+up8f10+' \n\n6) '+aaa+'\n'+up8f10+' \
        \n\n7) '+bbb+'\n'+up8f10+' \n\n8) '+ccc+'\n'+up8f10+' \n\n9) '+c+'\n'+up8f10+' \n\n10) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')

############################################################################################################################

    elif sex == 'парень' and aim == 'подсушиться' and placing == 'в зале' and time == '2 раза': #4.1 ДВА ДНЯ#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+b+'\n'+time20+' \n\n3) '+c+'\n'+up15f20+' \
        \n\n4) '+eee+'\n'+up15f20+' \n\n5) '+ggg+'\n'+up15f20+' \n\n6) '+hhh+'\n'+up15f20+' \
        \n\n7) '+iii+'\n'+up15f20+' \n\n8) '+ii+'\n'+up15f20+' \n\n9) '+jjj+'\n'+up15f20+' \n\n10) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+kkk+'\n'+time20+' \n\n3) '+c+'\n'+up15f20+' \
        \n\n4) '+f+'\n'+up15f20+' \n\n5) '+lll+'\n'+up15f20+' \n\n6) '+mmm+'\n'+up15f20+' \
        \n\n7) '+nnn+'\n'+up15f20+' \n\n8) '+ooo+'\n'+up15f20+' \n\n9) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'держать форму' and placing == 'в зале' and time == '2 раза': #4.2 ДВА ДНЯ#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+b+'\n'+time10+' \n\n3) '+c+'\n'+up10f12+' \
        \n\n4) '+eee+'\n'+up10f12+' \n\n5) '+ggg+'\n'+up10f12+' \n\n6) '+hhh+'\n'+up10f12+' \
        \n\n7) '+iii+'\n'+up10f12+' \n\n8) '+ii+'\n'+up10f12+' \n\n9) '+jjj+'\n'+up10f12+' \n\n10) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+kkk+'\n'+time10+' \n\n3) '+c+'\n'+up10f12+' \
        \n\n4) '+f+'\n'+up10f12+' \n\n5) '+lll+'\n'+up10f12+' \n\n6) '+mmm+'\n'+up10f12+' \
        \n\n7) '+nnn+'\n'+up10f12+' \n\n8) '+ooo+'\n'+up10f12+' \n\n9) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'подкачаться' and placing == 'в зале' and time == '2 раза': #4.3 ДВА ДНЯ#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+b+'\n'+time5+' \n\n3) '+c+'\n'+up8f10+' \
        \n\n4) '+eee+'\n'+up8f10+' \n\n5) '+ggg+'\n'+up8f10+' \n\n6) '+hhh+'\n'+up8f10+' \
        \n\n7) '+iii+'\n'+up8f10+' \n\n8) '+ii+'\n'+up8f10+' \n\n9) '+jjj+'\n'+up8f10+' \n\n10) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+kkk+'\n'+time5+' \n\n3) '+c+'\n'+up8f10+' \
        \n\n4) '+f+'\n'+up8f10+' \n\n5) '+lll+'\n'+up8f10+' \n\n6) '+mmm+'\n'+up8f10+' \
        \n\n7) '+nnn+'\n'+up8f10+' \n\n8) '+ooo+'\n'+up8f10+' \n\n9) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')

############################################################################################################################

    elif sex == 'парень' and aim == 'подсушиться' and placing == 'дома' and time == '2 раза': #5.1 ДВА ДНЯ#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time20+' \n\n3) '+c+'\n'+up15f20+' \
        \n\n4) '+eee+'\n'+up15f20+' \n\n5) '+ee+'\n'+up15f20+' \n\n6) '+ddd+'\n'+up15f20+' \
        \n\n7) '+ppp+'\n'+up15f20+' \n\n8) '+qqq+'\n'+up15f20+' \n\n9) '+rrr+'\n'+up15f20+' \n\n10) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time20+' \n\n3) '+sss+'\n'+up15f20+' \
        \n\n4) '+dd+'\n'+up15f20+' \n\n5) '+aab+'\n'+up15f20+' \n\n6) '+ff+'\n'+up15f20+' \
        \n\n7) '+aac+'\n'+up15f20+' \n\n8) '+aad+'\n'+up15f20+' \n\n9) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'держать форму' and placing == 'дома' and time == '2 раза': #5.2 ДВА ДНЯ
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time10+' \n\n3) '+c+'\n'+up10f12+' \
        \n\n4) '+eee+'\n'+up10f12+' \n\n5) '+ee+'\n'+up10f12+' \n\n6) '+ddd+'\n'+up10f12+' \
        \n\n7) '+ppp+'\n'+up10f12+' \n\n8) '+qqq+'\n'+up10f12+' \n\n9) '+rrr+'\n'+up10f12+' \n\n10) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time10+' \n\n3) '+sss+'\n'+up10f12+' \
        \n\n4) '+dd+'\n'+up10f12+' \n\n5) '+aab+'\n'+up10f12+' \n\n6) '+ff+'\n'+up10f12+' \
        \n\n7) '+aac+'\n'+up10f12+' \n\n8) '+aad+'\n'+up10f12+' \n\n9) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'подкачаться' and placing == 'дома' and time == '2 раза': #5.3 ДВА ДНЯ
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time5+' \n\n3) '+c+'\n'+up8f10+' \
        \n\n4) '+eee+'\n'+up8f10+' \n\n5) '+ee+'\n'+up8f10+' \n\n6) '+ddd+'\n'+up8f10+' \
        \n\n7) '+ppp+'\n'+up8f10+' \n\n8) '+qqq+'\n'+up8f10+' \n\n9) '+rrr+'\n'+up8f10+' \n\n10) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time5+' \n\n3) '+sss+'\n'+up8f10+' \
        \n\n4) '+dd+'\n'+up8f10+' \n\n5) '+aab+'\n'+up8f10+' \n\n6) '+ff+'\n'+up8f10+' \
        \n\n7) '+aac+'\n'+up8f10+' \n\n8) '+aad+'\n'+up8f10+' \n\n9) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')

#########################################################################################################################

    elif sex == 'парень' and aim == 'подсушиться' and placing == 'в воркаут зоне' and time == '2 раза': #6.1 ДВА ДНЯ#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time20+' \n\n3) '+hh+'\n'+up15f20+' \
        \n\n4) '+h+'\n'+up15f20+' \n\n5) '+aae+'\n'+up15f20+' \n\n6) '+qqq+'\n'+up15f20+' \
        \n\n7) '+rrr+'\n'+up15f20+' \n\n8) '+ppp+'\n'+up15f20+' \n\n9) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time20+' \n\n3) '+bb+'\n'+up15f20+' \
        \n\n4) '+sss+'\n'+up15f20+' \n\n5) '+aaa+'\n'+up15f20+' \n\n6) '+bbb+'\n'+up15f20+' \
        \n\n7) '+aab+'\n'+up15f20+' \n\n8) '+aac+'\n'+up15f20+' \n\n9) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'держать форму' and placing == 'в воркаут зоне' and time == '2 раза': #6.2 ДВА ДНЯ#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time10+' \n\n3) '+hh+'\n'+up10f12+' \
        \n\n4) '+ii+'\n'+up10f12+' \n\n5) '+aae+'\n'+up10f12+' \n\n6) '+qqq+'\n'+up10f12+' \
        \n\n7) '+rrr+'\n'+up10f12+' \n\n8) '+ppp+'\n'+up10f12+' \n\n9) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time20+' \n\n3) '+bb+'\n'+up10f12+' \
        \n\n4) '+sss+'\n'+up10f12+' \n\n5) '+aaa+'\n'+up10f12+' \n\n6) '+bbb+'\n'+up10f12+' \
        \n\n7) '+aab+'\n'+up10f12+' \n\n8) '+aac+'\n'+up10f12+' \n\n9) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'подкачаться' and placing == 'в воркаут зоне' and time == '2 раза': #6.3 ДВА ДНЯ#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time5+' \n\n3) '+hh+'\n'+up8f10+' \
        \n\n4) '+ii+'\n'+up8f10+' \n\n5) '+aae+'\n'+up8f10+' \n\n6) '+qqq+'\n'+up8f10+' \
        \n\n7) '+rrr+'\n'+up8f10+' \n\n8) '+ppp+'\n'+up8f10+' \n\n9) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time5+' \n\n3) '+bb+'\n'+up8f10+' \
        \n\n4) '+sss+'\n'+up8f10+' \n\n5) '+aaa+'\n'+up8f10+' \n\n6) '+bbb+'\n'+up8f10+' \
        \n\n7) '+aab+'\n'+up8f10+' \n\n8) '+aac+'\n'+up8f10+' \n\n9) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')

#########################################################################################################################

    elif sex == 'парень' and aim == 'подсушиться' and placing == 'в зале' and time == '3 раза': #7.1 ТРИ ДНЯ#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+b+'\n'+time20+' \n\n3) '+f+'\n'+up15f20+' \
        \n\n4) '+aag+'\n'+up15f20+' \n\n5) '+nnn+'\n'+up15f20+' \n\n6) '+mmm+'\n'+up15f20+' \
        \n\n7) '+aah+'\n'+up15f20+' \n\n8) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+b+'\n'+time20+' \n\n3) '+ggg+'\n'+up15f20+' \
        \n\n4) '+iii+'\n'+up15f20+' \n\n5) '+jjj+'\n'+up15f20+' \n\n6) '+aaf+'\n'+up15f20+' \
        \n\n7) '+ooo+'\n'+up15f20+' \n\n8) '+i+'\
        \n\n---3-ий день--- \
        \n\n1) '+a+' \n\n2) '+b+'\n'+time20+' \n\n3) '+hhh+'\n'+up15f20+' \
        \n\n4) '+ddd+'\n'+up15f20+' \n\n5) '+aai+'\n'+up15f20+' \n\n6) '+aaj+'\n'+up15f20+' \
        \n\n7) '+aak+'\n'+up15f20+' \n\n8) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'держать форму' and placing == 'в зале' and time == '3 раза': #7.2 ТРИ ДНЯ#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+b+'\n'+time10+' \n\n3) '+f+'\n'+up10f12+' \
        \n\n4) '+aag+'\n'+up10f12+' \n\n5) '+nnn+'\n'+up10f12+' \n\n6) '+mmm+'\n'+up10f12+' \
        \n\n7) '+aah+'\n'+up10f12+' \n\n8) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+b+'\n'+time10+' \n\n3) '+ggg+'\n'+up10f12+' \
        \n\n4) '+iii+'\n'+up10f12+' \n\n5) '+jjj+'\n'+up10f12+' \n\n6) '+aaf+'\n'+up10f12+' \
        \n\n7) '+ooo+'\n'+up10f12+' \n\n8) '+i+'\
        \n\n---3-ий день--- \
        \n\n1) '+a+' \n\n2) '+b+'\n'+time10+' \n\n3) '+hhh+'\n'+up10f12+' \
        \n\n4) '+ddd+'\n'+up10f12+' \n\n5) '+aai+'\n'+up10f12+' \n\n6) '+aaj+'\n'+up10f12+' \
        \n\n7) '+aak+'\n'+up10f12+' \n\n8) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'подкачаться' and placing == 'в зале' and time == '3 раза': #7.3 ТРИ ДНЯ#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+b+'\n'+time5+' \n\n3) '+f+'\n'+up8f10+' \
        \n\n4) '+aag+'\n'+up8f10+' \n\n5) '+nnn+'\n'+up8f10+' \n\n6) '+mmm+'\n'+up8f10+' \
        \n\n7) '+aah+'\n'+up8f10+' \n\n8) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+b+'\n'+time5+' \n\n3) '+ggg+'\n'+up8f10+' \
        \n\n4) '+iii+'\n'+up8f10+' \n\n5) '+jjj+'\n'+up8f10+' \n\n6) '+aaf+'\n'+up8f10+' \
        \n\n7) '+ooo+'\n'+up8f10+' \n\n8) '+i+'\
        \n\n---3-ий день--- \
        \n\n1) '+a+' \n\n2) '+b+'\n'+time5+' \n\n3) '+hhh+'\n'+up8f10+' \
        \n\n4) '+ddd+'\n'+up8f10+' \n\n5) '+aai+'\n'+up8f10+' \n\n6) '+aaj+'\n'+up8f10+' \
        \n\n7) '+aak+'\n'+up8f10+' \n\n8) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')

#########################################################################################################################

    elif sex == 'парень' and aim == 'подсушиться' and placing == 'дома' and time == '3 раза': #8.1 ТРИ ДНЯ#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time20+' \n\n3) '+dd+'\n'+up15f20+' \
        \n\n4) '+aab+'\n'+up15f20+' \n\n5) '+ff+'\n'+up15f20+' \n\n6) '+aac+'\n'+up15f20+' \
        \n\n7) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time20+' \n\n3) '+bb+'\n'+up15f20+' \
        \n\n4) '+c+'\n'+up15f20+' \n\n5) '+gg+'\n'+up15f20+' \n\n6) '+eee+'\n'+up15f20+' \
        \n\n7) '+ee+'\n'+up15f20+' \n\n8) '+aal+'\n'+up15f20+' \n\n9) '+i+'\
        \n\n---3-ий день--- \
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time20+' \n\n3) '+cc+'\n'+up15f20+' \
        \n\n4) '+ccc+'\n'+up15f20+' \n\n5) '+rrr+'\n'+up15f20+' \n\n6) '+qqq+'\n'+up15f20+' \
        \n\n7) '+ddd+'\n'+up15f20+' \n\n8) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'держать форму' and placing == 'дома' and time == '3 раза': #8.2 ТРИ ДНЯ#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time10+' \n\n3) '+dd+'\n'+up10f12+' \
        \n\n4) '+aab+'\n'+up10f12+' \n\n5) '+ff+'\n'+up10f12+' \n\n6) '+aac+'\n'+up10f12+' \
        \n\n7) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time10+' \n\n3) '+bb+'\n'+up10f12+' \
        \n\n4) '+c+'\n'+up10f12+' \n\n5) '+gg+'\n'+up10f12+' \n\n6) '+eee+'\n'+up10f12+' \
        \n\n7) '+ee+'\n'+up10f12+' \n\n8) '+aal+'\n'+up10f12+' \n\n9) '+i+'\
        \n\n---3-ий день--- \
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time10+' \n\n3) '+cc+'\n'+up10f12+' \
        \n\n4) '+ccc+'\n'+up10f12+' \n\n5) '+rrr+'\n'+up10f12+' \n\n6) '+qqq+'\n'+up10f12+' \
        \n\n7) '+ddd+'\n'+up10f12+' \n\n8) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'подкачаться' and placing == 'дома' and time == '3 раза': #8.3 ТРИ ДНЯ#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time5+' \n\n3) '+dd+'\n'+up8f10+' \
        \n\n4) '+aab+'\n'+up8f10+' \n\n5) '+ff+'\n'+up8f10+' \n\n6) '+aac+'\n'+up8f10+' \
        \n\n7) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time5+' \n\n3) '+bb+'\n'+up8f10+' \
        \n\n4) '+c+'\n'+up8f10+' \n\n5) '+gg+'\n'+up8f10+' \n\n6) '+eee+'\n'+up8f10+' \
        \n\n7) '+ee+'\n'+up8f10+' \n\n8) '+aal+'\n'+up8f10+' \n\n9) '+i+'\
        \n\n---3-ий день--- \
        \n\n1) '+a+' \n\n2) '+aa+'\n'+time5+' \n\n3) '+cc+'\n'+up8f10+' \
        \n\n4) '+ccc+'\n'+up8f10+' \n\n5) '+rrr+'\n'+up8f10+' \n\n6) '+qqq+'\n'+up8f10+' \
        \n\n7) '+ddd+'\n'+up8f10+' \n\n8) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')

#########################################################################################################################

    elif sex == 'парень' and aim == 'подсушиться' and placing == 'в воркаут зоне' and time == '3 раза': #9.1 ТРИ ДНЯ#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time20+' \n\n3) '+aaa+'\n'+up15f20+' \
        \n\n4) '+aab+'\n'+up15f20+' \n\n5) '+bbb+'\n'+up15f20+' \n\n6) '+aac+'\n'+up15f20+' \
        \n\n7) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time20+' \n\n3) '+hh+'\n'+up15f20+' \
        \n\n4) '+ii+'\n'+up15f20+' \n\n5) '+aae+'\n'+up15f20+' \n\n6) '+aak+'\n'+up15f20+' \
        \n\n7) '+aam+'\n'+up15f20+' \n\n8) '+i+'\
        \n\n---3-ий день--- \
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time20+' \n\n3) '+cc+'\n'+up15f20+' \
        \n\n4) '+ccc+'\n'+up15f20+' \n\n5) '+rrr+'\n'+up15f20+' \n\n6) '+qqq+'\n'+up15f20+' \
        \n\n7) '+ddd+'\n'+up15f20+' \n\n8) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'держать форму' and placing == 'в воркаут зоне' and time == '3 раза': #9.2 ТРИ ДНЯ#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time10+' \n\n3) '+aaa+'\n'+up10f12+' \
        \n\n4) '+aab+'\n'+up10f12+' \n\n5) '+bbb+'\n'+up10f12+' \n\n6) '+aac+'\n'+up10f12+' \
        \n\n7) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time10+' \n\n3) '+hh+'\n'+up10f12+' \
        \n\n4) '+ii+'\n'+up10f12+' \n\n5) '+aae+'\n'+up10f12+' \n\n6) '+aak+'\n'+up10f12+' \
        \n\n7) '+ee+'\n'+up10f12+' \n\n8) '+i+'\
        \n\n---3-ий день--- \
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time10+' \n\n3) '+cc+'\n'+up10f12+' \
        \n\n4) '+ccc+'\n'+up10f12+' \n\n5) '+rrr+'\n'+up10f12+' \n\n6) '+qqq+'\n'+up10f12+' \
        \n\n7) '+aam+'\n'+up10f12+' \n\n8) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')
    elif sex == 'парень' and aim == 'подкачаться' and placing == 'в воркаут зоне' and time == '3 раза': #9.3 ТРИ ДНЯ#
        bot.send_message(
        message.from_user.id,'Ваша программа готова! Выполняйте '+time+' в неделю следующую тренировку:\
        \n\n---1-ый день--- \
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time20+' \n\n3) '+aaa+'\n'+up8f10+' \
        \n\n4) '+aab+'\n'+up8f10+' \n\n5) '+bbb+'\n'+up8f10+' \n\n6) '+aac+'\n'+up8f10+' \
        \n\n7) '+i+'\
        \n\n---2-ой день--- \
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time20+' \n\n3) '+hh+'\n'+up8f10+' \
        \n\n4) '+ii+'\n'+up8f10+' \n\n5) '+aae+'\n'+up8f10+' \n\n6) '+aak+'\n'+up8f10+' \
        \n\n7) '+ee+'\n'+up8f10+' \n\n8) '+i+'\
        \n\n---3-ий день--- \
        \n\n1) '+a+' \n\n2) '+fff+'\n'+time20+' \n\n3) '+cc+'\n'+up8f10+' \
        \n\n4) '+ccc+'\n'+up8f10+' \n\n5) '+rrr+'\n'+up8f10+' \n\n6) '+qqq+'\n'+up8f10+' \
        \n\n7) '+aam+'\n'+up8f10+' \n\n8) '+i+'\n'
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')




#EAT добавить возраст
def get_height(message):
    global height
    height = message.text
    bot.send_message(message.from_user.id,'Твой вес в килограммах?')
    bot.register_next_step_handler(message, get_weight)

def get_weight(message):
    global weight
    height = message.text
    bot.send_message(message.from_user.id,'Вопрос про активность???????',reply_markup=keyboard6)
    bot.register_next_step_handler(message, get_activity)

def get_activity(message):
    global activity
    activity = message.text
    question1 = 'Твой рост '+str(height)+', по весу'+str(weight)+', тебе '+str(age)+', а по активности '+activity+'.'
    bot.send_message(message.from_user.id, text=question1)
    bot.register_next_step_handler(message, final_eat)

def final_eat(message):
    if 0<height<150 and 0<weight<40 and activity == 'активность 1': #1
        bot.send_message(
        message.from_user.id,'Ваша программа питания готова! Вот Ваш рацион:\
        \n\n1) '+a+' \n\n2) '+b+'\n'+time20+' \n\n3) '+c+'\n'+up15f20+' \n\n4) '+d+'\n'+up15f20+' \n\n5) '+e+'\n'+up15f20+' \n\n6) '+f+'\n'+up15f20+' \n\n7) '+g+'\n'+up15f20+' \n\n8) '+h+'\n'+up15f20+' \n\n9) '+i+'\n'+time20+''
        )
        bot.send_message(message.from_user.id,'Если хочешь получить программу питания, тыкни /eat')






#    bot.send_message(message.from_user.id, 'кек')
#    keyboard = types.InlineKeyboardMarkup()
#    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
#    keyboard.add(key_yes)
#    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
#    keyboard.add(key_no)

@bot.callback_query_handler(func=lambda call: True) #TRAINING
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запомню! Если хочешь составить твой план питания, тыкни /eat')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Где-то ошибся? Давай по-новой! Тыкни /reg')

#GLOBALS
name = ''
sex = ''
age = 0
aim = ''
placing = ''
bulk = ''
health = ''
time = ''
height = '' #eat
weight = ''
activity = ''

#ARRAYS
a='Разминка '
b='Бег на беговой дорожке'
c='Скручивания на скамье'
d='Гиперэкстензия'
e='Присед со штангой'
f='Жим лежа'
g='Тяга верхнего блока'
h='Подтягивания обратным хватом'
i='Растяжка'
aa='Бег по леснице'
bb='Берпи'
cc='Приседания'
dd='Отжимания'
ee='Охотничья собака'
ff='Обратные отжимания от стула'
gg='Велосипед'
hh='Подтягивание'
ii=''
aaa='Отжимания'
bbb='Отжимания на брусьях'
ccc='Приседания с выпрыгиванием'
ddd='Подъемы на носки с возвышением'
eee='Гиперэкстензия'
fff='Бег по улице'
ggg='Становая тяга'
hhh='Приседания со штангой'
iii='Тяга верхнего блока'
jjj='Тяга Т-грифа'
kkk='Эллипсоид'
lll='Сведение рук в бабочке'
mmm='Армейский жим в тренажере'
nnn='Французский жим'
ooo='Сгибание рук с гантелями со ступинацией'
ppp='Приседания с выпрыгиванием'
qqq='Выпады вперед'
rrr='Стульчик'
sss='Книжка'
aab='Треугольные отжимания'
aac='Отжимания уголком'
aad='Поднятие тяжести перед собой'
aae='Горизонтальные подтягивания'
aaf='Сгибание рук со штангой'
aag='Жим лежа узким хватом'
aah='Тяна штанги к груди стоя'
aai='Разгибание ног в тренажере'
aaj='Cгибание ног в тренажере'
aak='Скручивание на скамье'
aal='Уголок'
aam='Подъем ног в висе'
aan=''
aao=''
aap=''
aaq=''
aar=''
aas=''

time5='5 минут'
time10='10 минут'
time20='20 минут'

up15f20='4 подхода по 15-20 раз'
up10f12='4 подхода по 10-12 раз'
up8f10='4 подхода по 8-10 раз'


#KEYBOARDS
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.add('парень', 'девушка')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.add('подсушиться', 'подкачаться', 'держать форму')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.add('в зале', 'в воркаут зоне', 'дома')
keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.add('эктоморф', 'мезоморф', 'эндоморф')
keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard5.add('проблема 1', 'проблема 2', 'все в порядке')
keyboard6 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard6.add('активность 1', 'активность 2', 'активность 3')
keyboard7 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard7.add('/reg', '/start')
keyboard8 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard8.add('1 раз', '2 раза', '3 раза')
keyboard9 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard9.add('Да')

bot.polling(none_stop=True, interval=0)

#ЗАГОТОВОЧКИ


#C:\Users\Hirata\Desktop\bot.py\bot.py
