def is_valid(query):
    # Import regex module inside the function to save memory
    import re

    # List of valid SQL commands
    sql_statements = [
        "CREATE", "ALTER", "DROP", "SELECT", "INSERT", "UPDATE", "DELETE", 
        "TRUNCATE", "RENAME", "GRANT", "REVOKE", "COMMIT", "ROLLBACK", 
        "SAVEPOINT", "EXPLAIN", "DESCRIBE", "SHOW"
    ]
    
    query=query.upper()
    query=query.split(';')
    print(query)


# Test the function with various queries
print(is_valid("SELECT * FROM users;INSERT INTO users (name, age) VALUES ('John', 30);"))  # True
print(is_valid("INSERT INTO users (name, age) VALUES ('John', 30);"))  # True
print(is_valid("UPDATE users SET name = 'Jane' WHERE id = 1;"))  # True
print(is_valid("DELETE FROM users WHERE id = 1;"))  # True
print(is_valid("SELECT FROM users"))
