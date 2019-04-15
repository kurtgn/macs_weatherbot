# 3. Кнопки в отдельной функции


## Зачем?

Потому что количество кода будет расти, а смотреть на одну длинную программу - тяжеловато. 
Нужно дробить код на небольшие функции.

- Обновите функцию `process_chat_message`, она теперь не только 
создает ответ, но и добавляет к ответу кнопки.

```python
def process_chat_message(msg):
    text = msg['text']
    print(text)
    reply = 'Ты сказал ' + text
    buttons = [['Установить город', 'Узнать погоду']]
    return reply, buttons
```

- Обновите функцию `on_chat_message`, чтобы она не создавала кнопки сама,
а брала их из функции `process_chat_message`.

```python
def on_chat_message(msg):
    reply, buttons = process_chat_message(msg)
    chat_id = msg['chat']['id']
    bot.sendMessage(
        chat_id=chat_id,
        text=reply,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=buttons,
            resize_keyboard=True
        )
    )
```

# Задание 


Бот показывает кнопки в один ряд. 

*Сделайте так, чтобы одна кнопка была под другой.*
