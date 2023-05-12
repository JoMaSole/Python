#pip install flask
from flask import Flask, render_template

app = Flask(__name__)


#nueva ruta
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('pages-profile.html')

@app.route('/sign-in')
def signIn():
    return render_template('pages-sign-in.html')

@app.route('/contact')
def signOut():
    return render_template('pages-contact.html')

@app.route('/study')
def blank():
    return render_template('pages-study.html')

@app.route('/maps')
def maps():
    return render_template('maps-google.html')

@app.route('/inicio')
def inicio():
    return render_template('layout.html')



# @app.route('/')
# def maps():
#     return render_template('')



if __name__ == '__main__':
    app.run(debug = True)