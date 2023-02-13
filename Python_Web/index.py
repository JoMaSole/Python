#pip install flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

#nueva ruta
@app.route('/about')
def about():
    return render_template('pagina2.html')

@app.route('/index.html')
def maps():
    return render_template('index.html')












if __name__ == '__main__':
    app.run(debug = True)