from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    items = ["salad", "bread", "water"]
    return render_template("index.html", bb="behnam", cc="fff", items=items)


if __name__ == "__main__":
    app.run(debug=True)
