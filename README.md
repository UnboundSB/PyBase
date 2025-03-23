# PyBase - Lightweight Relational Database Management System

## Overview
PyBase is a lightweight, high-performance relational database management system written in Python and C++. It is designed for local storage with support for structured tables, key-value mapping, and efficient query execution.

## Features
- **Schema & Database Management**: Supports table creation, modification, and deletion.
- **Custom Storage Engine**: Uses a binary format with CSV support.
- **Data Encryption**: Ensures secure storage using encryption techniques.
- **Query Execution**: Supports SQL-like queries including `SELECT`, `WHERE`, `JOIN`, `ORDER BY`, and more.
- **Performance Optimized**: Written in Python, C++, and Cython to reduce RAM usage and improve speed.
- **AngularJS-Based UI**: Lightweight frontend for database interaction.

## Installation

### Prerequisites
- Python 3.x
- C++ Compiler
- Virtual Environment (`virtualenv`)
- Required Python Libraries: `NumPy`, `Tabulate`

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/UnboundSB/PyBase.git
   cd PyBase
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the PyBase system:
   ```sh
   python main.py
   ```

## Folder Structure
```
PyBase/
│── pybase_python/         # Core Python modules
│   ├── storage_manager.py  # Handles database storage
│   ├── data_formatter.py   # Converts raw data into readable format
│   ├── data_filter.py      # Implements filtering and query logic
│── pybase_cpp/            # C++ modules for performance optimization
│── pybase-ui/             # AngularJS frontend
│── venv/                  # Virtual environment
│── README.md              # Project documentation
│── .gitignore             # Ignored files
```

## Usage
### Creating a Database
```python
from storage_manager import DatabaseManager
l
db = DatabaseManager("my_database")
```

### Creating Tables
```python
db.create_table("users", {"id": "PRIMARY KEY", "name": "TEXT", "age": "INTEGER"})
```

### Inserting Data
```python
db.insert("users", {"id": 1, "name": "Alice", "age": 25})
```

### Querying Data
```python
from data_filter import Select
query = Select("SELECT name AS user_name, age FROM users WHERE age > 20")
print(query.fetch())
```

## Contributing
1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch`
3. Commit changes: `git commit -m "Added new feature"`
4. Push to GitHub: `git push origin feature-branch`
5. Create a Pull Request

## License
MIT License

