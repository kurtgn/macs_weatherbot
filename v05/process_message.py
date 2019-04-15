from pprint import pprint


def process_chat_message(msg):
    text = msg['text']
    print(str(msg['from']['id']) + ': ' + text)

    if text == 'Установить город':
        reply = 'Хорошо, устанавливаю город'

    elif text == 'Узнать погоду':
        reply = 'Узнаю погоду'

    else:
        reply = 'Ты сказал ' + text

    buttons = [['Установить город', 'Узнать погоду']]
    return reply, buttons
