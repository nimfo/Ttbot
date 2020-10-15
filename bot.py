import telebot
from telebot import types

bot = telebot.TeleBot('951176483:AAGuL17E-lOtWa7gLxi2ECxotx9fPpNHYS4')

# города
global goroda, gorod_m, gorod_s, gorod_v
goroda = types.InlineKeyboardMarkup(row_width=1)
gorod_m = types.InlineKeyboardButton("Минск", callback_data='minsk')
gorod_s = types.InlineKeyboardButton("Солигорск", callback_data='soligorsk')
gorod_v = types.InlineKeyboardButton("Витебск", callback_data='vitebsk')
# Пример: gorod_test(переменная в которой будет кнопка) = types.InlineKeyboardButton("Тестовый город(текст кнопки)", callback_data='test1 (значение кнопки, может быть любым)')
goroda.add(gorod_m, gorod_s, gorod_v) #сюда добавляем переменную кнопки, к примеру (gorod, gorod2, gorod_test)

@bot.message_handler(commands=['start'])
def welcome(message):

	bot.send_message(message.chat.id, 'Привет, выберите город', reply_markup=goroda)

@bot.callback_query_handler(func=lambda call: True)
def messages_shop(call):
	if call.message:
		# продукты
		pr1 = ['Яблоко1', 'цена']
		pr2 = ['Яблоко2', 'цена']
		pr3 = ['Яблоко3', 'цена']
		pr4 = ['Яблоко4', 'цена']
		pr5 = ['Яблоко5', 'цена']
		pr6 = ['Яблоко6', 'цена']
		pr7 = ['Яблоко7', 'цена']
		pr8 = ['Яблоко8', 'цена']
		pr9 = ['Яблоко9', 'цена']

		product = types.InlineKeyboardMarkup(row_width=1)
		p1 = types.InlineKeyboardButton(pr1[0], callback_data='pr1')
		p2 = types.InlineKeyboardButton(pr2[0], callback_data='pr2')
		p3 = types.InlineKeyboardButton(pr3[0], callback_data='pr3')
		p4 = types.InlineKeyboardButton(pr4[0], callback_data='pr4')
		p5 = types.InlineKeyboardButton(pr5[0], callback_data='pr5')
		p6 = types.InlineKeyboardButton(pr6[0], callback_data='pr6')
		p7 = types.InlineKeyboardButton(pr7[0], callback_data='pr7')
		p8 = types.InlineKeyboardButton(pr8[0], callback_data='pr8')
		p9 = types.InlineKeyboardButton(pr9[0], callback_data='pr9')
		product.add(p1, p2, p3, p4, p5, p6, p7, p8, p9)
		pay = types.InlineKeyboardMarkup(row_width=1)
		oplata = types.InlineKeyboardButton("Оплатить", callback_data='p_ay', url='https://t.me/NIKLIM022') # Ссылка на профиль в телеграмме
		otmena = types.InlineKeyboardButton("Отмена", callback_data='o_tm')
		pay.add(oplata, otmena)
		if call.data == 'minsk':
			bot.send_message(call.message.chat.id, 'Выберите продукт', reply_markup=product)
		# сдесь идёт обработка, если добавлен новый город то делаем следующае:
		# elif call.data == 'test1 (это значение кнопки которое задано в callback_data к примеру на 12 строке)':
		# 	bot.send_message(call.message.chat.id, 'Выберите продукт', reply_markup=product)
		elif call.data == 'soligorsk':
			bot.send_message(call.message.chat.id, 'Выберите продукт', reply_markup=product)
		elif call.data == 'vitebsk':
			bot.send_message(call.message.chat.id, 'Выберите продукт', reply_markup=product)
		elif call.data == 'o_tm':
			bot.send_message(call.message.chat.id, 'Выберите город', reply_markup=goroda)
		else:
			pf = '#'
			psum = '#'
			vr = str(call.data)
			if vr == 'pr1':
				pf = pr1[0]
				psum = pr1[1]
			elif vr == 'pr2':
				pf = pr2[0]
				psum = pr2[1]
			elif vr == 'pr3':
				pf = pr3[0]
				psum = pr3[1]
			elif vr == 'pr4':
				pf = pr4[0]
				psum = pr4[1]
			elif vr == 'pr5':
				pf = pr5[0]
				psum = pr5[1]
			elif vr == 'pr6':
				pf = pr6[0]
				psum = pr6[1]
			elif vr == 'pr7':
				pf = pr7[0]
				psum = pr7[1]
			elif vr == 'pr8':
				pf = pr8[0]
				psum = pr8[1]
			elif vr == 'pr9':
				pf = pr9[0]
				psum = pr9[1]
			bot.send_message(call.message.chat.id, 'Товар и объем '+pf+' ('+psum+'р.'+')\nОплатите '+psum+' руб.\nДля проведения оплаты нажмите на\nкнопку ОПЛАТИТЬ', reply_markup=pay)
			pay_opl = call.data

bot.polling(none_stop = True, interval = 0)