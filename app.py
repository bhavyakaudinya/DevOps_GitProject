from flask import Flask, render_template
from pymongo import MongoClient
from urllib.parse import quote_plus

app = Flask(__name__)

# username = "c0919320"
# password = "host"
# encoded_password = quote_plus(password)

mongo_client = MongoClient(f"mongodb+srv://c0919320:<c0919320_BK>@devopsbase.26zbs.mongodb.net/?retryWrites=true&w=majority&appName=DevOpsBase")
db = mongo_client["store"]
collections = db["product"]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/products')
def product():
    product = list(collections.find())
    return render_template("products.html", product_obj=product)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
