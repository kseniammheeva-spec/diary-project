"""HTTP-роуты домашних заданий."""

from flask import Blueprint, jsonify

bp = Blueprint("homework", __name__, url_prefix="/homework")


@bp.get("/")
def list_homework():
    return jsonify({"homework": []})
