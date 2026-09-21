import pytest

from app import create_app
from app.config import TestingConfig
from app.models import users


@pytest.fixture()
def client():
    users.clear()
    return create_app(TestingConfig).test_client()


def test_list_users_empty(client):
    res = client.get("/api/users")
    assert res.status_code == 200
    assert res.get_json() == []


def test_create_user(client):
    res = client.post("/api/users", json={"name": "Ada Lovelace", "email": "ada@example.com"})
    assert res.status_code == 201
    body = res.get_json()
    assert body["name"] == "Ada Lovelace"
    assert body["email"] == "ada@example.com"
    assert "id" in body
    assert "created_at" in body


def test_create_user_requires_name_and_email(client):
    res = client.post("/api/users", json={"name": "No Email"})
    assert res.status_code == 400
    assert "error" in res.get_json()


def test_get_user(client):
    created = client.post("/api/users", json={"name": "Grace Hopper", "email": "grace@example.com"})
    user_id = created.get_json()["id"]
    res = client.get(f"/api/users/{user_id}")
    assert res.status_code == 200
    assert res.get_json()["email"] == "grace@example.com"


def test_get_missing_user(client):
    res = client.get("/api/users/does-not-exist")
    assert res.status_code == 404


def test_delete_user(client):
    created = client.post("/api/users", json={"name": "Alan Turing", "email": "alan@example.com"})
    user_id = created.get_json()["id"]
    assert client.delete(f"/api/users/{user_id}").status_code == 204
    assert client.get(f"/api/users/{user_id}").status_code == 404
