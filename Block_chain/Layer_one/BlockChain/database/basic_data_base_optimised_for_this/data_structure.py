class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.data = []
        self.index = {}
        for column in columns:
            self.index[column] = {}

    def insert(self, values):
        row = dict(zip(self.columns, values))
        self.data.append(row)
        for column, value in row.items():
            if value not in self.index[column]:
                self.index[column][value] = []
            self.index[column][value].append(row)

    def query(self, conditions):
        results = self.data
        for column, value in conditions.items():
            results = self.index.get(column, {}).get(value, [])
        return results


class Database:
    def __init__(self):
        self.tables = {}

    def create_table(self, name, columns):
        self.tables[name] = Table(name, columns)

    def get_table(self, name):
        return self.tables.get(name)
