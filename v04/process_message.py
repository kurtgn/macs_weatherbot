def process_chat_message(msg):
    text = msg['text']
    print(text)
    reply = 'Ты сказал ' + text
    buttons = [['Установить город', 'Узнать погоду']]
    return reply, buttons
