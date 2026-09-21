from flask import Blueprint, jsonify, request

from .models import products, users

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.get("/health")
def health():
    return jsonify(status="ok")


@bp.get("/users")
def list_users():
    return jsonify(users.list())


@bp.post("/users")
def create_user():
    payload = request.get_json(silent=True) or {}
    if not payload.get("name") or not payload.get("email"):
        return jsonify(error="name and email are required"), 400
    return jsonify(users.create(payload)), 201


@bp.get("/users/<user_id>")
def get_user(user_id):
    user = users.get(user_id)
    if user is None:
        return jsonify(error="user not found"), 404
    return jsonify(user)


@bp.delete("/users/<user_id>")
def delete_user(user_id):
    if users.delete(user_id) is None:
        return jsonify(error="user not found"), 404
    return "", 204


@bp.get("/products")
def list_products():
    return jsonify(products.list())


@bp.post("/products")
def create_product():
    payload = request.get_json(silent=True) or {}
    if not payload.get("name") or payload.get("price") is None:
        return jsonify(error="name and price are required"), 400
    return jsonify(products.create(payload)), 201


@bp.get("/products/<product_id>")
def get_product(product_id):
    product = products.get(product_id)
    if product is None:
        return jsonify(error="product not found"), 404
    return jsonify(product)


@bp.delete("/products/<product_id>")
def delete_product(product_id):
    if products.delete(product_id) is None:
        return jsonify(error="product not found"), 404
    return "", 204
