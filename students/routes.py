"""HTTP-роуты учеников."""
from flask import Blueprint, jsonify

bp = Blueprint("students", __name__, url_prefix="/students")


@bp.get("/")
def list_students():
    """Список учеников."""
    return jsonify({"students": []})