import random
import string
import os
import pickle
from crypter import encrypt, decrypt

class NonExistantTableException(Exception):
    def  __init__(self):
        super().__init__("Warning: the table does not exist")

class SchemaManager:
    def __init__(self, database_name):
        self.database_name = database_name
        self.schema_file = f"database/{database_name}.pbs"
        self.db_file = f"database/{database_name}.pbf"
        
        if not os.path.exists("database"):
            os.makedirs("database")
        
        if os.path.exists(self.schema_file):
            with open(self.schema_file, "rb") as f:
                self.schema = pickle.load(f)
        else:
            self.schema = {'tables': {}, '0lkjKo09': self.generate_passkey()}
            self.save_schema()
        
        if not os.path.exists(self.db_file):
            with open(self.db_file, "wb") as f:
                pickle.dump({}, f)
        
    def generate_passkey(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=21))
    
    def save_schema(self):
        with open(self.schema_file, "wb") as f:
            pickle.dump(self.schema, f)
    
    def add_table(self, table_name, columns, primary_key, foreign_keys=None):
        if table_name in self.schema['tables']:
            raise ValueError(f"Table '{table_name}' already exists in the schema.")
        
        self.schema['tables'][table_name] = {
            'columns': {col: [] for col in columns},
            'primary_key': primary_key,
            'foreign_keys': foreign_keys or {},
        }
        self.save_schema()
    
    def get_table_info(self, table_name):
        return self.schema.get('tables', {}).get(table_name)
    
    def get_passkey(self):
        return self.schema['0lkjKo09']

class DatabaseManager:
    def __init__(self, schema_manager):
        self.schema_manager = schema_manager
        self.db_file = schema_manager.db_file
        
        with open(self.db_file, "rb") as f:
            self.database = pickle.load(f)
    
    def save_database(self):
        with open(self.db_file, "wb") as f:
            pickle.dump(self.database, f)
    
    def insert_data(self, table_name, data):
        table_info = self.schema_manager.get_table_info(table_name)
        if not table_info:
            raise NonExistantTableException
        
        if table_info['primary_key'] not in data:
            raise ValueError("Primary key is missing in the data.")
        
        if table_name not in self.database:
            self.database[table_name] = {col: [] for col in table_info['columns']}
        
        passkey = self.schema_manager.get_passkey()
        for column, value in data.items():
            encrypted_value = encrypt(passkey, value)
            self.database[table_name][column].append(encrypted_value)
        
        self.save_database()
    
    def fetch_data(self, table_name):
        if table_name not in self.database:
            raise NonExistantTableException
        encrypted_data = self.database.get(table_name, {})
        passkey = self.schema_manager.get_passkey()
        decrypted_data = {col: [decrypt(passkey, val) for val in values] for col, values in encrypted_data.items()}
        return decrypted_data
    
if __name__ == "__main__":
    schema_manager = SchemaManager("test_db")
    db_manager = DatabaseManager(schema_manager)
    
    student_data = db_manager.fetch_data("student")
    children_data = db_manager.fetch_data("children")
    print(f"Fetched {len(student_data['id'])} records from 'student' table.")
    print(f"Fetched {len(children_data['child_id'])} records from 'children' table.")
    print(student_data)
