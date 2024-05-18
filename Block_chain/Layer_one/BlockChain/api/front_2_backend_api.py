from ariadne import QueryType, MutationType, make_executable_schema
from ariadne.asgi import GraphQL
from starlette.applications import Starlette
from starlette.routing import Route

# Define the GraphQL schema
type_defs = """
type TransactionInitiation {
  senderAddress: String!
  receiverAddress: String!
  transactionAmount: Float!
  priority: Int!
  status: String!
}

input TransactionInput {
  senderAddress: String!
  transactionAmount: Float!
  receiverAddress: String!
}

type Query {
  _empty: String
}

type Mutation {
  initiateTransaction(input: TransactionInput!): TransactionInitiation!
}
"""

# Create query and mutation types
query = QueryType()
mutation = MutationType()

# Define resolvers
@query.field("_empty")
def resolve_empty(*_):
    return "This is a placeholder"

@mutation.field("initiateTransaction")
def resolve_initiate_transaction(_, info, input):
    sender_address = input["senderAddress"]
    transaction_amount = input["transactionAmount"]
    receiver_address = input["receiverAddress"]

    # Calculate priority based on transaction amount
    priority = 1 if transaction_amount < 50 else 2 if transaction_amount < 100 else 3

    # Simulate blockchain transaction initiation
    status = "Transaction initiated, pending confirmation"

    return {
        "senderAddress": sender_address,
        "receiverAddress": receiver_address,
        "transactionAmount": transaction_amount,
        "priority": priority,
        "status": status,
    }

# Create executable schema
schema = make_executable_schema(type_defs, [query, mutation])

# Run the server
app = Starlette(
    routes=[
        Route("/graphql", GraphQL(schema, debug=True)),
    ],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)


    #mutation {
    #  initiateTransaction(input: {
    #    senderAddress: "0xSenderAddressExample",
    #    receiverAddress: "0xReceiverAddressExample",
    #    transactionAmount: 75.0
    #  }) {
    #    senderAddress
    #    receiverAddress
    #    transactionAmount
    #    priority
    #    status
    #  }
    #}