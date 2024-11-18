import unittest
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
cluster_name = "devopsbase.26zbs.mongodb.net"
database_name = "store"

class TestDatabaseRead(unittest.TestCase):
    def setUp(self):
        self.connection_string = (
            f"mongodb+srv://{db_username}:{db_password}@{cluster_name}/?retryWrites=true&w=majority&appName=DevOpsBase"
        )
        self.client = MongoClient(self.connection_string)

    def tearDown(self):
        self.client.close()  # Close MongoDB connection

    def test_mongo_connection(self):
        try:
            self.client.admin.command("ping")
            connected = True
        except Exception:
            connected = False
        self.assertTrue(connected)

if __name__ == "__main__":
    unittest.main()
