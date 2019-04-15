from pathlib import Path

from flask import Flask, redirect, request
from flask_admin import Admin

from bot import on_chat_message

app = Flask(__name__)

current_dir = Path.cwd()
app.config['SECRET_KEY'] = '123'


@app.route("/")
def hello():
    return 'hi'


@app.route("/telegram_notification/", methods=['POST'])
def tg_notification():
    message = request.json['message']
    on_chat_message(message)
    return 'ok'


if __name__ == '__main__':
    app.run()
