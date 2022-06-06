from flask import Flask, url_for, render_template, request, redirect, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField,PasswordField
from wtforms import validators
from wtforms.validators import DataRequired,Length,EqualTo, Email 
import os.path
import os 


TEMPLATE_DIR = os.path.abspath("Extractor_APP\templates")
STATIC_DIR = os.path.abspath("Extractor_APP\static")
IMAGE_FOLDER = os.path.join("static", "images")


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = IMAGE_FOLDER
app.config['SECRET_KEY'] = 'the random string' 

bootstrap = Bootstrap(app)


#REGISTRATION CLASS
class RegistrationForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(),Length(min=3,max=20)])
    email = StringField(label="Email",validators=[DataRequired(),Email()])
    password = PasswordField(label="Password", validators=[DataRequired(),Length(min=6,max=16)])
    confirm_password = PasswordField(label="Confirm password", validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField(label="Sign Up")


#LOGIN CLASS
class LoginForm(FlaskForm):
    email = StringField(label="Email",validators=[DataRequired(),Email()])
    password = PasswordField(label="Password", validators=[DataRequired(),Length(min=6,max=16)])
    submit = SubmitField(label="Login")


#HOME CONFIG
@app.route("/")
def home():
    full_filename = os.path.join(app.config["UPLOAD_FOLDER"], "extractor.png")
    icon_fillname = os.path.join(app.config["UPLOAD_FOLDER"], "favicon.ico")   
    return render_template("index_base.html", user_image = full_filename, icon_image = icon_fillname, title="Home")


#GAMES CONFIG
@app.route("/games")
def games():
    icon_fillname = os.path.join(app.config["UPLOAD_FOLDER"], "favicon.ico")
    r6_full_filename = os.path.join(app.config["UPLOAD_FOLDER"], "r6siege.jpg")
    return render_template("index_games.html",title="Games", icon_image = icon_fillname,r6_image = r6_full_filename)


#STATUTE CONFIG
@app.route("/statute")
def statute():
    icon_fillname = os.path.join(app.config["UPLOAD_FOLDER"], "favicon.ico")  
    return render_template("index_statute.html",title="Statute", icon_image = icon_fillname)


#TEAM_MEMBERS CONFIG
@app.route("/teammembers")
def team():
    icon_fillname = os.path.join(app.config["UPLOAD_FOLDER"], "favicon.ico")  
    full_filename = os.path.join(app.config["UPLOAD_FOLDER"], "papaj.png")
    return render_template("index_teammembers.html",title="Team Members", icon_image = icon_fillname,testo_image = full_filename)

#RECRUITMENT CONFIG
@app.route("/account")
def account():
    icon_fillname = os.path.join(app.config["UPLOAD_FOLDER"], "favicon.ico")  
    return render_template("index_account.html",title="Account", icon_image = icon_fillname)


#REGISTER CONFIG
@app.route("/register",methods=['POST','GET'])
def register():
    icon_fillname = os.path.join(app.config["UPLOAD_FOLDER"], "favicon.ico")  
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created succesfully for {form.username.data}", category=success)
        return redirect(url_for("login"))
    return render_template("index_registration.html",title="Register", form=form, icon_image = icon_fillname)


#LOGIN CONFIG
@app.route("/login", methods=["GET","POST"])
def login():
    icon_fillname = os.path.join(app.config["UPLOAD_FOLDER"], "favicon.ico")  
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data==form.email and form.password.data==form.password: 
            flash(f"Login succesful for {form.username.data}", category=success)
            return redirect(url_for("account"))
        else:
            flash(f"Login unsuccessful for {form.username.data}", category=danger)
    return render_template('index_login.html', icon_image = icon_fillname)


if __name__ == "__main__":
    app.run(debug=True)