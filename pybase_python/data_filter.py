import re
from storage_manager import *
import os

# Exception when the database directory is not existent
class NonExistantDatabaseException(Exception):
    def __init__(self):
        super().__init__("Warning: the database does not exist")

# Exception when the table name is not given
class TableNotPresent(Exception):
    def __init__(self):
        super().__init__("The table name is not specified")

class Select:
    def __init__(self, database, query):
        self.query = query.strip()
        self.database = database
        
        if not os.path.exists(self.database):
            raise NonExistantDatabaseException()
        
        self.columns, self.table_name = self._extract_columns_and_table()
        
        if not self.table_name:
            raise TableNotPresent()
        
        print(f"Table Name: {self.table_name}")
        print(f"Columns: {self.columns}")

    def _extract_columns_and_table(self):
        match = re.match(r"(?i)SELECT\s+(.+?)\s+FROM\s+(\w+)", self.query)
        if match:
            columns = match.group(1).strip()
            table_name = match.group(2).strip()
            return columns, table_name
        return None, None

# Example Usage
x = Select("database", "SELECT * FROM student")
s = SchemaManager("test_db")
d = DatabaseManager(s)
y = d.fetch_data(x.table_name)
print(y)
