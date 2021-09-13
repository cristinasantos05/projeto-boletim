from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', name='página inicial')

@app.route("/login/<name>")
def login(name):
    return f'Seja bem vindo, {name}!'

@app.route("/<val>")
def match_num(val) ->str:
    return f'{val}'
