# app/common/logging_config.py
"""
Centralized logging configuration for the Flask application.
"""

import logging
from flask import Flask


def configure_logging(app: Flask, level: int = logging.INFO) -> None:
    """
    Configures structured logging for a Flask app.

    Args:
        app (Flask): The Flask application instance.
        level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
    """
    # Create a stream handler for stdout
    handler = logging.StreamHandler()
    handler.setLevel(level)

    # Define standard log format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # Avoid duplicate handlers in reloader or debug mode
    if app.logger.hasHandlers():
        app.logger.handlers.clear()

    # Attach the handler and set the desired logging level
    app.logger.addHandler(handler)
    app.logger.setLevel(level)

    # Suppress overly verbose logs from Werkzeug
    logging.getLogger("werkzeug").setLevel(logging.WARNING)

    app.logger.info("Logging is configured with level: %s", logging.getLevelName(level))
