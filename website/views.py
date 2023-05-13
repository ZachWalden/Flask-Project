from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route("/")   #@name of blueprint
def home():
    return render_template("home.html")

@views.route('/table')
def table():
    return render_template("table.html")