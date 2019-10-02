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
tgadmin=385390931
@bot.message_handler(commands=['start'])
def send_welcome(message):
	print("welcome triggered")
	bot.reply_to(message, "*ආයුබෝවන් හැමෝටම! මම අලුතින් පැමිණෙන සාමාජිකයන් පිළිගැනීමට බැදී සිටිමි*",parse_mode='Markdown')
@bot.message_handler(commands=['UmU'])
def send_welcome(message):
	print("help triggered")
	gfromusr_id	= message.from_user.id
	gfromusr_fname = message.from_user.first_name
	try:
		gfromusr_lname = message.from_user.last_name
	except:
		gfromusr_lname = "  - "
	try:
		gfromusrname = message.from_user.username
	except:
		gfromusrname = " - "
	bot.reply_to(message, "*මට පාඩුවේ ඉන්න දෙන්න *"+gfromusr_fname+" "+gfromusr_lname,parse_mode='Markdown')
@bot.message_handler(content_types=['new_chat_members'])
def user_joined_greet(message):
	print("group Joined Welcome triggered")
	if message.new_chat_member.id != bot.get_me().id:
		print("group Joined Welcome triggered 2")
		f_name = message.new_chat_member.first_name
		title = message.chat.title
		try:
			l_name=message.new_chat_member.last_name
			newmember=str(f_name+" "+l_name)
		except:
			l_name=" "
			newmember=str(f_name)
		bot.send_message(message.chat.id, "`ආයුබෝවන්` " + "_"+newmember+ "_"+ "`..  ඔබව` "+ "*"+title+"*" + "` වෙත සාදරයෙන් පිළිගනිමු 🙏`",parse_mode='Markdown')
	else:
		title = message.chat.title
		print("added to a new group named "+title)
		bot.send_message(tgadmin, "*I was added by someone to group* "+title,parse_mode='Markdown')
		
@bot.message_handler(content_types=['left_chat_member'])
def user_leave_greet(message):
	if message.left_chat_member.id != bot.get_me().id:
		print("group left curse triggered")
		f_name = message.left_chat_member.first_name
		title = message.chat.title
		try:
			l_name=message.left_chat_member.last_name
			leftmember=str(f_name+" "+l_name)
		except:
			l_name=" "
			leftmember=str(f_name)
		bot.send_message(message.chat.id, "* "+title+"*` හි සිට ඉවත්ව ගිය `_"+leftmember+"_` ව නැවතත් හමුවෙන්න බලාපොරොත්තු වෙමු!  👋..`",parse_mode='Markdown')
	else:
		title = message.chat.title
		print("kicked the bot by some one from a group named "+title)
		bot.send_message(tgadmin, "*I was kicked by someone from group* "+title,parse_mode='Markdown')
		
	
@bot.message_handler(func=lambda message: True)
def totext_all(message):
	print("writing to text")
	gtext=message.text
	gchatid =message.chat.id
	gchat_fname = message.chat.first_name
	try:
		gchat_lname = message.chat.last_name
	except:
		gchat_lname = " - "
	try:
		gchatusrname = message.chat.username
	except:
		gfchatusrname = "  - "
	try:
		gtitle = message.chat.title
	except:
		gtitle = ("*its_empty*")
	gfromusr_id	= message.from_user.id
	gfromusr_fname = message.from_user.first_name
	try:
		gfromusr_lname = message.from_user.last_name
	except:
		gfromusr_lname = "  - "
	try:
		gfromusrname = message.from_user.username
	except:
		gfromusrname = " - "
	
	dumping_data=("| "+str(gtitle)+" "+str(gchatid)+" "+str(gchatusrname)+" "+str(gchat_fname)+" "+str(gchat_lname)+" "+str(gfromusr_id)+" "+str(gfromusrname)+" "+gfromusr_fname+" "+str(gfromusr_lname)+" \n "+gtext+" |  \n \n")
	
	bot.send_message(tgadmin, dumping_data,parse_mode='Markdown')
	#bot.send_message(message.chat.id , message.text)

bot.polling()
