# 🛒 Storefront API

A full-featured e-commerce application. This RESTful API supports CRUD operations, search, sorting, pagination, and secure authentication and authorization with JSON Web Tokens (JWT).

### 🌐 [Live Demo → sherybuy-prod-8c19f1a2a82c.herokuapp.com](https://sherybuy-prod-8c19f1a2a82c.herokuapp.com/)

[![GitHub](https://img.shields.io/badge/GitHub-ShehryarAzhar-181717?style=for-the-badge&logo=github)](https://github.com/ShehryarAzhar)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![DRF](https://img.shields.io/badge/DRF-3.x-A30000?style=for-the-badge)](https://django-rest-framework.org)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://mysql.com)

---

## 📖 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 Getting Started](#-getting-started)
- [🐳 Optional Services (Docker)](#-optional-services-docker)
- [🖥️ Admin Panel](#️-admin-panel)
- [🔑 Environment Variables](#-environment-variables)
- [📘 API Reference](#-api-reference)
  - [🔐 Authentication](#-authentication)
  - [👤 Users](#-users)
  - [📦 Products](#-products)
  - [🖼️ Product Images](#️-product-images)
  - [⭐ Reviews](#-reviews)
  - [🗂️ Collections](#️-collections)
  - [🛒 Carts](#-carts)
  - [🧺 Cart Items](#-cart-items)
  - [📋 Orders](#-orders)
  - [👥 Customers](#-customers)
- [🧪 Testing](#-testing)
- [🚧 Planned Features](#-planned-features)
- [🌐 Deployment](#-deployment)
- [👨‍💻 Author](#-author)

---

## ✨ Features

|     | Feature                | Description                                                      |
| --- | ---------------------- | ---------------------------------------------------------------- |
| 🔐  | **JWT Authentication** | Secure token-based auth via `djangorestframework-simplejwt`      |
| 🛍️  | **Product Management** | Full CRUD with filtering, search, and ordering                   |
| 🖼️  | **Image Uploads**      | Upload and manage product images, validated via Pillow           |
| ⭐  | **Reviews**            | Nested per-product reviews with full CRUD                        |
| 🛒  | **Cart System**        | Anonymous UUID-based carts with smart item management            |
| 📋  | **Order Processing**   | Cart-to-order conversion with full order history                 |
| 🔍  | **Filtering & Search** | Filter by collection, search by title/description, sort by price |
| 🗺️  | **Nested Routing**     | Clean nested endpoints via `drf-nested-routers`                  |
| ☁️  | **Production Ready**   | Deployed on Heroku with MySQL                                    |

---

## 🛠️ Tech Stack

| Category           | Technology                                                   |
| ------------------ | ------------------------------------------------------------ |
| **Backend**        | Django 4.x + Django REST Framework                           |
| **Authentication** | `djangorestframework-simplejwt` + Djoser                     |
| **Database**       | MySQL                                                        |
| **Storage**        | Pillow _(image processing & validation)_                     |
| **Task Queue**     | Celery + Redis _(infrastructure ready)_                      |
| **Caching**        | Redis via `django-redis` _(infrastructure ready)_            |
| **Email**          | Mailgun _(production)_ · smtp4dev _(development)_            |
| **Testing**        | pytest · pytest-django · model-bakery · Locust · django-silk |
| **Deployment**     | Heroku · gunicorn · whitenoise                               |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Pipenv (`pip install pipenv`)
- MySQL
- Docker _(for Redis and smtp4dev)_

### 1. Clone & Install

```bash
git clone https://github.com/ShehryarAzhar/storefront.git
cd storefront
pipenv install
pipenv shell
```

### 2. Configure Local Settings

Open `storefront/settings/dev.py` and update the database credentials to match your local MySQL setup:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',      # your database name
        'HOST': 'localhost',
        'USER': 'root',             # your MySQL username
        'PASSWORD': 'yourpassword'  # your MySQL password
    }
}
```

> 💡 No `.env` file needed — all other dev settings are pre-configured in `storefront/settings/dev.py`.

### 3. Apply Migrations & Create Superuser

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4. Start the Development Server

```bash
python manage.py runserver
```

> API is available at `http://127.0.0.1:8000/`

---

## 🐳 Optional Services (Docker)

The following services are optional depending on which features you want to run locally. All can be started with Docker.

### 📧 Email — smtp4dev (Fake SMTP Server)

A fake SMTP server for catching and inspecting emails during development.

```bash
docker run --rm -it -p 5000:80 -p 2525:25 -p 110:110 rnwood/smtp4dev
```

- **smtp4dev UI** available at `http://localhost:5000`
- Already configured in `dev.py` — `EMAIL_HOST=localhost`, `EMAIL_PORT=2525`

### 🗄️ Redis — Background Tasks & Caching

Both Celery (background tasks) and Redis caching share the same Redis instance:

```bash
docker run -d -p 6379:6379 redis
```

**Run the Celery worker:**

```bash
celery -A storefront worker
```

**Run the Celery beat scheduler** _(for periodic tasks)_:

```bash
celery -A storefront beat
```

> ⚠️ **Windows users:** Celery 4+ is not supported natively on Windows. Use [WSL](https://learn.microsoft.com/en-us/windows/wsl/) to run Celery commands.

---

## 🖥️ Admin Panel

The Django Admin panel is available at `/admin` and provides a full management interface for the entire application.

|                | URL                                                      |
| -------------- | -------------------------------------------------------- |
| **Local**      | `http://127.0.0.1:8000/admin`                            |
| **Production** | `https://sherybuy-prod-8c19f1a2a82c.herokuapp.com/admin` |

You can manage products, collections, orders, customers, users, and more directly from the admin panel without touching the API.

> 💡 Use the superuser account created during setup to log in. The admin panel is branded as **Storefront Admin**.

---

## 🔑 Environment Variables

This project uses **split settings** — no environment variables are needed to run locally.

| File                            | Purpose                                                           |
| ------------------------------- | ----------------------------------------------------------------- |
| `storefront/settings/common.py` | Shared settings across all environments                           |
| `storefront/settings/dev.py`    | Local development — hardcoded DB, Redis, and email config         |
| `storefront/settings/prod.py`   | Production — all sensitive values read from environment variables |

The following environment variables are required **only when deploying to production** (e.g. Heroku):

| Variable                 | Set By              | Description                       |
| ------------------------ | ------------------- | --------------------------------- |
| `SECRET_KEY`             | Manual              | Django secret key                 |
| `DJANGO_SETTINGS_MODULE` | Manual              | Set to `storefront.settings.prod` |
| `DATABASE_URL`           | JawsDB add-on       | MySQL connection URL              |
| `JAWSDB_URL`             | JawsDB add-on       | MySQL connection URL (alias)      |
| `REDISCLOUD_URL`         | Redis® Cloud add-on | Redis connection URL              |
| `MAILGUN_API_KEY`        | Mailgun add-on      | Mailgun API key                   |
| `MAILGUN_DOMAIN`         | Mailgun add-on      | Mailgun sending domain            |
| `MAILGUN_PUBLIC_KEY`     | Mailgun add-on      | Mailgun public key                |
| `MAILGUN_SMTP_SERVER`    | Mailgun add-on      | SMTP hostname                     |
| `MAILGUN_SMTP_LOGIN`     | Mailgun add-on      | SMTP username                     |
| `MAILGUN_SMTP_PASSWORD`  | Mailgun add-on      | SMTP password                     |
| `MAILGUN_SMTP_PORT`      | Mailgun add-on      | SMTP port                         |

> 💡 Variables marked **add-on** are automatically set by Heroku when the add-on is provisioned. You only need to manually set `SECRET_KEY` and `DJANGO_SETTINGS_MODULE`.

> ⚠️ Never commit `storefront/settings/dev.py` credentials to a public repository.

---

## 📘 API Reference

**Base URL:** `https://sherybuy-prod-8c19f1a2a82c.herokuapp.com`

| Symbol | Meaning                                             |
| ------ | --------------------------------------------------- |
| 🌐     | Public — no authentication required                 |
| 🔑     | Requires `Authorization: JWT <access_token>` header |
| 🔴     | Admin only — requires staff privileges              |

---

### 🔐 Authentication

**Prefix:** `/auth/jwt/`

| Method | Endpoint             | Description                     | Auth |
| ------ | -------------------- | ------------------------------- | ---- |
| `POST` | `/auth/jwt/create/`  | Obtain access & refresh tokens  | 🌐   |
| `POST` | `/auth/jwt/refresh/` | Refresh an expired access token | 🌐   |
| `POST` | `/auth/jwt/verify/`  | Verify token validity           | 🌐   |

#### `POST /auth/jwt/create/` — Request Body

| Field      | Type   | Required |
| ---------- | ------ | -------- |
| `username` | string | ✅ Yes   |
| `password` | string | ✅ Yes   |

**Response:** Returns `access` and `refresh` tokens.

> 💡 Use the access token in all protected requests as: `Authorization: JWT <access_token>`

---

### 👤 Users

**Prefix:** `/auth/users/` — powered by Djoser

| Method | Endpoint          | Description                 | Auth |
| ------ | ----------------- | --------------------------- | ---- |
| `POST` | `/auth/users/`    | Register a new user         | 🌐   |
| `GET`  | `/auth/users/me/` | Get current user profile    | 🔑   |
| `PUT`  | `/auth/users/me/` | Update current user profile | 🔑   |

#### `POST /auth/users/` — Request Body

| Field        | Type   | Required    |
| ------------ | ------ | ----------- |
| `username`   | string | ✅ Yes      |
| `email`      | string | ✅ Yes      |
| `password`   | string | ✅ Yes      |
| `first_name` | string | ➖ Optional |
| `last_name`  | string | ➖ Optional |

#### `GET /auth/users/me/` — Response

| Field        | Type    |
| ------------ | ------- |
| `id`         | integer |
| `username`   | string  |
| `email`      | string  |
| `first_name` | string  |
| `last_name`  | string  |

---

### 📦 Products

**Prefix:** `/store/products/`

| Method   | Endpoint                | Description                           | Auth |
| -------- | ----------------------- | ------------------------------------- | ---- |
| `GET`    | `/store/products/`      | List all products                     | 🌐   |
| `POST`   | `/store/products/`      | Create a product                      | 🔴   |
| `GET`    | `/store/products/{id}/` | Retrieve a product with nested images | 🌐   |
| `PUT`    | `/store/products/{id}/` | Full update                           | 🔴   |
| `PATCH`  | `/store/products/{id}/` | Partial update                        | 🔴   |
| `DELETE` | `/store/products/{id}/` | Delete product                        | 🔴   |

#### Query Parameters — `GET /store/products/`

| Parameter       | Example                 | Description                |
| --------------- | ----------------------- | -------------------------- |
| `collection_id` | `?collection_id=2`      | Filter by collection       |
| `search`        | `?search=laptop`        | Search title & description |
| `ordering`      | `?ordering=unit_price`  | Sort by price ascending    |
| `ordering`      | `?ordering=-unit_price` | Sort by price descending   |
| `ordering`      | `?ordering=last_update` | Sort by last updated       |
| `page`          | `?page=2`               | Paginate results           |

#### Response Fields

| Field            | Type    | Description                     |
| ---------------- | ------- | ------------------------------- |
| `id`             | integer |                                 |
| `title`          | string  |                                 |
| `description`    | string  | Nullable                        |
| `slug`           | string  |                                 |
| `inventory`      | integer | Stock count                     |
| `unit_price`     | decimal |                                 |
| `price_with_tax` | decimal | `unit_price × 1.1` — read-only  |
| `collection`     | integer | Collection ID                   |
| `images`         | array   | List of `{ id, image }` objects |

> ⚠️ `DELETE` returns `405 Method Not Allowed` if the product is referenced by any order item.

---

### 🖼️ Product Images

**Prefix:** `/store/products/{product_id}/images/` — nested resource

| Method   | Endpoint                                    | Description                   | Auth |
| -------- | ------------------------------------------- | ----------------------------- | ---- |
| `GET`    | `/store/products/{product_id}/images/`      | List all images for a product | 🌐   |
| `POST`   | `/store/products/{product_id}/images/`      | Upload a product image        | 🔴   |
| `GET`    | `/store/products/{product_id}/images/{id}/` | Retrieve a single image       | 🌐   |
| `DELETE` | `/store/products/{product_id}/images/{id}/` | Delete a product image        | 🔴   |

#### `POST` — Upload Image

Content-Type: `multipart/form-data`

| Field   | Type | Required |
| ------- | ---- | -------- |
| `image` | file | ✅ Yes   |

> File size is validated server-side. Images stored under `store/images/`.

---

### ⭐ Reviews

**Prefix:** `/store/products/{product_id}/reviews/` — nested resource

| Method   | Endpoint                                     | Description                    | Auth |
| -------- | -------------------------------------------- | ------------------------------ | ---- |
| `GET`    | `/store/products/{product_id}/reviews/`      | List all reviews for a product | 🌐   |
| `POST`   | `/store/products/{product_id}/reviews/`      | Create a review                | 🌐   |
| `GET`    | `/store/products/{product_id}/reviews/{id}/` | Retrieve a review              | 🌐   |
| `PUT`    | `/store/products/{product_id}/reviews/{id}/` | Update a review                | 🌐   |
| `DELETE` | `/store/products/{product_id}/reviews/{id}/` | Delete a review                | 🌐   |

#### `POST` / `PUT` — Request Body

| Field         | Type   | Required |
| ------------- | ------ | -------- |
| `name`        | string | ✅ Yes   |
| `description` | string | ✅ Yes   |

#### Response Fields

| Field         | Type    | Description          |
| ------------- | ------- | -------------------- |
| `id`          | integer |                      |
| `name`        | string  | Reviewer name        |
| `description` | string  | Review body          |
| `date`        | date    | Auto-set on creation |

---

### 🗂️ Collections

**Prefix:** `/store/collections/`

| Method   | Endpoint                   | Description           | Auth |
| -------- | -------------------------- | --------------------- | ---- |
| `GET`    | `/store/collections/`      | List all collections  | 🌐   |
| `POST`   | `/store/collections/`      | Create a collection   | 🔴   |
| `GET`    | `/store/collections/{id}/` | Retrieve a collection | 🌐   |
| `PUT`    | `/store/collections/{id}/` | Update a collection   | 🔴   |
| `DELETE` | `/store/collections/{id}/` | Delete a collection   | 🔴   |

#### Response Fields

| Field            | Type    | Description               |
| ---------------- | ------- | ------------------------- |
| `id`             | integer |                           |
| `title`          | string  |                           |
| `products_count` | integer | Read-only, auto-annotated |

> ⚠️ `DELETE` returns `405 Method Not Allowed` if the collection contains any products.

---

### 🛒 Carts

**Prefix:** `/store/carts/`

| Method   | Endpoint               | Description                            | Auth |
| -------- | ---------------------- | -------------------------------------- | ---- |
| `POST`   | `/store/carts/`        | Create a new anonymous cart            | 🌐   |
| `GET`    | `/store/carts/{uuid}/` | Retrieve cart with items & total price | 🌐   |
| `DELETE` | `/store/carts/{uuid}/` | Delete a cart                          | 🌐   |

#### `POST /store/carts/` — Response

| Field         | Type    | Description                                        |
| ------------- | ------- | -------------------------------------------------- |
| `id`          | UUID    | **Save this** — used for all cart & order requests |
| `items`       | array   | Empty on creation                                  |
| `total_price` | decimal | `0.00` on creation                                 |

> 💡 Carts are **anonymous** — no auth required. The cart is automatically deleted when converted to an order.

---

### 🧺 Cart Items

**Prefix:** `/store/carts/{cart_id}/items/` — nested resource

| Method   | Endpoint                             | Description              | Auth |
| -------- | ------------------------------------ | ------------------------ | ---- |
| `GET`    | `/store/carts/{cart_id}/items/`      | List all items in a cart | 🌐   |
| `POST`   | `/store/carts/{cart_id}/items/`      | Add item to cart         | 🌐   |
| `PATCH`  | `/store/carts/{cart_id}/items/{id}/` | Update item quantity     | 🌐   |
| `DELETE` | `/store/carts/{cart_id}/items/{id}/` | Remove item from cart    | 🌐   |

#### `POST` — Add Item

| Field        | Type    | Required |
| ------------ | ------- | -------- |
| `product_id` | integer | ✅ Yes   |
| `quantity`   | integer | ✅ Yes   |

#### `PATCH` — Update Quantity

| Field      | Type    | Required |
| ---------- | ------- | -------- |
| `quantity` | integer | ✅ Yes   |

#### Response Fields

| Field         | Type    | Description                 |
| ------------- | ------- | --------------------------- |
| `id`          | integer |                             |
| `product`     | object  | `{ id, title, unit_price }` |
| `quantity`    | integer | Min: 1                      |
| `total_price` | decimal | `quantity × unit_price`     |

> 💡 If a product already exists in the cart, `POST` **increments** the quantity rather than creating a duplicate entry.

---

### 📋 Orders

**Prefix:** `/store/orders/`

| Method   | Endpoint              | Description                                      | Auth |
| -------- | --------------------- | ------------------------------------------------ | ---- |
| `GET`    | `/store/orders/`      | List orders — users see own, admins see all      | 🔑   |
| `POST`   | `/store/orders/`      | Place order — atomically converts & deletes cart | 🔑   |
| `GET`    | `/store/orders/{id}/` | Retrieve an order with nested items              | 🔑   |
| `PATCH`  | `/store/orders/{id}/` | Update payment status                            | 🔴   |
| `DELETE` | `/store/orders/{id}/` | Delete an order                                  | 🔴   |

#### `POST /store/orders/` — Request Body

| Field     | Type | Required |
| --------- | ---- | -------- |
| `cart_id` | UUID | ✅ Yes   |

> Cart must be non-empty. Cart is **permanently deleted** on success.

#### `PATCH /store/orders/{id}/` — Request Body

| Field            | Type   | Values                                  |
| ---------------- | ------ | --------------------------------------- |
| `payment_status` | string | `P` Pending · `C` Complete · `F` Failed |

#### Response Fields

| Field            | Type     | Description                                                        |
| ---------------- | -------- | ------------------------------------------------------------------ |
| `id`             | integer  |                                                                    |
| `customer`       | integer  | Customer ID                                                        |
| `placed_at`      | datetime | Auto-set on creation                                               |
| `payment_status` | string   | `P` / `C` / `F`                                                    |
| `items`          | array    | `{ id, product: { id, title, unit_price }, unit_price, quantity }` |

---

### 👥 Customers

**Prefix:** `/store/customers/`

| Method | Endpoint                         | Description                     | Auth |
| ------ | -------------------------------- | ------------------------------- | ---- |
| `GET`  | `/store/customers/me/`           | Get current customer profile    | 🔑   |
| `PUT`  | `/store/customers/me/`           | Update current customer profile | 🔑   |
| `GET`  | `/store/customers/`              | List all customers              | 🔴   |
| `GET`  | `/store/customers/{id}/history/` | View customer order history     | 🔴   |

#### `PUT /store/customers/me/` — Request Body

| Field        | Type   | Required    |
| ------------ | ------ | ----------- |
| `phone`      | string | ✅ Yes      |
| `birth_date` | date   | ➖ Optional |
| `membership` | string | ➖ Optional |

#### Response Fields

| Field        | Type    | Description                        |
| ------------ | ------- | ---------------------------------- |
| `id`         | integer |                                    |
| `user_id`    | integer | Read-only                          |
| `phone`      | string  |                                    |
| `birth_date` | date    | Nullable                           |
| `membership` | string  | `B` Bronze · `S` Silver · `G` Gold |

> `/history/` requires the custom `view_history` Django model permission.

---

## 🧪 Testing

This project includes two types of testing.

---

### ✅ Automated Testing

Built with **pytest**, `pytest-django`, and `model-bakery`. Tests live in `store/tests/`.

> ⚠️ Test coverage is a work in progress — currently focused on the Collections endpoint.

**Run all tests:**

```bash
pytest
```

**Run with verbose output:**

```bash
pytest -v
```

**Run a specific file:**

```bash
pytest store/tests/test_collections.py
```

**Test structure:**

```
store/
└── tests/
    ├── conftest.py            # Shared fixtures (api_client, authenticate)
    └── test_collections.py   # Collection endpoint tests
```

> 💡 Pytest is configured via `pytest.ini` in the project root — Django settings are automatically pointed to `storefront.settings.dev` so no extra flags are needed.

**Current coverage:**

| Class                    | Endpoint                       | Scenario                 | Expected           |
| ------------------------ | ------------------------------ | ------------------------ | ------------------ |
| `TestCreateCollection`   | `POST /store/collections/`     | Anonymous user           | `401 Unauthorized` |
| `TestCreateCollection`   | `POST /store/collections/`     | Authenticated, not admin | `403 Forbidden`    |
| `TestCreateCollection`   | `POST /store/collections/`     | Admin, invalid data      | `400 Bad Request`  |
| `TestCreateCollection`   | `POST /store/collections/`     | Admin, valid data        | `201 Created`      |
| `TestRetrieveCollection` | `GET /store/collections/{id}/` | Collection exists        | `200 OK`           |

---

### 📈 Performance Testing

Built with **Locust** for load testing and **django-silk** for request profiling.

**Locust — Load Testing**

Locust scripts live in `locustfiles/`. The `browse_products.py` script simulates realistic user behaviour:

| Task            | Weight | Description                                     |
| --------------- | ------ | ----------------------------------------------- |
| `view_products` | 2      | Browse products filtered by a random collection |
| `view_product`  | 4      | View a random product detail page               |
| `add_to_cart`   | 1      | Add a random product to the user's cart         |
| `say_hello`     | 1      | Hit the playground endpoint                     |

Each simulated user creates a cart on startup and reuses it across tasks.

**Run Locust:**

```bash
locust -f locustfiles/browse_products.py
```

Then open `http://0.0.0.0:8089` to configure and start the load test.

**Silk — Request Profiling**

django-silk is configured in the project and profiles live requests. Access the Silk dashboard at:

```
http://127.0.0.1:8000/silk/
```

---

## 🚧 Planned Features

The following features have their infrastructure and setup in place but are **not yet fully implemented:**

|     | Feature                 | Status         | Notes                                                          |
| --- | ----------------------- | -------------- | -------------------------------------------------------------- |
| 📧  | **Email Notifications** | 🚧 In Progress | SMTP config ready — order confirmation emails not yet wired up |
| ⚙️  | **Background Tasks**    | 🚧 In Progress | Celery + Redis setup complete — no active tasks assigned yet   |
| 🗄️  | **Redis Caching**       | 🚧 In Progress | Redis is available as broker — caching layer not yet applied   |

---

## 🌐 Deployment

This API is deployed on **Heroku** using the production settings in `storefront/settings/prod.py`.

🔗 **Live URL:** `https://sherybuy-prod-8c19f1a2a82c.herokuapp.com/`

**Deploy your own:**

**1. Create the Heroku app and provision add-ons**

```bash
heroku login
heroku create your-app-name
heroku addons:create jawsdb:kitefin
heroku addons:create mailgun:starter
heroku addons:create rediscloud:30
```

**2. Set the required environment variables**

```bash
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DJANGO_SETTINGS_MODULE=storefront.settings.prod
```

> All other variables (`DATABASE_URL`, `JAWSDB_URL`, `REDISCLOUD_URL`, and all `MAILGUN_*` vars) are **automatically set** by their respective add-ons.

**3. Deploy**

```bash
git push heroku main
```

> The `release` phase in the `Procfile` automatically runs `python manage.py migrate` on every deploy.

**Procfile**

```
release: python manage.py migrate
web: gunicorn storefront.wsgi
worker: celery -A storefront worker
```

---

## 👨‍💻 Author

**Muhammad Shehryar Azhar**

[![GitHub](https://img.shields.io/badge/GitHub-ShehryarAzhar-181717?style=for-the-badge&logo=github)](https://github.com/ShehryarAzhar)

---

_Made with ❤️ using Django REST Framework_
