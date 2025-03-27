# app/__init__.py
"""
Flask application factory and extension initialization.
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flasgger import Swagger
from app.common.logging_config import configure_logging
from app.common.errors import register_error_handlers

# Public symbols exposed by this module
__all__ = ["create_app", "db", "ma"]

# Initialize extensions without app context
db = SQLAlchemy()  # SQLAlchemy ORM
ma = Marshmallow()  # Marshmallow for schema serialization/validation


def create_app() -> Flask:
    """
    Flask Application Factory.

    Creates and configures the Flask application instance.
    Loads environment-specific configuration, sets up extensions, logging,
    Swagger documentation, and registers application blueprints.

    Returns:
        Flask: A fully configured Flask application instance.
    """
    app = Flask(__name__)

    # Load configuration from environment variable or default to DevelopmentConfig
    config_path = os.getenv("FLASK_CONFIG", "app.common.config.DevelopmentConfig")
    try:
        app.config.from_object(config_path)
    except (ImportError, AttributeError) as e:
        raise ImportError(f"Invalid FLASK_CONFIG value '{config_path}': {e}")

    # Set up application logging
    configure_logging(app)

    # Initialize Flask extensions
    db.init_app(app)
    ma.init_app(app)
    Swagger(app)

    # Register error handlers
    register_error_handlers(app)

    # Register route blueprints
    from app.routes import register_blueprints

    register_blueprints(app)

    # Log successful startup
    app.logger.info("Application created and configured using: %s", config_path)

    return app
