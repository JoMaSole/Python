#pip install flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

#nueva ruta
@app.route('/Profile')
def about():
    return render_template('pages-profile.html')

@app.route('/sign-in')
def maps():
    return render_template('pages-sign-in')

@app.route('/sign-out')
def maps():
    return render_template('pages-sign-out')

@app.route('/blank')
def maps():
    return render_template('pages-blank')

@app.route('/')
def maps():
    return render_template('')

@app.route('/')
def maps():
    return render_template('')

@app.route('/')
def maps():
    return render_template('')












if __name__ == '__main__':
    app.run(debug = True)