"""Точка входа приложения «Электронный дневник»."""

from flask import Flask

from core.config import Config
from grades.routes import bp as grades_bp
from students.routes import bp as students_bp

# и т.д.

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(students_bp)
app.register_blueprint(grades_bp)


@app.route("/")
def index():
    return "Электронный дневник"


if __name__ == "__main__":
    app.run(debug=True)
