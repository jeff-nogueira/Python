# -*- Coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

conv = ['oi','olá','tudo bem','Sim,e voce']

bot.set_trainer(ListTrainer)
bot.train(conv)

while True:
    quest = input('Voce:')

    response = bot.get_response(quest)
    print ('Bot:', response)
