from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    # Other common configurations

class ProductionConfig(Config):
    # Production-specific configurations
    DEBUG = False
    # Database, security, and other production settings

class DevelopmentConfig(Config):
    # Development-specific configurations
    DEBUG = True
    # Development database, debugging settings, etc.