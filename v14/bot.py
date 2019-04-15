# добавим реальный запрос погоды



from time import sleep
import telepot
from telepot import Bot


# функция, которая определяет, что ответить пользователю
from telepot.namedtuple import ReplyKeyboardMarkup


from process_message import process_chat_message


# обход блокировки Телеграмма
def _methodurl(req, **user_kw):
    token, method, params, files = req
    return 'http://tg.fstrk.io/bot%s/%s' % (token, method)
telepot.api._methodurl = _methodurl


bot = Bot('779201721:AAGtKbHrgAS99WeI9pT5qrxhX0fyM3xtP4E')
bot.setWebhook(None)


# функция приема нового сообщения
def on_chat_message(msg):
    reply, buttons = process_chat_message(msg)
    chat_id = msg['chat']['id']
    bot.sendMessage(
        chat_id=chat_id,
        text=reply,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=buttons,
            resize_keyboard=True
        )
    )

# создаем конфигурацию бота: словарь с нашими функциями (пока что одной)
telepot_config = {'chat': on_chat_message}

# запускаем цикл
bot.message_loop(telepot_config)

# Входим в бесконечный цикл, чтобы программа не останавливалась и бот работал
while True:
    sleep(10)


