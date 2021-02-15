
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList 
from db import db

# JWT = Json Web Token

# para iniciar virtual env source venv/bin/activate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #podemos colocar qualquer tipo de SQL aqui. poderia ser por exemplo postgres seria apenas mudar isso aqui.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret_key'
api = Api(app)


jwt = JWT(app, authenticate, identity) # JWT creates a new endpoint /auth. when we call /auth temos que enviar um username e um password


api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>') # http://127.0.0.1:5000/item/Rolf
api.add_resource(ItemList,'/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister,'/register')


db.init_app(app)
app.run(port=5000, debug=True)



if __name__ == '__main__': # isso daqui serve para prevenir caso algum file rode um import app ele não rode um app.run. o __main__ é o nome que o python atribui ao arquivo da onde surgiu a execução do run
    
    app.run(port=5000, debug=True)