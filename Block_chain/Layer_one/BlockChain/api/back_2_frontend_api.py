from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from starlette.applications import Starlette
from starlette.routing import Route

# Sample transaction data
sample_transaction = {
    "senderID": "99xxxxxxxx",
    "amountReceived": 100.0,
    "transactionId": "123456789",
    "timestamp": "2024-05-20 12:04 PM",
}

# Define the GraphQL schema
type_defs = """
type TransactionSummary {
  senderID: String!
  amountReceived: Float!
}

type TransactionDetails {
  senderID: String!
  amountReceived: Float!
  transactionId: ID!
  timestamp: String!
}

type Query {
  getTransactionSummary(receiverId: String!): TransactionSummary!
  getTransactionDetails(receiverId: String!): TransactionDetails!
}
"""

# Create query and mutation types
query = QueryType()

# Define resolvers
@query.field("getTransactionSummary")
def resolve_transaction_summary(_, info, receiverId):
    return {
        "senderID": sample_transaction["senderID"],
        "amountReceived": sample_transaction["amountReceived"],
    }

@query.field("getTransactionDetails")
def resolve_transaction_details(_, info, receiverId):
    return sample_transaction

# Create executable schema
schema = make_executable_schema(type_defs, query)

# Run the server
app = Starlette(
    routes=[
        Route("/graphql", GraphQL(schema, debug=True)),
    ],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=4001)
#
# query {
#   getTransactionSummary(receiverId: "someReceiverId") {
#     senderID
#     amountReceived
#   }
#   getTransactionDetails(receiverId: "someReceiverId") {
#     senderID
#     amountReceived
#     transactionId
#     timestamp
#   }
# }
#
#