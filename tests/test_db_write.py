import unittest
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
cluster_name = "devopsbase.26zbs.mongodb.net"
database_name = "store"
collection_name = "product"

class TestDatabaseWrite(unittest.TestCase):
    def setUp(self):
        """Set up MongoDB connection before each test."""
        self.connection_string = (
            f"mongodb+srv://{db_username}:{db_password}@{cluster_name}/?retryWrites=true&w=majority&appName=DevOpsBase"
        )
        self.client = MongoClient(self.connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def tearDown(self):
        """Close MongoDB connection after each test."""
        self.client.close()

    def test_insert_document(self):
        """Test inserting a document into the collection."""
        test_document = {
            "name": "Test Product",
            "price": 9.99,
            "description": "A test product description."
        }
        result = self.collection.insert_one(test_document)
        self.assertIsNotNone(result.inserted_id)

        self.collection.delete_one({"_id": result.inserted_id})

if __name__ == "__main__":
    unittest.main()
