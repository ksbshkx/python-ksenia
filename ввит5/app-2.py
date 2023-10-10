from flask import Flask, render_template, request, redirect  # импортируем необходимые иструменты
import psycopg2

app = Flask(__name__)  # создаём приложение

conn = psycopg2.connect(database="service_db",  # подключение к базе данных
                        user="postgres",
                        password="WDPTsz3F",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()  # добавляем курсор для обращения к базе данных


@app.route('/login/', methods=['POST', 'GET'])  # декоратор
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            password = request.form.get('password')
            if not username:
                return render_template('login.html', error="Введите логин")
            if not password:
                return render_template('login.html', error="Введите пароль")
            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
            records = list(cursor.fetchall())

            return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])
        elif request.form.get("registration"):
            return redirect("/registration/")

    return render_template('login.html')


@app.route('/registration/', methods=['POST', 'GET'])  # декоратор
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login1 = request.form.get('login')
        password = request.form.get('password')

        if not name:
            return render_template('registration.html', error="Введите имя")
        if not password:
            return render_template('registration.html', error="Введите пароль")
        if not login1:
            return render_template('registration.html', error="Введите логин")
        cursor.execute("SELECT * FROM service.users WHERE login='{login1}'". \
                       format(login1=login1))
        records = list(cursor.fetchall())
        if not records:
            cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);',
                           (str(name), str(login1), str(password)))
            conn.commit()
            return redirect('/login/')
        else:
            return render_template('registration.html', error='Такой аккаунт уже существует')

    return render_template('registration.html')
