from flask import Flask
from flask_pymongo import PyMongo
from config import Config

mongo = PyMongo()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize MongoDB
    app.config["MONGO_URI"] = "mongodb+srv://yashsharmamkn:Chitai60km@cluster0.4kpcwyj.mongodb.net/StudentDB"
    mongo.init_app(app)
    
    # Import routes after app initialization to avoid circular imports
    from app.routes import main
    app.register_blueprint(main)
    
    return app 