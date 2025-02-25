from query_validator import SQLValidator

class QueryProcessor(SQLValidator):
    sql_commands = {
        "DDL": ["CREATE", "ALTER", "DROP", "TRUNCATE", "RENAME"],
        "DML": ["INSERT", "UPDATE", "DELETE"],
        "DQL": ["SELECT"],
        "DCL": ["GRANT", "REVOKE"],
        "TCL": ["COMMIT", "ROLLBACK", "SAVEPOINT"]
    }

    def __init__(self, query):
        self.query = query.strip()  # Removing unnecessary spaces
        self.is_valid = self.is_valid_sql(self.query)
        self._throw_invalid_exception()

    def _throw_invalid_exception(self):
        if not self.is_valid:
            raise ValueError(f"Invalid SQL query: {self.query}")

# Example Usage:
try:
    q = QueryProcessor("SELECT * FROM Table;")
    print("Query is valid!")
except ValueError as e:
    print(e)
