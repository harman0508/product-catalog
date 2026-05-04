# Product Showcase (Full-Stack)

A production-ready full-stack application for managing and displaying products, categories, and inventory with a clean, scalable architecture.

---

## 🧰 Tech Stack

### Backend

* Python 3.8+
* Django 3.2
* Django REST Framework
* django-filter

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

* RESTful APIs for Products and Categories
* Inventory management (per product)
* Service Layer (business logic separation)
* Repository Layer (data access abstraction)
* Filtering:

  * Search by product name
  * Filter by category
* Seed data command
* Structured error handling
* Unit + API tests

### Frontend

* Product listing page
* Search functionality
* Category filtering
* Inventory display
* Checklist page for requirement verification
* API integration using Axios
* Loading and error states

---

## 📁 Project Structure

```
product-showcase/
├── api-server/
│   ├── manage.py
│   ├── showcase_api/
│   │   ├── settings.py
│   │   └── urls.py
│   └── catalog/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── services/
│       ├── repositories/
│       ├── tests/
│       └── management/commands/
│
└── ui-client/
    └── product-dashboard-react/
        ├── public/
        ├── src/
        │   ├── components/
        │   ├── pages/
        │   ├── api/
        │   └── styles/
        └── package.json
```

---

## ⚙️ Setup Instructions

### 1. Backend Setup

```bash
cd api-server

python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

python manage.py migrate
python manage.py seed_data
python manage.py runserver
```

Backend will run at:
👉 http://127.0.0.1:8000/api/

---

### 2. Frontend Setup

```bash
cd ui-client/product-dashboard-react

npm install
npm start
```

Frontend will run at:
👉 http://localhost:3000

---

## 🔌 API Endpoints

### Products

* `GET /api/products/`
* `GET /api/products/?q=<search>`
* `GET /api/products/?category=<id>`

### Categories

* `GET /api/categories/`

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

Includes:

* Categories (e.g., Electronics)
* Products (e.g., Laptop, Phone)
* Inventory quantities

---

## 🧪 Testing

### Run backend tests:

```bash
pytest
```

### Coverage includes:

* Model tests
* Service layer tests
* API endpoint tests

### Edge Cases Covered:

* Empty dataset
* Invalid query parameters
* API failure handling

---

## 🧠 Architecture & Design Decisions

### 1. Service Layer

Encapsulates business logic and keeps views thin.

### 2. Repository Layer

Abstracts database queries for better maintainability and scalability.

### 3. DRF ViewSets

Provide clean and scalable API routing.

### 4. React Component Architecture

* Separation of concerns
* Reusable components
* Centralized API layer

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
* No pagination (can be added easily)
* No caching layer (Redis not included)

---

## 🚀 Future Improvements

* Add pagination & sorting
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
