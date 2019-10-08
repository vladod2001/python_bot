import  telebot

bot = telebot.TeleBot('861128087:AAEMptgfaeNGnlSWXtvA9-oh5aEtaynsvmo')

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup=telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row('/start')
    user_markup.row('АНГЛИЙСКИЙ','ОТВЕТЫ')
    bot.send_message(message.chat.id,'Welcome',reply_markup=user_markup)

@bot.message_handler(commands=['text'])
def start_message(message):
    bot.send_message(message.chat.id, '1)Д/З')
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.upper() == 'АНГЛИЙСКИЙ':
        bot.send_photo(message.chat.id, open('1.jpg','rb'));
    if message.text.upper() == 'ОТВЕТЫ':
        bot.send_photo(message.chat.id, open('1.jpg','rb'));

    else:
        bot.send_message(message.from_user.id, "Sorry, i dont understand you.")

bot.polling(none_stop=True, interval=0)
