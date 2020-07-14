from flask import Flask, render_template,url_for
import os
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('random', id="1"))

@app.route('/<id>')
def random(id):
    return id
def mail():

    return "^^FLAG^^\n"

if __name__ == '__main__':
    app.run(port=8080)
