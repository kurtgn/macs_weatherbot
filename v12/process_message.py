from weather import get_weather
from cities_db_manager import db, City
# словарь, в котором ключи будут юзернеймами, а значения - True/False
waiting_for_cities = {}
cities = {}



def process_chat_message(msg):
    text = msg['text']
    chat_id = str(msg['from']['username'])
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
        if chat_id in waiting_for_cities and waiting_for_cities[chat_id] == True:

            # пытаемся достать город из базы данных
            city_from_db = City.query.filter_by(username=chat_id).first()

            # если он есть - меняем имя города на новое (которое передал юзер)
            if city_from_db:
                city_from_db.city_name = text

            # если его нет - создаем новый город
            else:
                city_from_db = City(city_name=text, username=username)

            # сохраняем город обратно в базу
            db.session.add(city_from_db)
            db.session.commit()

            waiting_for_cities[chat_id] = False

            reply = 'Устанавливаю город ' + text
        else:

            reply = 'Я еще совсем маленький и не понимаю человеческую речь. Воспользуйся кнопками, пожалуйста.'

    buttons = [['Установить город', 'Узнать погоду']]
    return reply, buttons
