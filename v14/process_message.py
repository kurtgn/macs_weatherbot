from weather import get_weather
from cities_db_manager import db, City




# словарь, в котором ключи будут юзернеймами, а значения - True/False
waiting_for_cities = {}
cities = {}


def set_waiting(username):
    waiting_for_cities[username] = True


def clear_waiting(username):
    waiting_for_cities[username] = False


def is_waiting(username):
    if username in waiting_for_cities and waiting_for_cities[username] == True:
        return True


def get_city(username):
    city_from_db = City.query.filter_by(username=username).first()
    return city_from_db.city_name


def save_city(username, cityname):
    """ Сохранить город пользователя в БД """
    # пытаемся достать город из базы данных
    city_from_db = City.query.filter_by(username=username).first()

    # если он есть - меняем имя города на новое (которое передал юзер)
    if city_from_db:
        city_from_db.city_name = cityname

    # если его нет - создаем новый город
    else:
        city_from_db = City(city_name=cityname, username=username)

    # сохраняем город обратно в базу
    db.session.add(city_from_db)
    db.session.commit()




def process_chat_message(msg):
    text = msg['text']
    username = msg['from']['username']
    print(username + ': ' + text)

    if text == 'Установить город':
        set_waiting(username)
        reply = 'Отправь мне свой город'

    elif text == 'Узнать погоду':

        # пытаемся достать город из базы данных
        city = get_city(username)

        # если он есть - достаем имя и запрашиваем погоду
        if city:
            reply = get_weather(city)
        else:
            reply = 'Сначала установи город.'

    else:
        # если бот ждет от пользователя город - то сохраняем пользовательский ввод.
        # иначе говорим, что не поняли пользователя
        if is_waiting(username):

            save_city(username=username, cityname=text)

            clear_waiting(username)

            reply = 'Устанавливаю город ' + text
        else:

            reply = 'Я еще совсем маленький и не понимаю человеческую речь. Воспользуйся кнопками, пожалуйста.'

    buttons = [['Установить город', 'Узнать погоду']]
    return reply, buttons
