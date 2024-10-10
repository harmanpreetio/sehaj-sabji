from flask import Flask, render_template, request, redirect
from src.models.db import db
from src.models import Sabji, User
from sqlalchemy import select

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:example@localhost:5432/sabji"

db.init_app(app)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.form)
        # TODO: logic to process login feature
        return redirect("/")
    return render_template("login.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    # TODO: fetch sabji list from database
    # convert to list
    stmt = select(Sabji)
    sabji_list = db.session.scalars(stmt).all()
    return render_template("dashboard.html", sabji_list=sabji_list)

@app.route("/add-sabji", methods=["GET", "POST"])
def add_sabji():
    if request.method == "POST":
        sabji = Sabji()
        sabji.name = request.form["name"]
        sabji.qty = request.form["qty"]
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