# app/__init__.py
from flask import Flask
from app.config import Config
from pymongo import MongoClient

mongo_client = None
db = None

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize MongoDB connection
    global mongo_client, db
    mongo_client = MongoClient(app.config['MONGO_URI'])
    db = mongo_client.get_default_database()
    
    # Import routes after app initialization to avoid circular imports
    from app.routes import main
    app.register_blueprint(main)
    
    return app
