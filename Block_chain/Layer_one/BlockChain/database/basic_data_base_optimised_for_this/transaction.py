class Transaction:
    def __init__(self):
        self.operations = []

    def add_operation(self, operation):
        self.operations.append(operation)

    def commit(self, query_processor):
        for operation in self.operations:
            query_processor.execute_query(operation)
