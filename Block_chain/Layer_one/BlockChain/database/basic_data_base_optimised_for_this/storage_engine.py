import json
import os
from cryptography.fernet import Fernet
from simple_dbms.data_structures import Table

class StorageEngine:
    def __init__(self, db_directory='db_files', key_file='key.key'):
        self.db_directory = db_directory
        if not os.path.exists(self.db_directory):
            os.makedirs(self.db_directory)

        self.key = self.load_key(key_file)
        self.cipher = Fernet(self.key)

    def load_key(self, key_file):
        if os.path.exists(key_file):
            with open(key_file, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, 'wb') as f:
                f.write(key)
            return key

    def save_table(self, table):
        file_path = os.path.join(self.db_directory, f'{table.name}.json')
        with open(file_path, 'w') as f:
            data = {
                'columns': table.columns,
                'data': table.data
            }
            encrypted_data = self.cipher.encrypt(json.dumps(data).encode()).decode()
            f.write(encrypted_data)

    def load_table(self, table_name):
        file_path = os.path.join(self.db_directory, f'{table_name}.json')
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                encrypted_data = f.read()
                data = json.loads(self.cipher.decrypt(encrypted_data.encode()).decode())
                table = Table(table_name, data['columns'])
                table.data = data['data']
                for row in table.data:
                    for column, value in row.items():
                        if value not in table.index[column]:
                            table.index[column][value] = []
                        table.index[column][value].append(row)
                return table
        return None
