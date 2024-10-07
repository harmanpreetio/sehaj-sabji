from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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
    sabji_list = [
        {"name": "Allo", "qty": "1kg"},
        {"name": "Pyaaz", "qty": "2kg"},
        {"name": "Tamatar", "qty": "1kg"},
    ]
    return render_template("dashboard.html", sabji_list=sabji_list)

@app.route("/add-sabji", methods=["GET", "POST"])
def add_sabji():
    if request.method == "POST":
        # TODO: logic to process sabji addition
        print(request.form)
        return redirect("/dashboard")
    return render_template("add_sabji.html")

if __name__ == "__main__":
    app.run(debug=True)