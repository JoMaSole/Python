#pip install flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

#nueva ruta
@app.route('/profile')
def profile():
    return render_template('pages-profile.html')

@app.route('/sign-in')
def signIn():
    return render_template('pages-sign-in.html')

@app.route('/sign-up')
def signOut():
    return render_template('pages-sign-up.html')

@app.route('/blank')
def blank():
    return render_template('pages-blank.html')

@app.route('/maps')
def maps():
    return render_template('maps-google.html')

# @app.route('/')
# def maps():
#     return render_template('')

# @app.route('/')
# def maps():
#     return render_template('')












if __name__ == '__main__':
    app.run(debug = True)