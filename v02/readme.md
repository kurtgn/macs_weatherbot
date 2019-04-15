

# 2. Кнопки 

Научим бота показывать кнопки. Они передаются в виде списка списков:

```python
bot.sendMessage(
    chat_id=chat_id,
    text=reply,
    reply_markup=ReplyKeyboardMarkup(
        keyboard=[['Кнопка!']],
        resize_keyboard=True
    )
)


```

---

# ✅ Задание 

Наш бот должен показывать две кнопки: **“Установить город”** и **“Узнать погоду”**. 

Добавьте в бота эти кнопки.
