import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', "sqlite:///data.db")
app.secret_key = 'sijo'
api = Api(app)



jwt = JWT(app, authenticate, identity)  #This will give /auth end point


api.add_resource(Item, '/item/<name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug = True)
