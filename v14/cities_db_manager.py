from pathlib import Path

from flask import Flask, redirect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

current_dir = Path.cwd()
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{current_dir}/cities.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123'

db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    city_name = db.Column(db.String(120), index=True)


db.create_all()

app.config['FLASK_ADMIN_SWATCH'] = 'flatly'
admin = Admin(app, name='Database', template_mode='bootstrap3')
admin.add_view(ModelView(City, db.session))


@app.route("/")
def hello():
    return redirect('/admin/city/')


if __name__ == '__main__':
    app.run()
