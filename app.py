from flask import render_template, Flask
from pymongo import MongoClient
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

app = Flask(__name__)
load_dotenv()

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
cluster_name = "devopsbase.26zbs.mongodb.net"
database_name = "store"
collection_name = "product"

mongo_client = MongoClient(
    f"mongodb+srv://{db_username}:{db_password}@{cluster_name}/?retryWrites=true&w=majority&appName=DevOpsBase"
)
db = mongo_client[database_name]
products_collection = db[collection_name]

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/home', methods=['GET'])
def home():
    return "Welcome to Home Page!", 200

@app.route("/products")
def product():
    temp = list(products_collection.find())
    print(temp) 
    return render_template("products.html", product_obj=temp)

def close_connection(exception=None):
    """Close the MongoDB connection."""
    mongo_client.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
