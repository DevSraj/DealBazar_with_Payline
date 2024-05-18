from cryptography.fernet import Fernet
import json
import os

class Block:
    def __init__(self):
        self.height = None
        self.blocksize = None
        self.blockheader = None
        self.txcount = None
        self.txs = None

class BlockHeader:
    def __init__(self, version, prevBlockHash, merkleRoot, timestamp, bits):
        self.version = version
        self.prevBlockHash = prevBlockHash
        self.merkleRoot = merkleRoot
        self.timestamp = timestamp
        self.bits = bits
        self.nonce = 0
        self.blockHash = ""

class BlockchainDB:
    def __init__(self, db_directory='blockchain_db', key_file='key.key'):
        self.db_directory = db_directory
        if not os.path.exists(self.db_directory):
            os.makedirs(self.db_directory)
        self.blocks_file = os.path.join(self.db_directory, 'blocks.json')
        self.blockheaders_file = os.path.join(self.db_directory, 'blockheaders.json')

        self.key = self.load_key(key_file)
        self.cipher = Fernet(self.key)

        # Initialize the files if they do not exist
        if not os.path.exists(self.blocks_file):
            with open(self.blocks_file, 'w') as f:
                f.write(self.cipher.encrypt(json.dumps([]).encode()).decode())
        if not os.path.exists(self.blockheaders_file):
            with open(self.blockheaders_file, 'w') as f:
                f.write(self.cipher.encrypt(json.dumps([]).encode()).decode())

    def load_key(self, key_file):
        if os.path.exists(key_file):
            with open(key_file, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, 'wb') as f:
                f.write(key)
            return key

    def read_encrypted_file(self, file_path):
        with open(file_path, 'r') as f:
            encrypted_data = f.read()
            decrypted_data = self.cipher.decrypt(encrypted_data.encode()).decode()
            return json.loads(decrypted_data)

    def write_encrypted_file(self, file_path, data):
        with open(file_path, 'w') as f:
            encrypted_data = self.cipher.encrypt(json.dumps(data).encode()).decode()
            f.write(encrypted_data)

    def add_blockheader(self, blockheader):
        blockheaders = self.read_encrypted_file(self.blockheaders_file)
        blockheader_id = len(blockheaders) + 1
        blockheader_data = {
            'id': blockheader_id,
            'version': blockheader.version,
            'prevBlockHash': blockheader.prevBlockHash,
            'merkleRoot': blockheader.merkleRoot,
            'timestamp': blockheader.timestamp,
            'bits': blockheader.bits,
            'nonce': blockheader.nonce,
            'blockHash': blockheader.blockHash
        }
        blockheaders.append(blockheader_data)
        self.write_encrypted_file(self.blockheaders_file, blockheaders)
        return blockheader_id

    def add_block(self, block):
        blockheader_id = self.add_blockheader(block.blockheader)
        blocks = self.read_encrypted_file(self.blocks_file)
        block_id = len(blocks) + 1
        block_data = {
            'id': block_id,
            'height': block.height,
            'blocksize': block.blocksize,
            'blockheader_id': blockheader_id,
            'txcount': block.txcount,
            'txs': block.txs
        }
        blocks.append(block_data)
        self.write_encrypted_file(self.blocks_file, blocks)
        return block_id

    def get_block(self, block_id):
        blocks = self.read_encrypted_file(self.blocks_file)
        for block_data in blocks:
            if block_data['id'] == block_id:
                block = Block()
                block.height = block_data['height']
                block.blocksize = block_data['blocksize']
                block.txcount = block_data['txcount']
                block.txs = block_data['txs']

                blockheader_id = block_data['blockheader_id']
                block.blockheader = self.get_blockheader(blockheader_id)
                return block
        return None

    def get_blockheader(self, blockheader_id):
        blockheaders = self.read_encrypted_file(self.blockheaders_file)
        for blockheader_data in blockheaders:
            if blockheader_data['id'] == blockheader_id:
                blockheader = BlockHeader(
                    version=blockheader_data['version'],
                    prevBlockHash=blockheader_data['prevBlockHash'],
                    merkleRoot=blockheader_data['merkleRoot'],
                    timestamp=blockheader_data['timestamp'],
                    bits=blockheader_data['bits']
                )
                blockheader.nonce = blockheader_data['nonce']
                blockheader.blockHash = blockheader_data['blockHash']
                return blockheader
        return None

    def update_block(self, block_id, block):
        blocks = self.read_encrypted_file(self.blocks_file)
        for block_data in blocks:
            if block_data['id'] == block_id:
                block_data['height'] = block.height
                block_data['blocksize'] = block.blocksize
                block_data['blockheader_id'] = self.add_blockheader(block.blockheader)
                block_data['txcount'] = block.txcount
                block_data['txs'] = block.txs
                break
        self.write_encrypted_file(self.blocks_file, blocks)

    def delete_block(self, block_id):
        blocks = self.read_encrypted_file(self.blocks_file)
        blocks = [block for block in blocks if block['id'] != block_id]
        self.write_encrypted_file(self.blocks_file, blocks)

# Example usage:
blockchain_db = BlockchainDB()

block_header = BlockHeader(version="1.0", prevBlockHash="0000...", merkleRoot="abcd...", timestamp="2023-01-01", bits="1d00ffff")
block = Block()
block.height = 1
block.blocksize = 1024
block.blockheader = block_header
block.txcount = 2
block.txs = ["tx1", "tx2"]

# Add block
block_id = blockchain_db.add_block(block)
print(f"Block added with ID: {block_id}")

# Get block
retrieved_block = blockchain_db.get_block(block_id)
print(f"Retrieved Block: {retrieved_block.__dict__}")

# Update block
block.txcount = 3
block.txs.append("tx3")
blockchain_db.update_block(block_id, block)

# Get updated block
updated_block = blockchain_db.get_block(block_id)
print(f"Updated Block: {updated_block.__dict__}")

# Delete block
blockchain_db.delete_block(block_id)
print(f"Block with ID {block_id} deleted")
