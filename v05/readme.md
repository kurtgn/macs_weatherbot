#  5. Распознаем нажатия разных кнопок


- Как сделать так, чтобы бот понимал, что человек нажимает кнопку, а не вводит текст вручную?
- Научим бота отвечать по-разному в зависимости от нажатия кнопок.


Измените функцию `process_chat_message` так, чтобы она создавала разный `reply` 
в зависимости от ввода пользователя. Не забудьте, что в конце функции должны создаваться кнопки.
```python

def process_chat_message(msg):
    text = msg['text']

    if text == 'Установить город':
        reply = 'Хорошо, устанавливаю город'

    elif text == 'Узнать погоду':
        reply = 'Узнаю погоду'

    else:
        reply = 'Ты сказал ' + text
        
```


---
![right](coffee.jpeg)
# ✅ Задание 

Измените текст в случае свободного ввода на какой-нибудь другой. 
Например, *“Я не понимаю тебя, человек. Используй кнопки”*.

