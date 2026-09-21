import pytest

from app import create_app
from app.config import TestingConfig
from app.models import products


@pytest.fixture()
def client():
    products.clear()
    return create_app(TestingConfig).test_client()


def test_list_products_empty(client):
    res = client.get("/api/products")
    assert res.status_code == 200
    assert res.get_json() == []


def test_create_product(client):
    res = client.post(
        "/api/products",
        json={"name": "Mechanical Keyboard", "price": 89.99, "in_stock": True},
    )
    assert res.status_code == 201
    body = res.get_json()
    assert body["name"] == "Mechanical Keyboard"
    assert body["price"] == 89.99
    assert body["in_stock"] is True
    assert "id" in body


def test_create_product_defaults_in_stock(client):
    res = client.post("/api/products", json={"name": "Mouse", "price": 19.5})
    assert res.status_code == 201
    assert res.get_json()["in_stock"] is True


def test_create_product_requires_name_and_price(client):
    res = client.post("/api/products", json={"name": "No Price"})
    assert res.status_code == 400
    assert "error" in res.get_json()


def test_get_product(client):
    created = client.post("/api/products", json={"name": "Monitor", "price": 249.0})
    product_id = created.get_json()["id"]
    res = client.get(f"/api/products/{product_id}")
    assert res.status_code == 200
    assert res.get_json()["name"] == "Monitor"


def test_get_missing_product(client):
    res = client.get("/api/products/does-not-exist")
    assert res.status_code == 404


def test_delete_product(client):
    created = client.post("/api/products", json={"name": "Webcam", "price": 45.0})
    product_id = created.get_json()["id"]
    assert client.delete(f"/api/products/{product_id}").status_code == 204
    assert client.get(f"/api/products/{product_id}").status_code == 404
