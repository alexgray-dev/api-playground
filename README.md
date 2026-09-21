# API Playground

Flask API playground with in-memory user and product stores, a pytest suite, and example requests/responses.

## Requirements

- Python 3.10+

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The API runs on http://localhost:5000.

## API

| Method | Path | Description |
| --- | --- | --- |
| GET | `/api/health` | Health check |
| GET | `/api/users` | List users |
| POST | `/api/users` | Create a user (`name`, `email`) |
| GET | `/api/users/<user_id>` | Get a user |
| DELETE | `/api/users/<user_id>` | Delete a user |
| GET | `/api/products` | List products |
| POST | `/api/products` | Create a product (`name`, `price`, optional `in_stock`) |
| GET | `/api/products/<product_id>` | Get a product |
| DELETE | `/api/products/<product_id>` | Delete a product |

Example:

```bash
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Ada Lovelace","email":"ada@example.com"}'
```

## Tests

```bash
pytest
```

Sample payloads to try are in `examples/requests.json` with matching sample responses in `examples/responses.json`.

## Project structure

```
api-playground/
├── app/
│   ├── __init__.py             App factory
│   ├── routes.py               Blueprint with /api routes
│   ├── models.py               In-memory user and product stores
│   └── config.py               Configuration classes
├── tests/
│   ├── test_users.py
│   └── test_products.py
├── examples/
│   ├── requests.json
│   └── responses.json
├── requirements.txt
├── app.py                       Entry point
├── README.md
└── .gitignore
```
