# 🎵 Chinook REST API

![Tests](https://github.com/martinp95/FLASK_API_CHINOOK/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/martinp95/FLASK_API_CHINOOK/branch/main/graph/badge.svg)](https://codecov.io/gh/martinp95/FLASK_API_CHINOOK)
![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![License](https://img.shields.io/github/license/martinp95/FLASK_API_CHINOOK)

A production-ready RESTful API built with **Flask**, **SQLAlchemy**, and **Marshmallow**, based on the classic Chinook database. It exposes endpoints to browse artists, albums, and tracks with support for pagination, nested resources, summaries, and OpenAPI documentation.

---

## 🚀 Features

- ✅ RESTful endpoints (artists, albums, tracks)
- ✅ SQLAlchemy ORM with SQLite (Chinook schema)
- ✅ Marshmallow for schema validation and serialization
- ✅ Swagger UI (via Flasgger) available at `/apidocs/`
- ✅ Centralized error handling (404, 500, etc.)
- ✅ Clean service-oriented architecture
- ✅ Auto-formatted with `black`
- ✅ 100% unit test coverage with `pytest`
- ✅ Configurable via environment (`FLASK_CONFIG`)
- ✅ Dockerized and compatible with `Makefile`

---

## 📁 Project Structure

```
flask_api_chinook/
├── app/
│   ├── __init__.py            # Application factory
│   ├── run.py                 # Entrypoint for running the app
│   ├── common/
│   │   ├── config.py          # Configuration classes
│   │   ├── logging_config.py  # Logging setup
│   │   └── errors.py          # Centralized error handling
│   ├── models/                # SQLAlchemy models
│   │   └── models.py
│   ├── schemas/               # Marshmallow schemas
│   │   ├── albums_schema.py
│   │   ├── albums_summary_schema.py
│   │   ├── artists_schema.py
│   │   └── tracks_schema.py
│   ├── services/              # Business logic layer
│   │   └── services.py
│   └── routes/                # Flask blueprints
│       ├── __init__.py
│       ├── artists.py
│       └── albums.py
├── instance/
│   └── chinook.db             # SQLite database (preloaded)
├── tests/                     # Pytest-based tests
│   ├── test_albums.py
│   ├── test_artists.py
│   ├── test_errors.py
│   └── conftest.py
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
└── README.md
```

---

## 🔧 Setup & Usage

### 🔸 1. Clone the repository

```bash
git clone https://github.com/martinp95/flask_api_chinook.git
cd flask_api_chinook
```

### 🔸 2. Start the application with Docker

```bash
make up
```

This will build and run the app using `docker-compose`.  
When it's running:

- ✅ API Base: [http://localhost:5000/artists](http://localhost:5000/artists)
- ✅ Swagger UI: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

---

## 📌 Environment Configuration

Set the Flask configuration using the `FLASK_CONFIG` env var:

| Mode         | Config Path                              |
|--------------|------------------------------------------|
| Development  | `app.common.config.DevelopmentConfig`    |
| Testing      | `app.common.config.TestingConfig`        |
| Production   | `app.common.config.ProductionConfig`     |

Default is Development if not set.

---

## 📚 API Endpoints (Sample)

### 🎤 GET `/artists?page=1&per_page=2`

Returns paginated list of artists:

```json
{
  "artists": [
    { "ArtistId": 1, "Name": "AC/DC" },
    { "ArtistId": 2, "Name": "Accept" }
  ],
  "page": 1,
  "per_page": 2,
  "total": 275
}
```

---

### 💿 GET `/artists/<artist_id>/albums`

Returns albums by artist:

```json
[
  { "AlbumId": 1, "Title": "For Those About To Rock We Salute You" },
  { "AlbumId": 4, "Title": "Let There Be Rock" }
]
```

---

### 📀 GET `/albums?page=1&per_page=1`

Returns albums and their tracks:

```json
{
  "albums": [
    {
      "AlbumId": 1,
      "Title": "For Those About To Rock We Salute You",
      "tracks": [
        { "TrackId": 1, "Name": "Track A" },
        { "TrackId": 2, "Name": "Track B" }
      ]
    }
  ],
  "page": 1,
  "per_page": 1,
  "total": 347
}
```

---

### 🎶 GET `/albums/<album_id>/tracks`

Returns all tracks from an album:

```json
{
  "album_id": 1,
  "tracks": [
    { "TrackId": 1, "Name": "Track A" },
    { "TrackId": 2, "Name": "Track B" }
  ]
}
```

---

### 📊 GET `/albums/summary`

Returns album summaries with artist and track count:

```json
[
  {
    "AlbumId": 1,
    "AlbumTitle": "For Those About To Rock",
    "ArtistName": "AC/DC",
    "TrackCount": 10
  }
]
```

---

## 🧪 Running Tests

### 🔹 Run all tests

```bash
make test
```

### 🔹 Run coverage

```bash
make coverage
```

Coverage report is also available in `htmlcov/index.html`.

---

## 🛠 Makefile Commands

```bash
make run         # Run the Flask app locally
make test        # Run all tests with pytest
make coverage    # Run coverage report
make format      # Format code with black
make clean       # Clean pyc/__pycache__
make up          # Start docker container
make down        # Stop docker container
```

---

## 🐍 Dependencies

Install with:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For testing & development
```

---

## 🔍 Swagger API Docs

Accessible without authentication at:

```
http://localhost:5000/apidocs/
```

Fully autogenerated via Flasgger.

---

### ✅ Project Highlights

This repository demonstrates a complete, production-ready Flask REST API with:

- Modular and scalable architecture
- Full Docker support for reproducible environments
- High test coverage with `pytest` and GitHub Actions
- Swagger UI documentation at `/apidocs/`
- Error handling and logging centralized
- Clean and readable codebase with auto-formatting via `make format`

All core functionality is covered by unit tests, with automated CI validating each push and pull request. This project serves as a solid foundation or reference for building robust backend services in Flask.

---

## 🧑‍💻 Author

Developed by **Martín Peláez Díaz**  
GitHub: [@martinp95](https://github.com/martinp95)

---

## 📄 License

Licensed under the [MIT License](LICENSE).