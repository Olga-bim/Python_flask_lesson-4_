from flask import Flask  # Импортируем класс Flask из библиотеки flask

app = Flask(__name__)  # Создаём экземпляр класса Flask, который будет нашим приложением

@app.route('/test 1')  # Декоратор route определяет маршрут для URL "/"
def fghndf():  # Функция, которая выполняется при обращении к маршруту "/"
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <button>test 1</button>
</body>
</html>
"""  # Возвращает текст "Hello, Flask!" как ответ на запрос

@app.route('/test2')  # Декоратор route определяет маршрут для URL "/"
def sgbs():  # Функция, которая выполняется при обращении к маршруту "/"
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <button>test 2</button>
</body>
</html>
"""

@app.route('/test3')  # Декоратор route определяет маршрут для URL "/"
def jlklh():  # Функция, которая выполняется при обращении к маршруту "/"
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <button>test 3</button>
    <img src="https://picsum.photos/200" alt="">
</body>
</html>
"""
if __name__ == '__main__':  # Проверяем, что код запущен как основной модуль, а не импортирован
    app.run(debug=True)  # Запускаем приложение Flask в режиме отладки
