from flask import g, Flask, render_template, url_for, request, session, redirect, flash, abort
from flask_sqlalchemy import SQLAlchemy
import os

# конфигурация

DEBUG = True
SECRET_KEY = 'de88b65b2875709700edaa9b0afa1ac98064961a'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carname = db.Column(db.String(50), nullable=False)
    data_created = db.Column(db.String(200))
    title=db.Column(db.String(1000))
    price=db.Column(db.Integer)

    def __repr__(self):
        return f"<Task {self.id}>"




car_list = [ 'Volkswagen Golf GTI', 'Honda Civic', 'Peugeot 206', 'Mazda MX-5','Dodge neon',
'Mitsubishi Motors Eclipse','Toyota Celica','Mazda RX-7','Mitsubishi Motors Lancer','Ford Focus',
'Subaru Impreza', 'Hyundai Tiburon GT V6','Nissan Sentra SE R SPEC V','Nissan 240SX','Toyota Supra',
'Acura RSX','Acura Integra Type R', 'Nissan 350Z','Honda S2000', 'Nissan Skyline GTR']


navigation=[
    {'name':'Главная','url':'index'},
   {'name':'Наши курсы','url':'courses'},
{'name':'Добавить курсы','url':'add_courses'},
{'name':'Личный кабинет','url':'cabinet'},
    {'name': 'О нас', 'url': 'about'},
{'name':'Обратная связь','url':'contact'},
]

spec=[
    {'name':'Танцевальная студия','img':'1.jpg'},
    {'name':'Библиотека','url':'about'},
{'name':'Компьютерный клуб','url':'contact'},
{'name':'Стена объявлений','url':'wand'},
{'name':'Личный кабинет','url':'cabinet'},
]
app = Flask(__name__)




# def index():
#     db = get_db()
#     dbase = FDataBase(db)
#     return render_template("index.html", title="Главная", menu=dbase.get_menu(), posts=dbase.get_posts_anonce())

@app.route('/')# Главная страница
@app.route('/index')
def index():

    return render_template('index.html', title='Главная страница', navigation=navigation, car_list=car_list)

@app.route('/<carname>')
def car(carname):
    return render_template('car.html', title = 'Описание сайта', navigation=navigation)

@app.route('/about')
def about():
    return render_template('about.html', title = 'Описание сайта', navigation=navigation)

@app.route('/courses')
def courses():
    return render_template('courses.html',  title='Обратная связь', navigation=navigation)

@app.route('/add_courses')
def add_courses():
    return render_template('add_courses.html',  title='Обратная связь', navigation=navigation)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
     return render_template('contact.html', title="Обратная связь",  navigation=navigation)

@app.route('/cabinet')
def cabinet():
    return render_template('cabinet.html',  title='Обратная связь', navigation=navigation)




if __name__=='__main__':

    app.run(debug=True)

