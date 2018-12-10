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

#módulo de expressões regulares
import re

#módulos do phantomjs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#módulo para tratar imagem
from PIL import Image

#módulo para checar se arquivo existe
import os.path

#módulos de data e hora
#import time
#import datetime

#-------------------------------------------------------------

#-------------------------------------------------------------
# criando o updater e dispatcher para o BOT
#-------------------------------------------------------------
updater = Updater(token="719504886:AAHzJ4TdB51DgLwzxExc7ws8jtS0j5PDUQ4")
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

<i>Telegram Bot Abelão
Criado por Fábio Berbert de Paula ( @vivaolinux )
Powered by Python 3.x</i>
"""

    bot.send_message(chat_id=update.message.chat_id, parse_mode="HTML", text=html)



def quote():
    """
    Envia uma frase de efeito do Abel
    """

    #importar classe Quotes, arquivo com todas as frases do Yoda
    from Quotes import Quotes
    quotes = Quotes()

    return quotes.quote()


def echo (bot, update):
    """
    Recursos de iteração do Yoda nos canais de chat
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


    #bot.send_message(chat_id=chat_id, text="test: " + name)

    try:

        msg = update.message.text.upper()

        if "ABEL" in msg:
            bot.send_message(chat_id=chat_id, text=quote())

        regjoy = [ re.compile("KKK"), re.compile("HAHAHA"), re.compile("HUAHUA") ]
        if any(regex.search(msg) for regex in regjoy):
            out = emojize(":joy::joy::joy:", use_aliases=True)
            #bot.send_message(chat_id=chat_id, text=out)

        regrage = [ re.compile("PQP"), re.compile("CARALHO"), re.compile("VTNC"), re.compile("MERDA") ]
        if any(regex.search(msg) for regex in regrage):
            out = emojize(":rage:", use_aliases=True)
            bot.send_message(chat_id=chat_id, text=out)

        regrage = [ re.compile("Gum"), re.compile("GUM") ]
        if any(regex.search(msg) for regex in regrage):
            out = "Gum é um zagueiro extraordinário, um dos melhores que vi jogar!"
            bot.send_message(chat_id=chat_id, text=out)

        regrage = [ re.compile("Pedro"), re.compile("pedro") ]
        if any(regex.search(msg) for regex in regrage):
            out = "Sempre falei que Pedro era melhor que 90% dos atacantes do Brasil"
            bot.send_message(chat_id=chat_id, text=out)

        regrage = [ re.compile("MJ") ]
        if any(regex.search(msg) for regex in regrage):
            out = "Marco Junior, que jogadoraço, que raça! Tenho orgulho desse ser humano"
            bot.send_message(chat_id=chat_id, text=out)

        regrage = [ re.compile("JC") ]
        if any(regex.search(msg) for regex in regrage):
            out = "JC, que goleiro! Estamos muito bem servidos na posição"
            bot.send_message(chat_id=chat_id, text=out)


        regcoffee = [ re.compile("CAFÉ"), re.compile("CAFE") ]
        if any(regex.search(msg) for regex in regcoffee):
            out = emojize(":coffee::coffee::coffee:", use_aliases=True)
            bot.send_message(chat_id=chat_id, text=out)

        regpump = [ re.compile("ALTA"), re.compile("PUMP") ]
        if any(regex.search(msg) for regex in regpump):
            out = emojize(":moneybag::moneybag::moneybag:", use_aliases=True)
            #bot.send_message(chat_id=chat_id, text=out)
    except:
        pass


    #verificar se o usuário possui username configurado
    #if not username:
        ##output = name + ": por favor, configure um username no Telegram!"
        #output = "Por favor " + name + ", configure um username no Telegram!\n\nNo aplicativo, clique em <strong>Configurações > Nome de usuário</strong>. Basta escolher um nome de sua preferência, ele será seu ID no Telegram, usado para entrarmos em contato contigo sem a necessidade de saber seu número de telefone."
        #bot.send_message(chat_id=chat_id, parse_mode='HTML', text=output)


def chatid(bot, update):
    """
    Retorna o chat_id do canal
    """

    bot.send_message(chat_id=update.message.chat_id, text=update.message.chat_id)

def repeat(bot, update):
    """
    Repetir o que você escreveu
    """

    output = update.message.text[8:]
    bot.send_message(chat_id=update.message.chat_id, parse_mode='HTML', text=output)

import random, string

def randomword(length):
    """
    Retorna uma palavra aleatória com <length> de tamanho
    """

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

#main block start
#
#

chatid_handler = CommandHandler('chatid', chatid)
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


