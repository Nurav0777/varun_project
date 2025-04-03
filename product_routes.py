from flask import Blueprint, request, jsonify
from services.product_service import ProductService

product_bp = Blueprint("product", __name__)

@product_bp.route("/products", methods=["GET"])
def get_products():
    return jsonify(ProductService.get_products())

@product_bp.route("/products", methods=["POST"])
def add_product():
    data = request.json
    return ProductService.add_product(data["name"], data["price"])
