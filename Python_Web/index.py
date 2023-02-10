#pip install flask
from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return 'Hola, bienvenido'

if __name__ == '__main__':
    app.run()