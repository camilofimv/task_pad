from flask import Flask
from dotenv import load_dotenv
import os


def create_app():
    load_dotenv()  # read .env file on startup
    app = Flask(__name__)

    # make DATABASE_URL available to the app
    app.config["DATABASE_URL"] = os.getenv("DATABASE_URL")

    from app.routes import bp as routes_bp

    app.register_blueprint(routes_bp)

    # register DB teardown hook (added in next step)
    from . import db as dbmod

    dbmod.init_app(app)

    return app
