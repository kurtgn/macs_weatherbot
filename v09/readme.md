# 9. Добавим запрос погоды

Создайте файл `weather.py` и скопируйте туда код:

```python
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


if __name__ == '__main__':
    weather = get_weather('Москва')
    print(weather)


```

Перейдите в `process_message.py` и воспользуйтесь функцией получени погоды. Вначале импортируйте его:

```python
from weather import get_weather
```

А ниже, вместо фразы "Узнаю погоду в городе...", вставьте настоящее обращение к сервису погоды:

```python
city = cities[username]
reply = get_weather(city)
```


# ✅ Задание 

Файл `weather.py` работает не только вместе с чатботом, 
его можно запустить самостоятельно. 

- Запустите его. Какой город он проверяет по умолчанию?
- Замените город на какой-нибудь другой.
- Что будет, если передать несуществующий город? Как это починить?  

