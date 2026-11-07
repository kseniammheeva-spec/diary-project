"""HTTP-роуты расписания."""
from flask import Blueprint, jsonify

bp = Blueprint("schedule", __name__, url_prefix="/schedule")

@bp.get("/")
def list_schedule():
    return jsonify({"schedule": []})