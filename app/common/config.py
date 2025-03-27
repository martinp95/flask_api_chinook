# app/common/config.py
"""
Configuration settings for the Flask application, including environment-specific configs.
"""

import os


class Config:
    """
    Base configuration class with default settings.
    All environment-specific configs should inherit from this class.
    """

    # SQLite database URI (default for simplicity, can be overridden via env)
    SQLALCHEMY_DATABASE_URI: str = os.getenv("DATABASE_URL", "sqlite:///chinook.db")

    # Disable Flask-SQLAlchemy event system to reduce overhead
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    # Enable or disable Swagger UI
    SWAGGER: dict = {
        "title": "Chinook API",
        "uiversion": 3,
        "version": "1.0.0",
        "description": "REST API for the Chinook database.",
    }


class DevelopmentConfig(Config):
    """
    Configuration for the development environment.
    Enables debugging and SQL echo for query logging.
    """

    DEBUG: bool = True
    SQLALCHEMY_ECHO: bool = True  # Print SQL statements to stdout


class TestingConfig(Config):
    """
    Configuration for the testing environment.
    Uses in-memory SQLite database.
    """

    TESTING: bool = True
    DEBUG: bool = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProductionConfig(Config):
    """
    Configuration for the production environment.
    Debugging and testing are disabled.
    """

    DEBUG: bool = False
    TESTING: bool = False
