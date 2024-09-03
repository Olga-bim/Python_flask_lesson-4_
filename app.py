from flask import Flask, render_template  

app = Flask(__name__)  

ar = ["waga", "baga", "saga"]


@app.route('/test1')  
def fghndf():  
    # n1 =9
    return  render_template('hello1.html', n = ar) 

@app.route('/test2')  
def sgbs():  
    return render_template('hello2.html') 

@app.route('/test3')  
def jlklh():  
    return render_template('hello3.html') 

if __name__ == '__main__':  
    app.run(debug=True)  # Запускаем приложение Flask в режиме отладки
