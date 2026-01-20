from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    @app.route("/")
    def home():
        return jsonify(message="Flask + Gunicorn + PostgreSQL")

    @app.route("/health")
    def health():
        return jsonify(status="OK")

    return app
