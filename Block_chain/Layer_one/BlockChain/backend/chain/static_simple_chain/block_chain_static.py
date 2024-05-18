

# Import the necessary classes
# from block import Block
# from block_header import BlockHeader
# from storing_data_structure import initiate_storing_datastructure
# from genesis_block import GenesisBlock

class BlockChainStatic:
    #must initiate class variable for blocks some data genrally headers
    def __init__(self):
        self.store_chain = initiate_storing_datastructure()
        #add genesis_block_too

    def addBlock(self, block_body, block_header):
        # Create a new block
        new_block = Block()

        # Set the block attributes
        new_block.Txs = block_body
        new_block.BlockHeader = block_header

        # Add the new block to the storage structure
        self.store_chain.append(new_block)

        # Return the new block
        return new_block

# Example usage:
# blockchain = BlockChainStatic()
# block_header = BlockHeader(version, prevBlockHash, merkleRoot, timestamp, bits)
# block_body = [transaction1, transaction2, ...]
# new_block = blockchain.addBlock(block_body, block_header)
