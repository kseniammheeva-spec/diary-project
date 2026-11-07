"""HTTP-роуты оценок."""

from flask import Blueprint, jsonify

bp = Blueprint("grades", __name__, url_prefix="/grades")


@bp.get("/")
def list_grades():
    return jsonify({"grades": []})
