from flask import Blueprint, jsonify, request, make_response

order_blueprint = Blueprint("order_api_routes", __name__, url_prefix="/api/order")


@order_blueprint.route("/", methods=["GET"])
def get_order():
    return "get_order"


@order_blueprint.route("/all", methods=["GET"])
def all_orders():
    return "all_orders"


@order_blueprint.route("/add-order", methods=["POST"])
def add_order():
    return "add item"
