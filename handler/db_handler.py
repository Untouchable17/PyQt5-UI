import sqlite3


def login(login, password, signal):
    """ Функция для авторизации """
    connection = sqlite3.connect('handler/users')
    cursor = connection.cursor()

    # Проверяем есть ли такой пользователь
    cursor.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cursor.fetchall()
    
    if value != [] and value[0][2] == password:
        signal.emit('Успешная авторизация!')
    else:
        signal.emit('Проверьте правильность ввода данных!')

    cursor.close()
    connection.close()


def register(login, password, signal):
    """ Функция для регистрации """
    connection = sqlite3.connect('handler/users')
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cursor.fetchall()

    if value != []:
        signal.emit('Такой ник уже используется')

    elif value == []:
        cursor.execute(f"INSERT INTO users (name, password) VALUES ('{login}', '{password}')")
        signal.emit('Вы успешно зарегистрировались')
        cursor.commit()

    cursor.close()
    connection.close()