from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from flask_bootstrap import Bootstrap4


app = Flask(__name__)
app.secret_key = "KEY"



@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/cafe')
def all_cafes():
    return render_template("cafes.html")


@app.route('/add')
def add_cafe():
    return render_template("add.html")










app.run(debug=True)
