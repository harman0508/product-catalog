# Product Showcase (Full-Stack)

A production-ready full-stack application for managing and displaying products, categories, and inventory with a clean, scalable architecture.

---

## 🧰 Tech Stack

### Backend

* Python 3.8+
* Django 3.2+
* Django REST Framework
* django-filter
* django-cors-headers

### Frontend

* React 18
* Axios
* React Router

### Database

* SQLite (development)
* Easily configurable for PostgreSQL

---

## 🚀 Features

### Backend

* Full CRUD APIs for Products and Categories
* Inventory management (per product)
* Featured products endpoint
* Priority-based filtering endpoint (low, medium, high, critical)
* Nested category-products endpoint
* Service Layer (business logic separation)
* Repository Layer (data access abstraction)
* Pagination (PageNumberPagination, 10 per page)
* Filtering:
  * Search by product title
  * Filter by category
  * Filter by priority level
* Seed data command + JSON fixtures (15 products, 5 categories)
* Structured error handling
* Unit + API tests

### Frontend

* Product listing page with pagination
* Search functionality (debounced)
* Category filtering
* Price display
* Inventory display
* Featured product badges
* Priority display
* Checklist page for requirement verification
* API integration using Axios
* Loading and error states

---

## 📁 Project Structure

```
product-catalog/
├── backend/
│   ├── manage.py
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── .env.example
│   ├── showcase_api/
│   │   ├── settings.py
│   │   └── urls.py
│   └── catalog/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── exceptions.py
│       ├── services/
│       ├── repositories/
│       ├── fixtures/
│       ├── tests/
│       └── management/commands/
│
└── frontend/
    ├── public/
    ├── src/
    │   ├── components/
    │   ├── pages/
    │   ├── api/
    │   ├── styles/
    │   └── __tests__/
    └── package.json
```

---

## ⚙️ Setup Instructions

### 1. Backend Setup

```bash
cd backend

python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py seed_data
python manage.py runserver
```

#### Alternative: Load fixture data instead of seed_data

```bash
python manage.py loaddata initial_data
```

Backend will run at:
👉 http://127.0.0.1:8000/api/

---

### 2. Frontend Setup

```bash
cd frontend

npm install
npm start
```

Frontend will run at:
👉 http://localhost:3000

---

## 🔌 API Endpoints

### Products

* `GET /api/products/` — List all products
* `GET /api/products/{id}/` — Get product details
* `POST /api/products/` — Create new product
* `PUT /api/products/{id}/` — Update product
* `DELETE /api/products/{id}/` — Delete product
* `GET /api/products/featured/` — Get featured products
* `GET /api/products/by_priority/?level=high` — Filter by priority
* `GET /api/products/?q=<search>` — Search by title
* `GET /api/products/?category=<id>` — Filter by category
* `GET /api/products/?page=<num>` — Pagination

### Categories

* `GET /api/categories/` — List all categories
* `GET /api/categories/{id}/` — Get category details
* `POST /api/categories/` — Create new category
* `PUT /api/categories/{id}/` — Update category
* `DELETE /api/categories/{id}/` — Delete category
* `GET /api/categories/{id}/products/` — Get all products in a category

### Admin

* `GET /admin/` — Django admin panel

---

## ✅ Checklist Page

Accessible at:
👉 http://localhost:3000/checklist

This page verifies:

* API server connectivity
* Product data loading
* Search functionality
* Category filtering
* UI rendering

---

## 🌱 Seed Data

Populate initial data using:

```bash
python manage.py seed_data
```

Or load the full fixture (15 products, 5 categories):

```bash
python manage.py loaddata initial_data
```

---

## 🧪 Testing

### Run backend tests:

```bash
cd backend
pytest
```

### Run frontend tests:

```bash
cd frontend
npm test
```

### Coverage includes:

* Model tests (13 tests — Category, Product, Inventory, relationships, cascade delete, defaults, choices)
* Service layer tests (9 tests — filtering, search, featured, priority, validation, category products)
* API endpoint tests (27 tests — full CRUD, search, filtering, featured, priority, pagination, nested routes, empty dataset)
* Frontend component tests with mocked API (7 tests — render, data display, error, empty state, category filter, search, loading)

### Edge Cases Covered:

* Empty dataset (no products, no categories)
* Invalid query parameters
* Search with no results
* API failure handling
* Invalid priority level (including "critical" support)
* Missing required parameters
* Short product title validation
* One-to-one inventory constraint
* Cascade delete behavior

---

## 🧠 Architecture & Design Decisions

### 1. Service Layer

Encapsulates business logic and keeps views thin. Accepts an injectable repository for testability.

### 2. Repository Layer

Abstracts database queries for better maintainability and scalability. Uses `select_related` for query optimization.

### 3. DRF ModelViewSets

Provide full CRUD with clean, scalable API routing and built-in pagination. Custom `@action` decorators for featured and priority endpoints.

### 4. Custom Exception Handler

Wraps all API errors in a consistent `{ error, status_code }` format.

### 5. React Component Architecture

* Separation of concerns with reusable components
* Centralized API layer with error handling
* Debounced search to reduce API calls

---

## ⚖️ Trade-offs

| Decision        | Reason                          |
| --------------- | ------------------------------- |
| SQLite          | Simplicity for development      |
| No Docker       | Keeps setup simple and portable |
| Minimal styling | Focus on functionality over UI  |

---

## ⚠️ Known Limitations

* No authentication/authorization
* No caching layer (Redis not included)

---

## 🚀 Future Improvements

* Add authentication/authorization
* Introduce Redis caching
* Add CI/CD pipeline
* Switch to PostgreSQL for production
* Improve UI/UX design

---

## 🌐 Access Points

* Frontend: http://localhost:3000
* Backend API: http://localhost:8000/api/
* Admin Panel: http://localhost:8000/admin/

---

## 👤 Author

Harmanjeet Singh
