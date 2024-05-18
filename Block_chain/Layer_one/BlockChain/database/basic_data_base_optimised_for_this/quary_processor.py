from simple_dbms.data_structures import Database, Table
from simple_dbms.storage_engine import StorageEngine

class QueryProcessor:
    def __init__(self, database, storage_engine):
        self.database = database
        self.storage_engine = storage_engine

    def execute_query(self, query):
        command = query.get('command')
        if command == 'CREATE_TABLE':
            self.database.create_table(query['table_name'], query['columns'])
        elif command == 'INSERT':
            table = self.database.get_table(query['table_name'])
            if table:
                table.insert(query['values'])
                self.storage_engine.save_table(table)
        elif command == 'SELECT':
            table = self.database.get_table(query['table_name'])
            if table:
                return table.query(query['conditions'])
