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
    bot.reply_to(message, """\
Hi there, I am EchoBot.දචචඤ ගිසබය්ක්.. sinhala
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(func=lambda message: True, content_types=['new_chat_member'])
def user_greet(message):
	if message.new_chat_member.id != bot.get_me().id:
		name = message.new_chat_member.first_name
		title = message.chat.title
		bot.send_message(message.chat.id, "Hey *{0}*! \n \nWelcome to the group *{1}* 😊 \n \n_Have fun & Enjoy!_"
.format(name,title), parse_mode='Markdown')
		
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
