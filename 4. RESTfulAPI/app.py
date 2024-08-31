from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from config import Config
from models import db
from resources import RegisterUser, LoginUser, ItemList, ItemDetail

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt = JWTManager(app)
    api = Api(app)

    # Register resources
    api.add_resource(RegisterUser, '/register')
    api.add_resource(LoginUser, '/login')
    api.add_resource(ItemList, '/items')
    api.add_resource(ItemDetail, '/items/<int:item_id>')

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
