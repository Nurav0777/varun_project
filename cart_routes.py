from flask import Blueprint, request, jsonify
from services.cart_service import CartService

cart_bp = Blueprint("cart", __name__)

@cart_bp.route("/cart/add", methods=["POST"])
def add_to_cart():
    data = request.json
    return CartService.add_to_cart(data["user_id"], data["product_id"])

@cart_bp.route("/cart/remove", methods=["POST"])
def remove_from_cart():
    data = request.json
    return CartService.remove_from_cart(data["user_id"], data["product_id"])
