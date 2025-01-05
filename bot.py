import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

#PROXY = {
#        'proxy_url': 'socks5://t3.learn.python.ru:1080',
#        'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Здравствуй, банан!")

def talk2me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

# Главная функция
def main():
    # Создаем бота
    mybot = Updater("settings.API_KEY", use_context=True) #, request_kwargs=PROXY)

    # Диспетчер для управления обработчиками
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))  # Обработчик команды /start
    dp.add_handler(MessageHandler(Filters.text, talk2me))

    # Запускаем бота
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()