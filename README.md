# 🛒 Product Catalog Service

A robust backend microservice for managing products and categories in an e-commerce platform.  
Built using **FastAPI**, **PostgreSQL**, and **Docker**, following clean architectural patterns like **Repository Pattern** and **Unit of Work**.

---

## 🚀 Features

- ✅ Full CRUD for Products
- ✅ Full CRUD for Categories
- ✅ Many-to-Many Product–Category Relationship
- ✅ Advanced Search with filtering and pagination
- ✅ Repository Pattern for data abstraction
- ✅ Unit of Work for transactional integrity
- ✅ Database indexing for performance optimization
- ✅ Automatic database seeding (10 products, 3 categories)
- ✅ Persistent Docker volume
- ✅ OpenAPI (Swagger) documentation
- ✅ Input validation and proper error handling

---

## 🏗 Architecture

The project follows clean layered architecture:

### 1️⃣ API Layer
- Handles HTTP requests/responses
- Implements RESTful endpoints
- Returns proper HTTP status codes

### 2️⃣ Service Layer
- Contains business logic
- Orchestrates repository calls
- Handles validation and error conversion

### 3️⃣ Repository Layer
- Abstracts database access
- Implements data operations
- Keeps ORM logic isolated

### 4️⃣ Unit of Work
- Manages database sessions
- Ensures atomic transactions
- Guarantees consistency across multiple operations

---

## 🗄 Database Design

### Tables

### `products`
| Column | Type | Constraint |
|--------|------|------------|
| id | UUID | Primary Key |
| name | TEXT | NOT NULL |
| description | TEXT | |
| price | DECIMAL | NOT NULL |
| sku | TEXT | UNIQUE |
| created_at | TIMESTAMP | |
| updated_at | TIMESTAMP | |

### `categories`
| Column | Type | Constraint |
|--------|------|------------|
| id | UUID | Primary Key |
| name | TEXT | UNIQUE |
| description | TEXT | |

### `product_categories`
- Many-to-many junction table
- Composite primary key (product_id, category_id)

---

## 🔍 Advanced Search

- Endpoint: GET /products/search


### Supported Query Parameters

| Parameter | Description |
|------------|------------|
| q | Keyword search (name + description) |
| category_id | Filter by category |
| min_price | Minimum price filter |
| max_price | Maximum price filter |
| skip | Pagination offset |
| limit | Pagination limit |

### Example:

- GET /products/search?q=laptop&min_price=500 max_price=1500&limit=5

---

## ⚙️ Setup Instructions

### Prerequisites
- Docker
- Docker Compose

### Run the Application

```bash
docker-compose up --build
- Application runs at: http://localhost:8000
Swagger documentation: http://localhost:8000/docs 
```
## 🧪 Database Seeding

On first startup, the application automatically seeds:

- 3 Categories  
- 10 Products (linked to categories)  

Seeding runs only if the database is empty.

---

## 🐳 Docker Configuration

### Services

- **db** → PostgreSQL (persistent volume enabled)  
- **app** → FastAPI backend  

Persistent volume ensures data is not lost between restarts.

---

## 🛡 Error Handling

- **400** → Validation errors / Duplicate entries  
- **404** → Resource not found  
- **422** → Invalid request format  
- **500** → Internal server errors (unexpected)  

Integrity errors (e.g., duplicate SKU) are converted to HTTP 400.

---

## 📈 Performance Optimization

### B-tree indexes on:

- Product name  
- Product price  
- Product SKU  
- Category name  

- Efficient query filtering  
- Pagination support  

---


## 📌 Architectural Decisions

- **Repository Pattern** ensures clean separation from database logic.  
- **Unit of Work** guarantees transactional consistency.  
- **Service Layer** keeps business logic independent of API.  
- **Dockerized setup** enables one-command deployment.  
- **PostgreSQL** chosen for robustness and indexing capabilities.  

---

## 👩‍💻 Author
**Sai Divya**  
Backend Development Project
