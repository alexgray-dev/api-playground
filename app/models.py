import uuid
from datetime import datetime, timezone


def _timestamp():
    return datetime.now(timezone.utc).isoformat()


class InMemoryStore:
    def __init__(self):
        self._items = {}

    def list(self):
        return list(self._items.values())

    def get(self, item_id):
        return self._items.get(item_id)

    def add(self, item):
        self._items[item["id"]] = item
        return item

    def delete(self, item_id):
        return self._items.pop(item_id, None)

    def clear(self):
        self._items = {}


class UserStore(InMemoryStore):
    def create(self, data):
        return self.add(
            {
                "id": str(uuid.uuid4()),
                "name": data["name"],
                "email": data["email"],
                "created_at": _timestamp(),
            }
        )


class ProductStore(InMemoryStore):
    def create(self, data):
        return self.add(
            {
                "id": str(uuid.uuid4()),
                "name": data["name"],
                "price": float(data["price"]),
                "in_stock": bool(data.get("in_stock", True)),
                "created_at": _timestamp(),
            }
        )


users = UserStore()
products = ProductStore()
