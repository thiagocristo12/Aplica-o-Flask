from flask import Blueprint

hello_bp = Blueprint("hello", __name__)

@hello_bp.route("/")
def index():
    return "òla, Mundo"

@hello_bp.route("/sobre")
def sobre():
    return "Óla, Thiago"

