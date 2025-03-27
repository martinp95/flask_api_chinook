# app/routes/__init__.py
"""
Registers all available Flask blueprints for the application.
"""

from flask import Flask
from typing import List, Tuple
from flask.blueprints import Blueprint


def register_blueprints(app: Flask) -> None:
    """
    Register all Flask blueprints to the given application instance.

    Args:
        app (Flask): The Flask application instance.
    """
    # Import blueprints locally to avoid circular dependencies
    from app.routes.artists import artists_bp
    from app.routes.albums import albums_bp

    # Define list of (blueprint, URL prefix) tuples
    blueprints: List[Tuple[Blueprint, str]] = [
        (artists_bp, "/artists"),
        (albums_bp, "/albums"),
    ]

    # Register each blueprint with the app and its corresponding URL prefix
    for blueprint, prefix in blueprints:
        app.register_blueprint(blueprint, url_prefix=prefix)
        app.logger.debug(f"Registered blueprint: {prefix}")
