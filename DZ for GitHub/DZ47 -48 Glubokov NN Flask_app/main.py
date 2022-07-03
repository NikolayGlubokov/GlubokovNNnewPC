import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
from FDataBase import FDataBase

DATABASE = '/tmp/menu.db'


DEBUG = True
SECRET_KEY = 'de88b65b2875709700edaa9b0afa1ac98064961a'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'cars.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con

def create_db():
    db = connect_db()
    with app.open_resource('sq2_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

menu = [
    {"name": "Главная", 'url': 'index'},
    {"name": "О нас", 'url': 'about'},
{"name": "Наши партнёры", 'url': 'infopartners'},
    {"name": "Обратная связь", 'url': 'contact'}]

psmenu = [
    {"name": "Каталог курсов", 'url':'post'},
    {"name": "Добавить курс", 'url': 'add_post'},
{"name": "Информация о партнерах", 'url': 'infopartners'}]

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db




@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/index")
@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("index.html", title="Главная", cars=dbase.get_menu(), menu=menu)

@app.route("/mazda")
def mazda():
    db = get_db()
    dbase = FDataBase(db)
    print(url_for('mazda'))
    return render_template('mazda.html', title="Mazda", dbs=dbase.get_menu(), menu=menu)

@app.route("/infopartners")
def infopartners():
    print(url_for('nissan'))
    return render_template('infopartners.html', title="Партнеры организации", menu=menu, psmenu=psmenu)

@app.route("/nissan")
def nissan():
    db = get_db()
    dbase = FDataBase(db)
    print(url_for('nissan'))
    return render_template('nissan.html', title="Nissan", dbs=dbase.get_menu(), menu=menu)

@app.route("/toyota")
def toyota():
    db = get_db()
    dbase = FDataBase(db)
    print(url_for('toyota'))
    return render_template('toyota.html', title="Toyota", dbs=dbase.get_menu(), menu=menu)

@app.route("/subaru")
def subaru():
    db = get_db()
    dbase = FDataBase(db)
    print(url_for('subaru'))
    return render_template('subaru.html', title="Subaru", dbs=dbase.get_menu(), menu=menu)

@app.route("/mitsubishi")
def mitsubishi():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('mitsubishi.html', title="Mitsubishi", dbs=dbase.get_menu(), menu=menu)

@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title="О нас", menu=menu)

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash("Сообщение отправлено успешно!", category='success')
        else:
            flash("Ошибка отправки данных", category='error')
    return render_template('contact.html', title="Обратная связь", menu=menu)


@app.route('/login', methods=["POST", "GET"])
def login():
    if 'userLogged' == session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'elena' and request.form['passw'] == '123456':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title="Авторизация", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f"Пользователь: {username}"


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10 and len(request.form['url']) <6:
            res = dbase.add_post(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash("Ошибка добавления статьи", category='error')
            else:
                flash("Статья добавлена успешно", category='success')
        else:
            flash("Ошибка добавления статьи", category='error')
    return render_template("add_post.html", title="Добавление статьи",psmenu=psmenu, menu=menu)


@app.route('/post')
def show_post():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('post.html', menu=menu, posts=dbase.get_post(), psmenu=psmenu)

if __name__ == '__main__':
    create_db()
    app.run(debug=True)