# Dependencies
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
import requests
from flask_seeder import FlaskSeeder
from flask_graphql import GraphQLView

# app initialization
app = Flask(__name__)

# Configs
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Modules
db = SQLAlchemy(app)
seeder = FlaskSeeder()
seeder.init_app(app, db)

# Models
from models import *

# Schema
from schema import *

# Routes
@app.route('/')
def index():
    return 'Welcome to Book Basket'

app.add_url_rule(
    '/graphql',
    view_func = GraphQLView.as_view(
        'graphql',
        schema = schema,
        graphiql = True
    )
)

if __name__ == '__main__':
     app.run()