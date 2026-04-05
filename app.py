"""
app.py — Gunicorn entry point for Render deployment
Renders default detection looks for 'app' variable, so we expose flask_app as 'app'.
"""

from server import flask_app as app

if __name__ == "__main__":
    app.run()
