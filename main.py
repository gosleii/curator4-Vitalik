import telebot
bot = telebot.TeleBot('6850045880:AAEYFyC2z0BI-oEYV9i2q955nXpC06QW8YA')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, я MG')

@bot.message_handler(commands=['who'])
def main(message):
    bot.send_message(message.chat.id, 'Разработчик: тот кто пишет этот текст :)')

@bot.message_handler(commands=['meow'])
def main(message):
    bot.send_message(message.chat.id, '*мяу*', parse_mode='Markdown')

@bot.message_handler(commands=['okgoogle'])
def main(message):
    bot.send_message(message.chat.id, '[OK, Google...](https://www.google.ru/)', parse_mode='Markdown')

bot.infinity_polling()
