from pprint import pprint


# словарь, в котором ключи будут юзернеймами, а значения - True/False
waiting_for_cities = {}



def process_chat_message(msg):

    text = msg['text']
    username = msg['from']['username']
    print(username + ': ' + text)

    if text == 'Установить город':
        reply = 'Отправь мне свой город'
        waiting_for_cities[username] = True


    elif text == 'Узнать погоду':

        reply = 'Узнаю погоду'

    else:
        # если бот ждет от пользователя город - то сохраняем пользовательский ввод.
        # иначе говорим, что не поняли пользователя
        if username in waiting_for_cities and waiting_for_cities[username] == True:
            waiting_for_cities[username] = False
            reply = 'Устанавливаю город ' + text
        else:

            reply = 'Я еще совсем маленький и не понимаю человеческую речь. Воспользуйся кнопками, пожалуйста.'

    buttons = [['Установить город', 'Узнать погоду']]
    return reply, buttons
