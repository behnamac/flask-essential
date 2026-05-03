from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    user = {"username": "Natasha"}
    items = [
        "bread",
        "milk",
        "eggs",
        "coffee",
        "apples",
        "olive oil",
    ]
    return render_template(
        "index.html",
        title="Home",
        user=user,
        items=items,
        year=datetime.now().year,
    )


@app.route("/welcome")
def welcome():
    return render_template("welcome.html", year=datetime.now().year)


if __name__ == "__main__":
    app.run(debug=True)
