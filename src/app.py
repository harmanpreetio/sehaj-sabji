from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from src.models.db import db
from src.models import Sabji, User
from sqlalchemy import select

app = Flask(__name__)
login_manager = LoginManager()
login_manager.login_view = "login" # type: ignore

app.secret_key = "alwdjwalkjdwaljcklwacnlkwancklwajcladjwalwj"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:example@localhost:5432/sabji"

db.init_app(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.form)
        # TODO: logic to process login feature
        email = request.form["email"]
        passwd = request.form['passwd']
        stmt = select(User).where(User.email == email)
        user = db.session.scalars(stmt).first()
        if user is not None and user.passwd == passwd:
            login_user(user)
            return redirect("/dashboard")
    return render_template("login.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
@login_required
def dashboard():
    # TODO: fetch sabji list from database
    # convert to list
    stmt = select(Sabji).where(Sabji.user_id == current_user.id)
    sabji_list = db.session.scalars(stmt).all()
    return render_template("dashboard.html", sabji_list=sabji_list)

@app.route("/add-sabji", methods=["GET", "POST"])
def add_sabji():
    if request.method == "POST":
        if current_user.is_authenticated:
            sabji = Sabji()
            sabji.name = request.form["name"]
            sabji.qty = request.form["qty"]
            sabji.user_id = current_user.id
            db.session.add(sabji)
            db.session.commit()
        return redirect("/dashboard")
    return render_template("add_sabji.html")

@app.route("/delete-sabji/<id>", methods=["GET"])
def delete_sabji(id):
    stmt = select(Sabji).where(Sabji.id == id)
    sabji = db.session.scalars(stmt).first()
    if sabji is not None:
        db.session.delete(sabji)
        db.session.commit()
    return redirect("/dashboard")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user = User()
        user.email = request.form["email"]
        user.passwd = request.form['passwd']
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    return render_template("signup.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")