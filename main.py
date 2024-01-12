from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
# Class to create form with 
class MyLoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Login')

app = Flask(__name__)
# secret key for csrf_token
app.secret_key = "ilh1j3ih12l"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods={"GET", "POST"})
def login():
    login_form = MyLoginForm()  #  create variable to passon login form to html
    login_form.validate_on_submit() # Validates form is properly filled
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
