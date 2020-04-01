from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homapage():
    return "Интернет-магазин мебели"

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/list1")
def list1():
    return render_template("list1.html")


@app.route("/special/<name>")
def hello(name):
    name = name.capitalize()
    return render_template("special.html", name=name)
