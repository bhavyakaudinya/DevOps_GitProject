from app import flask_app, products_collection
from flask import render_template

from app import flask_app

from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

db_username = "c0919320"
db_password = "c0919320_BK"
cluster_name = "devopsbase.26zbs.mongodb.net"
database_name = "store"
collection_name = "products"

mongo_client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@{cluster_name}/?retryWrites=true&w=majority&appName=DevOpsBase")

db = mongo_client[database_name]

products_collection = db[collection_name]

from app import routes

@flask_app.route("/")
def index():
    return render_template("index.html")

@flask_app.route("/products")
def products():
    products = list(products_collection.find())
    return render_template("products.html", products=products)

flask_app.run(host="0.0.0.0", port=5000)
