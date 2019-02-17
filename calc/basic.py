
from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
# from common import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'calculatorkey'

class infoForm(FlaskForm):
    number1 = StringField("First Number: ")
    number2 = StringField("Second Number: ")
    submit = SubmitField("Submit")

@app.route('/', methods = ['GET', 'POST'])
def index():
    
    n1 = False
    n2 = False
    form = infoForm()
    if form.validate_on_submit():
       session['n1'] = form.number1.data
       session['n2'] = form.number2.data
       return redirect(url_for("result"))

    return render_template('index.html',form=form)

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)