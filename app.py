import os
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_expenses_filename(month, year):
    return f"{month:02d}-{year}-expenses.json"

def load_expenses(month, year):
    filename = get_expenses_filename(month, year)
    if os.path.exists("/expense-data/" + filename):
        with open("/expense-data/" + filename, "r") as f:
            return json.load(f)
    return []

def save_expenses(month, year, expenses):
    filename = get_expenses_filename(month, year)
    with open("/expense-data/" + filename, "w") as f:
        json.dump(expenses, f, indent=4)

def get_current_month_year():
    import datetime
    now = datetime.datetime.now()
    return now.month, now.year

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        date = request.form["date"]
        category = request.form["category"].lower()
        amount = float(request.form["amount"])
        note = request.form["note"]
        _, month, year = map(int, date.split("-"))
        expenses = load_expenses(month, year)
        expenses.append({"date": date, "category": category, "amount": amount, "note": note})
        save_expenses(month, year, expenses)
    month, year = get_current_month_year()
    return redirect(url_for("show_expenses", month=month, year=year))

@app.route("/expenses")
def show_expenses():
    month = int(request.args.get("month", 0))
    year = int(request.args.get("year", 0))
    if not month or not year:
        month, year = get_current_month_year()
    expenses = load_expenses(month, year)
    return render_template("showcase.html", expenses=expenses, month=month, year=year)

if __name__ == "__main__":
    app.run(debug=True)
