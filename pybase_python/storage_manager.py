import os
import json
import secrets
import struct

class SchemaManager:
    def __init__(self, db_directory='database', schema_filename='schema.pbs'):
        self.db_directory = db_directory
        self.schema_filepath = os.path.join(self.db_directory, schema_filename)
        self.schema = {}
        self.encryption_key = None
        self._initialize()

    def _initialize(self):
        """Ensures the database directory exists and loads/creates the schema."""
        if not os.path.exists(self.db_directory):
            os.makedirs(self.db_directory)
            print(f"Created database directory at '{self.db_directory}'.")

        if os.path.exists(self.schema_filepath):
            self._load_schema()
        else:
            self.encryption_key = secrets.token_bytes(32)  # 256-bit key
            self.schema = {
                'encryption_key': self.encryption_key.hex(),
                'tables': {}
            }
            self._save_schema()
            print(f"Initialized new schema with encryption key.")

    def _load_schema(self):
        """Loads schema information from a `.pbs` binary file."""
        with open(self.schema_filepath, 'rb') as f:
            schema_size_data = f.read(4)
            if not schema_size_data:
                raise ValueError("Schema file is corrupted or empty.")
            schema_size = struct.unpack('I', schema_size_data)[0]
            schema_data = f.read(schema_size)
            self.schema = json.loads(schema_data.decode('utf-8'))
            self.encryption_key = bytes.fromhex(self.schema['encryption_key'])
            print(f"Loaded existing schema with encryption key.")

    def _save_schema(self):
        """Saves schema information to a `.pbs` binary file."""
        with open(self.schema_filepath, 'wb') as f:
            schema_data = json.dumps(self.schema).encode('utf-8')
            schema_size = len(schema_data)
            f.write(struct.pack('I', schema_size))  # Write schema size (4 bytes)
            f.write(schema_data)  # Write schema JSON
            print(f"Schema saved to '{self.schema_filepath}'.")

    def add_table(self, table_name, columns, foreign_keys=None):
        """Adds a new table to the schema with its columns and foreign keys."""
        if table_name in self.schema['tables']:
            raise ValueError(f"Table '{table_name}' already exists in the schema.")
        self.schema['tables'][table_name] = {
            'columns': columns,
            'foreign_keys': foreign_keys or {},
            'location': f"{table_name}.pbd"
        }
        self._save_schema()
        print(f"Added table '{table_name}' to schema.")

    def get_table_info(self, table_name):
        """Retrieves metadata for a specified table."""
        return self.schema['tables'].get(table_name)

# **Usage Example**
if __name__ == "__main__":
    schema_manager = SchemaManager()

    # Define columns and foreign keys for a new table
    columns = {
        'id': 'INTEGER PRIMARY KEY',
        'name': 'TEXT NOT NULL',
        'age': 'INTEGER',
        'department_id': 'INTEGER'
    }
    foreign_keys = {
        'department_id': {
            'references': 'departments(id)',
            'on_delete': 'CASCADE'
        }
    }

    # Add the new table to the schema
    #schema_manager.add_table('employees', columns, foreign_keys)

    # Retrieve and display table information
    table_info = schema_manager.get_table_info('employees')
    print(f"Table Info: {table_info}")
