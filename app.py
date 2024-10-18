from flask import render_template, Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

db_username = os.getenv("DB_USERNAME", "c0919320")
db_password = os.getenv("DB_PASSWORD", "c0919320_BK")
cluster_name = "devopsbase.26zbs.mongodb.net"
database_name = "store"
collection_name = "products"

mongo_client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@{cluster_name}/?retryWrites=true&w=majority&appName=DevOpsBase")
db = mongo_client[database_name]
products_collection = db[collection_name]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products")
def products():
    products = list(products_collection.find())
    return render_template("products.html", products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
