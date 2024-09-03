from flask import Flask, render_template  

app = Flask(__name__)  

ar = ["waga", "baga", "saga"]

data = [
        {'name': 'Alice', 'age': 30, 'admin': False},
        {'name': 'Bob', 'age': 25, 'admin': True},
        {'name': 'Charlie', 'age': 35, 'admin': False},
        {'name': 'Olga', 'age': 40, 'admin': True}
    ]
@app.route('/test1')  
def fghndf():  
    # n1 =9
    return  render_template('hello1.html', people=data) 

@app.route('/test2')  
def sgbs():  
    return render_template('hello2.html') 

@app.route('/test3')  
def jlklh():  
    return render_template('hello3.html') 

if __name__ == '__main__':  
    app.run(debug=True)  # Запускаем приложение Flask в режиме отладки
