# app/common/errors.py
"""
Centralized error handling for the Flask application.
Defines reusable error handlers for common and unexpected exceptions.
"""

from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException, NotFound


def register_error_handlers(app: Flask) -> None:
    """
    Register custom error handlers on the given Flask app instance.

    Args:
        app (Flask): The Flask application where handlers will be registered.
    """

    @app.errorhandler(NotFound)
    def handle_404_error(error: NotFound):
        """
        Handle 404 Not Found errors.
        """
        response = {"error": "Not Found", "message": str(error)}
        return jsonify(response), 404

    @app.errorhandler(HTTPException)
    def handle_http_exception(error: HTTPException):
        """
        Handle all HTTPException-based errors (e.g., 400, 401, 403, 405).
        """
        response = {"error": error.name, "message": error.description}
        return jsonify(response), error.code

    @app.errorhandler(Exception)
    def handle_generic_exception(error: Exception):
        """
        Handle all unexpected errors that are not HTTPExceptions.
        Logs the exception and returns a generic 500 error.
        """
        app.logger.exception("Unhandled exception occurred: %s", error)
        response = {
            "error": "Internal Server Error",
            "message": "An unexpected error occurred.",
        }
        return jsonify(response), 500
