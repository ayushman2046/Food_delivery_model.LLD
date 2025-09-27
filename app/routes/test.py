
from flask import Blueprint, jsonify


test_bp = Blueprint("test", __name__)

@test_bp.route("/test", methods = ["POST"])
def test():
    return jsonify({"message" : "success"}), 200
