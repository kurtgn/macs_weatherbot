import requests

from bot import bot
from process_message import cities_url
from weather import get_weather

# получаем словарь с chat_id и городами

def remind():
    cities = requests.get(cities_url).json().get('result') or {}

    # идем по каждому chat_id в словаре
    for chat_id in cities:
        # достаем город
        city_name = cities[chat_id]
        # достаем погоду для города
        reply = get_weather(city_name)
        # отправляем сообщение
        bot.sendMessage(chat_id, text=reply)

