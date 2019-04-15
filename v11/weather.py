import requests


def get_weather(city):
    response = requests.get(
        'https://api.openweathermap.org/data/2.5/weather',
        params={
            'q': city,
            'appid': '1c61f1a45db0ff493dd0a57b0bc10c57',
            'units': 'metric',
            'lang': 'ru'
        }
    )

    data = response.json()

    # сохраним температуру в переменной temp
    temp = data['main']['temp']

    # сохраним описание в переменной description
    description = data['weather'][0]['description']

    # сохраним полный ответ в переменной response и вернем ее
    response = city + ': ' + str(temp) + ' градусов, ' + description
    return response

