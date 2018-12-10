#!/usr/bin/env python3
"""
dilma.py

Bot Telegram

Métodos disponíveis:

"""

#-------------------------------------------------------------
# importar bibliotecas
#-------------------------------------------------------------

#módulo do telegram bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#módulo de log no console
import logging

#módulo de emojis
from emoji import emojize 

#expressões regulares
import re

#-------------------------------------------------------------
# criando o updater e dispatcher para o BOT
#-------------------------------------------------------------
mytoken = ''
try:
    from local_settings import *
except:
    pass

updater = Updater(token=mytoken)
job = updater.job_queue
dispatcher = updater.dispatcher

#ativando log de console, mudar para logging.DEBUG se quiser depurar
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#----------------------------------------------------------------
# SEÇÃO DE TRATADORES DE COMANDOS (command handlers)
#----------------------------------------------------------------

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Olá!")

def help(bot, update):
    """
    help
    """
    html = """
Digite:

/help - para obter ajuda

<strong>LISTA DE COMANDOS DO BOT</strong>

Under construction...

--

<i>Telegram Bot - Dilma Intelectual
Criado por Fábio Berbert de Paula ( @vivaolinux )
Powered by Python 3.x</i>
"""

    bot.send_message(chat_id=update.message.chat_id, parse_mode="HTML", text=html)


def quote():
    """
    Envia uma frase de efeito da Dilma
    """

    #importar classe Quotes, arquivo com todas as frases do Yoda
    from Quotes import Quotes
    #quotes = Quotes()

    return Quotes().quote()


def echo (bot, update):
    """
    Recursos de iteração da Dilma nos canais de chat
    """


    #definição de variáveis locais
    name = ""
    try:
        chat_id = update.message.chat_id
        username = update.message.from_user.username
        userid = update.message.from_user.id
        name = update.message.from_user.first_name
        surname = update.message.from_user.last_name
        if not surname:
            surname = ""
        name = name + " " + surname
    except:
        pass


    try:

        msg = update.message.text.upper()

        if "DILMA" in msg:
            bot.send_message(chat_id=chat_id, text=quote())

        regjoy = [ re.compile("KKK"), re.compile("HAHAHA"), re.compile("HUAHUA") ]
        if any(regex.search(msg) for regex in regjoy):
            out = emojize(":joy::joy::joy:", use_aliases=True)
            bot.send_message(chat_id=chat_id, text=out)

        regrage = [ re.compile("PQP"), re.compile("CARALHO"), re.compile("VTNC"), re.compile("MERDA") ]
        if any(regex.search(msg) for regex in regrage):
            out = emojize(":rage:", use_aliases=True)
            bot.send_message(chat_id=chat_id, text=out)

        regcoffee = [ re.compile("CAFÉ"), re.compile("CAFE") ]
        if any(regex.search(msg) for regex in regcoffee):
            out = emojize(":coffee::coffee::coffee:", use_aliases=True)
            bot.send_message(chat_id=chat_id, text=out)

    except:
        pass


def chatid(bot, update):
    """
    Retorna o chat_id do canal
    """

    bot.send_message(chat_id=update.message.chat_id, text=update.message.chat_id)

def calc(bot, update):
    """
    Retorna o resultado da equação
    """
    formula = update.message.text[6:]
    resp = eval(formula)

    resp = "Com minha precisão absoluta, lhes digo que " + formula + " equivale a:\n\n" + str(resp)
    bot.send_message(chat_id=update.message.chat_id, parse_mode='HTML', text=resp)

#main block start
#
#

chatid_handler = CommandHandler('chatid', chatid)
dispatcher.add_handler(chatid_handler)

chatid_handler = CommandHandler('calc', calc)
dispatcher.add_handler(chatid_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

echo_handler = MessageHandler(Filters.all, echo, pass_update_queue=False, pass_job_queue=False, pass_user_data=False, pass_chat_data=False, message_updates=True, channel_post_updates=True, edited_updates=False)
dispatcher.add_handler(echo_handler)

#starting the bot
try:
    updater.start_polling()
except:
    pass


