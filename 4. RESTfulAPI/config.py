import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'b4b6d862cc8bb31049f4d1a75b530db07dc89d6a238464475f06f7c1b1842cf0')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'e9fe1d06fd44dc147ddb32f7997eeecdbc7d4412a8356f11408b5fc5347eca31'  # Update this with a secure key
