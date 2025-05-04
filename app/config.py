import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    MONGO_URI = "mongodb+srv://yashsharmamkn:Chitai60km@cluster0.4kpcwyj.mongodb.net/StudentDB" 