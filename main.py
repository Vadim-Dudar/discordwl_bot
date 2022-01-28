import config
import telebot


bot = telebot.TeleBot(config.token)
accounts = []
base = {}


for account in open('discord.txt', 'r'):
    accounts.append(account)


@bot.message_handler(commands=['start'])
def send_inf(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    get_account = telebot.types.InlineKeyboardButton('Получить!', callback_data='get')
    markup.add(get_account)

    bot.send_message(message.chat.id,
                     f'Приветствую 👋\n\n‼️Оформление: Почта+пароль+токен\nПароль от дс и почты ОДИНАКОВЫЙ\n\nВаш аккаунт для набива вайтлиста, у вас получится:',
                     reply_markup=markup)
    base[message.chat.id] = 0


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        for key in base.keys():
            if key == call.message.chat.id and base[key] < 2:
                bot.send_message(call.message.chat.id, f'{accounts[0]}')
                accounts.pop(0)
                base[key] += 1
                print(base[key])
            else:
                bot.send_message(call.message.chat.id, 'Извините, но у вас уже есть 2 аккаунта ☹!')


bot.polling(none_stop=True)
