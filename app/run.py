# app/run.py

"""
Entry point for the Flask application.

This module creates and runs the Flask app instance using the application factory.
"""

from app import create_app


def main() -> None:
    """
    Main function to create and run the Flask application.

    The application is created using the factory function `create_app()`.
    The debug mode is dynamically set based on the application's configuration.
    """
    # Create the Flask application using the application factory.
    app = create_app()

    # Log that the application is starting.
    app.logger.info("Starting the Flask application...")

    # Run the app using the debug flag from the loaded config
    app.run(debug=app.config.get("DEBUG", False))


if __name__ == "__main__":
    main()
