# FastAPI Reference Project Structure

This directory contains a complete, production-ready FastAPI application structure with authentication, database ORM integration, Pydantic schemas, and modular routing.

---

## 📂 Project Architecture

```
fastapi/
│
├── .env                  # Environment configuration (DB credentials, secret keys)
├── requirements.txt      # Python package dependencies
│
└── app/                  # Main Application Package
    ├── __init__.py
    ├── main.py           # Application entrypoint & route inclusions
    ├── config.py         # Environment settings using Pydantic BaseSettings
    ├── database.py       # SQLAlchemy engine & session setup (get_db dependency)
    ├── models.py         # SQLAlchemy ORM Database Models (Tables)
    ├── schemas.py        # Pydantic Schemas (Request/Response validation)
    ├── utils.py          # Utility functions (Password hashing & verification)
    │
    └── routers/          # Modular API Route Handlers
        ├── auth.py       # Authentication router (/login -> JWT generation)
        ├── oauth2.py     # JWT token generation & current user authentication
        ├── post.py       # CRUD operations for Posts (/posts)
        └── user.py       # User registration & user profiles (/users)
```

---

## 🚀 How Each File Works

### 1. `app/main.py`
The central entry point of the FastAPI application.
- Initializes the FastAPI app: `app = FastAPI()`.
- Runs `models.Base.metadata.create_all(bind=engine)` to create tables automatically.
- Mounts modular routers (`user.router`, `post.router`, `auth.router`).

### 2. `app/config.py`
Uses `pydantic-settings` to load environment variables safely from `.env`.
- Defines the `Settings` class mapped to `.env` variables (`database_hostname`, `secret_key`, etc.).

### 3. `app/database.py`
Manages PostgreSQL database connections via SQLAlchemy.
- Creates `engine` using connection string built from `settings`.
- Provides `get_db()` dependency for database session management with yield/cleanup.

### 4. `app/models.py`
Defines database tables using SQLAlchemy ORM (e.g. `User`, `Post`).

### 5. `app/schemas.py`
Defines Pydantic data schemas for API request validation and response formatting.

### 6. `app/utils.py`
Contains helper functions for security:
- `hash(password)`: Hashes passwords using `passlib`/`bcrypt`.
- `verify(plain, hashed)`: Validates user passwords against stored hashes.

### 7. `app/routers/`
Houses modular router modules:
- `auth.py`: Handles POST `/login` credentials check and returns JWT bearer tokens.
- `oauth2.py`: Handles JWT token encoding, decoding, and `get_current_user` dependency for protected endpoints.
- `post.py`: RESTful endpoints for CRUD on posts.
- `user.py`: RESTful endpoints for creating users and fetching profiles.

---

## 🛠️ How to Run

1. **Set up virtual environment & install dependencies**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**:
   Ensure `.env` contains valid connection settings for your database.

3. **Start the Development Server**:
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Interactive API Documentation**:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc UI: `http://127.0.0.1:8000/redoc`
