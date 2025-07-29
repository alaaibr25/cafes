from flask import Flask, render_template, redirect ,request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, URLField, TimeField, SelectField
from flask_bootstrap import Bootstrap5



class CafeForm(FlaskForm):
    name = StringField('Cafe name', [validators.DataRequired(message="fill the field.")] )
    loc = URLField('Location', [validators.URL(require_tld=False)])
    open = TimeField()
    close = TimeField()
    coffee = SelectField(choices=['⭐', '⭐⭐', '⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'])
    wifi = SelectField(choices=['⭐', '⭐⭐', '⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'])
    power = SelectField(choices=['⭐', '⭐⭐', '⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.secret_key = "ndwkcns8uh3jkqwnms"


bootstrap = Bootstrap5(app)

#//video:

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/cafe')
def all_cafes():
    with open("cafe-data.csv", encoding="utf8") as f:
        list_cafes = f.readlines()
        lista = [x.strip("\n").rsplit(",") for x in list_cafes]

        return render_template("cafes.html", all_cafes=lista, list_cafes=list_cafes)


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    cfForm = CafeForm()
    if cfForm.validate_on_submit() and request.method == 'POST':

        with open("cafe-data.csv", "a", encoding="utf8") as f:
            f.write(f"{request.form['name']},"
                    f"{request.form['loc']},"
                    f"{request.form['open']},"
                    f"{request.form['close']},"
                    f"{request.form['coffee']},"
                    f"{request.form['wifi']},"
                    f"{request.form['power']}")
            return redirect('/cafe')

    return render_template("add.html", form=cfForm)


app.run(debug=True)
