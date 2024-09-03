from flask import Flask, render_template  # Импортируем класс Flask из библиотеки flask

app = Flask(__name__)  # Создаём экземпляр класса Flask, который будет нашим приложением

@app.route('/test1')  # Декоратор route определяет маршрут для URL "/"
def fghndf():  # Функция, которая выполняется при обращении к маршруту "/"
    return  render_template('hello1.html') 

@app.route('/test2')  # Декоратор route определяет маршрут для URL "/"
def sgbs():  # Функция, которая выполняется при обращении к маршруту "/"
    return render_template('hello2.html') 

@app.route('/test3')  # Декоратор route определяет маршрут для URL "/"
def jlklh():  # Функция, которая выполняется при обращении к маршруту "/"
    return render_template('hello3.html') 
if __name__ == '__main__':  # Проверяем, что код запущен как основной модуль, а не импортирован
    app.run(debug=True)  # Запускаем приложение Flask в режиме отладки
