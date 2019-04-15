from pprint import pprint


# словарь, в котором ключи будут юзернеймами, а значения - True/False
waiting_for_cities = False


def process_chat_message(msg):

    global waiting_for_cities

    text = msg['text']
    username = msg['from']['username']

    if text == 'Установить город':
        reply = 'Отправь мне свой город'
        waiting_for_cities = True

    elif text == 'Узнать погоду':

        reply = 'Узнаю погоду'

    else:

        if waiting_for_cities == True:
            reply = 'Устанавливаю город ' + text
            waiting_for_cities = False
        else:

            reply = 'Я еще совсем маленький и не понимаю человеческую речь. Воспользуйся кнопками, пожалуйста.'

    buttons = [['Установить город', 'Узнать погоду']]
    return reply, buttons
