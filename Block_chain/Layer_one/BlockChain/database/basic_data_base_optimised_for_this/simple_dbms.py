from simple_dbms.data_structures import Database
from simple_dbms.storage_engine import StorageEngine
from simple_dbms.query_processor import QueryProcessor
from simple_dbms.transaction import Transaction

class SimpleDBMS:
    def __init__(self):
        self.database = Database()
        self.storage_engine = StorageEngine()
        self.query_processor = QueryProcessor(self.database, self.storage_engine)

    def execute(self, query):
        return self.query_processor.execute_query(query)

# Example usage:
if __name__ == "__main__":
    dbms = SimpleDBMS()

    # Create a table
    dbms.execute({'command': 'CREATE_TABLE', 'table_name': 'users', 'columns': ['id', 'name', 'email']})

    # Insert data
    dbms.execute({'command': 'INSERT', 'table_name': 'users', 'values': [1, 'Alice', 'alice@example.com']})
    dbms.execute({'command': 'INSERT', 'table_name': 'users', 'values': [2, 'Bob', 'bob@example.com']})

    # Select data
    result = dbms.execute({'command': 'SELECT', 'table_name': 'users', 'conditions': {'name': 'Alice'}})
    print(result)

    # Start a transaction
    transaction = Transaction()
    transaction.add_operation({'command': 'INSERT', 'table_name': 'users', 'values': [3, 'Charlie', 'charlie@example.com']})
    transaction.add_operation({'command': 'INSERT', 'table_name': 'users', 'values': [4, 'Dave', 'dave@example.com']})
    transaction.commit(dbms.query_processor)

    # Verify data
    result = dbms.execute({'command': 'SELECT', 'table_name': 'users', 'conditions': {}})
    print(result)
