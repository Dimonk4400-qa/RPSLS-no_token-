import telebot 
import random

from telebot import types #keyboard module

TOKEN = 'ТОКЕН'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def game_start(message):
	# Build keyboard
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton('Камень🤜')
	btn2 = types.KeyboardButton('Ножницы✌️')
	btn3 = types.KeyboardButton('Бумага✋')
	btn4 = types.KeyboardButton('Ящерица🤏')
	btn5 = types.KeyboardButton('Спок🖖')
	keyboard.add (btn1, btn2, btn3, btn4, btn5)
	bot.send_message(message.chat.id, 'Камень🤜, Ножницы✌️, Бумага✋, Ящерица🤏, Спок🖖 ! Выберите жест:', reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def game(message):
	choice = random.choice(['Камень🤜', 'Ножницы✌️', 'Бумага✋', 'Ящерица🤏', 'Спок🖖'])
	if message.text == choice:
		bot.send_message(message.chat.id, '🤝Ничья! Для начала новой игры пишите /start')
	else:
		if message.text == 'Камень🤜':
			if choice == 'Ножницы✌️':
				bot.send_message(message.chat.id, 'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /start'.format(choice))
			elif choice == 'Ящерица🤏':
				bot.send_message(message.chat.id, 'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /start'.format(choice))
			elif choice == 'Бумага✋':
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(choice))
			elif choice == 'Спок🖖':
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(choice))

		elif message.text == 'Ножницы✌️':
			if choice == 'Бумага✋':
				bot.send_message(message.chat.id, 'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /start'.format(choice))
			elif choice == 'Ящерица🤏':
				bot.send_message(message.chat.id, 'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /start'.format(choice))
			elif choice == 'Камень🤜':
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(choice))
			elif choice == 'Спок🖖':
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(choice))		

		elif message.text == 'Бумага✋':
			if choice == 'Камень🤜':
				bot.send_message(message.chat.id, 'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /start'.format(choice))
			elif choice == 'Спок🖖':
				bot.send_message(message.chat.id, 'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /start'.format(choice))
			elif choice == 'Ножницы✌️':
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(choice))
			elif choice == 'Ящерица🤏':
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(choice))

		elif message.text == 'Ящерица🤏':
			if choice == 'Бумага✋':
				bot.send_message(message.chat.id, 'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /start'.format(choice))
			elif choice == 'Спок🖖':
				bot.send_message(message.chat.id, 'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /start'.format(choice))
			elif choice == 'Ножницы✌️':
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(choice))
			elif choice == 'Камень🤜':
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(choice))

		elif message.text == 'Спок🖖':
			if choice == 'Ножницы✌️':
				bot.send_message(message.chat.id, 'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /start'.format(choice))
			elif choice == 'Камень🤜':
				bot.send_message(message.chat.id, 'Поздравляю с победой! У меня была {}. Для начала новой игры пишите /start'.format(choice))
			elif choice == 'Бумага✋':
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(choice))
			elif choice == 'Ящерица🤏':
				bot.send_message(message.chat.id, 'Извените, но Вы проиграли 😢. У меня был(и/a) {}. Для начала новой игры пишите /start'.format(choice))
bot.polling(none_stop=True)
