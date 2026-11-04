"""Точка входа приложения «Электронный дневник»."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Электронный дневник"


if __name__ == "__main__":
    app.run(debug=True)