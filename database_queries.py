
import sqlite3

class Database():
    def __init__(self, path_to_db):
        self.path_to_db = path_to_db

    def connect_to_database(self):
        try:
            self.connection = sqlite3.connect(self.path_to_db)
            print("Connected to database successfully.")
        except Exception as e:
            print(e)
    
    def create_cursor(self):
        self.cursor = self.connection.cursor()

    def run_query(self, query:str, parameters:tuple=None):
        self.cursor.execute(query, parameters)
        print("Query finished.")
    
    def fetch_all(self):
        return self.cursor.fetchall()
    
    def commit_transaction(self):
        self.connection.commit()
        print("Transaction committed successfully.")

    def close_database(self):
        self.connection.close()
        print("Database closed successfully.")

