import re

class SQLValidator:
    """A simple SQL syntax validator using regex (without sqlparse)."""

    # Define basic SQL patterns
    SELECT_PATTERN = r"^\s*SELECT\s+[\w\*,\s]+\s+FROM\s+\w+(\s+WHERE\s+.+)?\s*;$"
    INSERT_PATTERN = r"^\s*INSERT\s+INTO\s+\w+\s*\([\w,\s]+\)\s*VALUES\s*\([\w'\d\s,]+\)\s*;$"
    UPDATE_PATTERN = r"^\s*UPDATE\s+\w+\s+SET\s+[\w\s,=']+\s*(WHERE\s+.+)?\s*;$"
    DELETE_PATTERN = r"^\s*DELETE\s+FROM\s+\w+\s*(WHERE\s+.+)?\s*;$"

    @staticmethod
    def is_valid_sql(query: str) -> bool:
        """Checks if a query matches known SQL patterns."""
        query = query.strip()
        patterns = [
            SQLValidator.SELECT_PATTERN,
            SQLValidator.INSERT_PATTERN,
            SQLValidator.UPDATE_PATTERN,
            SQLValidator.DELETE_PATTERN,
        ]
        return any(re.match(pattern, query, re.IGNORECASE) for pattern in patterns)

# Example Usage
if __name__ == "__main__":
    test_queries = [
        "SELECT * from employees ;",
        "INSERT INTO users (name, age) VALUES ('Alice', 25);",
        "UPDATE users SET age = 26 WHERE name = 'Alice';",
        "DELETE * FROM users;",
        "DROP TABLE users;",  # Invalid
    ]

    for query in test_queries:
        print(f"Valid: {SQLValidator.is_valid_sql(query)}  |  Query: {query}")
