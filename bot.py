# -*- coding: utf-8 -*-
import redis
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['token']
#some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
#r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	print("welcome triggered")
	bot.reply_to(message, """\
Hi there, I am EchoBot.දචචඤ ගිසබය්ක්.. sinhala
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(content_types=['new_chat_participant'])
def user_greet(message):
	print("group welcome triggered")
	if message.new_chat_participant.id != bot.get_me().id:
		print("welcome triggered 2")
		name = message.new_chat_participant.first_name
		title = message.chat.title
		bot.send_message(message.chat.id, "Hey "+name+" \nWelcome to the group "+title+ " \n_Have fun & Enjoy!_")
		
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	print("echo_all triggered")
	bot.reply_to(message, message.text)

bot.polling()
