from weather import get_weather

# словарь, в котором ключи будут юзернеймами, а значения - True/False
waiting_for_cities = {}
cities = {}


def process_chat_message(msg):

    text = msg['text']
    chat_id = str(msg['from']['id'])
    print(chat_id + ': ' + text)

    if text == 'Установить город':
        reply = 'Отправь мне свой город'
        waiting_for_cities[chat_id] = True

    elif text == 'Узнать погоду':

        # если бот уже запомнил город человека - узнаем погоду в этом городе.
        # иначе просим установить город
        if chat_id in cities:
            city = cities[chat_id]
            reply = get_weather(city)
        else:
            reply = 'Сначала установи город.'

    else:
        # если бот ждет от пользователя город - то сохраняем пользовательский ввод.
        # иначе говорим, что не поняли пользователя
        if chat_id in waiting_for_cities and waiting_for_cities[username] == True:
            cities[chat_id] = text
            waiting_for_cities[chat_id] = False
            reply = 'Устанавливаю город ' + text
        else:

            reply = 'Я еще совсем маленький и не понимаю человеческую речь. Воспользуйся кнопками, пожалуйста.'

    buttons = [['Установить город', 'Узнать погоду']]
    return reply, buttons
