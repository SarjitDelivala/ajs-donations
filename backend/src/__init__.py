from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

import os

def create_app(config_name='production'):
    load_dotenv()

    app = Flask(__name__)

    # Load configuration based on the environment
    app.config.from_object(f'app.config.{config_name.capitalize()}Config')
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@"
        f"{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )

    # Register blueprints or views
    # from app.views.auth import auth_bp
    # app.register_blueprint(auth_bp)

    db = SQLAlchemy(app)

    # Other setups, error handlers, middleware, etc.

    return app