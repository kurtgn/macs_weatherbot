from pprint import pprint

import requests
from weather import get_weather


jsonstore_url = 'https://www.jsonstore.io/c4a09b5c42a254591516d574d76b99f3c52988f3eac7f9b9c6c383d32f979f02'
waiting_url = jsonstore_url + '/waiting/'
cities_url = jsonstore_url + '/cities/'




# словарь, в котором ключи будут юзернеймами, а значения - True/False
waiting_for_cities = {}
cities = {}


def set_waiting(chat_id):
    waiting = requests.get(waiting_url).json().get('result') or {}
    waiting[chat_id] = True
    requests.post(waiting_url, json=waiting)


def clear_waiting(chat_id):
    waiting = requests.get(waiting_url).json().get('result') or {}
    waiting[chat_id] = False
    requests.post(waiting_url, json=waiting)

def is_waiting(chat_id):
    waiting = requests.get(waiting_url).json().get('result') or {}
    return waiting.get(chat_id, False)


def save_city(chat_id, cityname):
    cities = requests.get(cities_url).json().get('result') or {}
    cities[chat_id] = cityname
    requests.post(cities_url, json=cities)


def get_city(chat_id):
    cities = requests.get(cities_url).json().get('result') or {}
    return cities.get(chat_id)



def process_chat_message(msg):

    pprint(msg)
    text = msg['text']
    chat_id = str(msg['chat']['id'])
    print(chat_id + ': ' + text)

    if text == 'Установить город':
        set_waiting(chat_id)
        reply = 'Отправь мне свой город'

    elif text == 'Узнать погоду':

        # пытаемся достать город из базы данных
        city = get_city(chat_id)

        # если он есть - меняем имя города на новое (которое передал юзер)
        if city:
            reply = get_weather(city)
        else:
            reply = 'Сначала установи город.'

    else:
        # если бот ждет от пользователя город - то сохраняем пользовательский ввод.
        # иначе говорим, что не поняли пользователя
        if is_waiting(chat_id):

            save_city(chat_id=chat_id, cityname=text)

            clear_waiting(chat_id)

            reply = 'Устанавливаю город ' + text
        else:

            reply = 'Я еще совсем маленький и не понимаю человеческую речь. Воспользуйся кнопками, пожалуйста.'

    buttons = [['Установить город', 'Узнать погоду']]
    return reply, buttons
