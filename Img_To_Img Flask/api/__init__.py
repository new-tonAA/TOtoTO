from flask import Blueprint
from .map_routes import map_bp

def register_blueprints(app):
    app.register_blueprint(map_bp)
