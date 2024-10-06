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


if __name__ == "__main__":
    app.run(debug=True)