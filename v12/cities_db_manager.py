from weather import get_weather
from cities_db_manager import db, City




# словарь, в котором ключи будут юзернеймами, а значения - True/False
waiting_for_cities = {}
cities = {}



def process_chat_message(msg):
    text = msg['text']
    username = msg['from']['username']
    print(username + ': ' + text)

    if text == 'Установить город':
        reply = 'Отправь мне свой город'
        waiting_for_cities[username] = True

    elif text == 'Узнать погоду':

        # пытаемся достать город из базы данных
        city_from_db = City.query.filter_by(username=username).first()

        # если он есть - достаем имя и запрашиваем погоду
        if city_from_db:
            city_name = city_from_db.city_name
            reply = get_weather(city_name)
        else:
            reply = 'Сначала установи город.'

    else:
        # если бот ждет от пользователя город - то сохраняем пользовательский ввод.
        # иначе говорим, что не поняли пользователя
        if username in waiting_for_cities and waiting_for_cities[username] == True:

            # пытаемся достать город из базы данных
            city_from_db = City.query.filter_by(username=username).first()

            # если он есть - меняем имя города на новое (которое передал юзер)
            if city_from_db:
                city_from_db.city_name = text

            # если его нет - создаем новый город
            else:
                city_from_db = City(city_name=text, username=username)

            # сохраняем город обратно в базу
            db.session.add(city_from_db)
            db.session.commit()

            waiting_for_cities[username] = False

            reply = 'Устанавливаю город ' + text
        else:

            reply = 'Я еще совсем маленький и не понимаю человеческую речь. Воспользуйся кнопками, пожалуйста.'

    buttons = [['Установить город', 'Узнать погоду']]
    return reply, buttons
