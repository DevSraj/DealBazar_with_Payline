from Blockchain.Backend.core.blockheader import BlockHeader
from Blockchain.Backend.core.Tx import Tx
from Blockchain.Backend.util.util import (little_endian_to_int, int_to_little_endian, encode_varint, read_varint)

class Block:
    def __init__(self, height, blocksize, blockheader, txcount, txs, data_size_limit, form,
                 user_transaction_number, priority, multichainable, block_number, mining_rate,
                 interaction_region, encryption_dynamic_hash, block_type, lifetime, data, scheduled_time):
        self._height = height
        self._blocksize = blocksize
        self._blockheader = blockheader
        self._txcount = txcount
        self._txs = txs
        self._data_size_limit = data_size_limit
        self._form = form
        self._user_transaction_number = user_transaction_number
        self._priority = priority
        self._multichainable = multichainable
        self._block_number = block_number
        self._mining_rate = mining_rate
        self._interaction_region = interaction_region
        self._encryption_dynamic_hash = encryption_dynamic_hash
        self._block_type = block_type
        self._lifetime = lifetime
        self._data = data
        self._scheduled_time = scheduled_time

    @classmethod
    def parse(cls, s):
        height = little_endian_to_int(s.read(4))
        blocksize = little_endian_to_int(s.read(4))
        blockheader = BlockHeader.parse(s)
        txcount = read_varint(s)

        txs = []

        for _ in range(txcount):
            txs.append(Tx.parse(s))

        return cls(height, blocksize, blockheader, txcount, txs, None, None, None, None, None, None, None, None, None, None, None, None, None)

    def serialize(self):
        result = int_to_little_endian(self._height, 4)
        result += int_to_little_endian(self._blocksize, 4)
        result += self._blockheader.serialize()
        result += encode_varint(self._txcount)

        for tx in self._txs:
            result += tx.serialize()

        return result

    @classmethod
    def to_obj(cls, lastblock):
        blockheader = BlockHeader(
            lastblock['_blockheader']['version'],
            bytes.fromhex(lastblock['_blockheader']['prevBlockHash']),
            bytes.fromhex(lastblock['_blockheader']['merkleRoot']),
            lastblock['_blockheader']['timestamp'],
            bytes.fromhex(lastblock['_blockheader']['bits'])
        )

        blockheader.nonce = int_to_little_endian(lastblock['_blockheader']['nonce'], 4)

        txs = [Tx.to_obj(tx) for tx in lastblock['_txs']]

        blockheader.blockHash = bytes.fromhex(lastblock['_blockheader']['blockHash'])

        return cls(
            lastblock['_height'],
            lastblock['_blocksize'],
            blockheader,
            lastblock['_txcount'],
            txs,
            lastblock['_data_size_limit'],
            lastblock['_form'],
            lastblock['_user_transaction_number'],
            lastblock['_priority'],
            lastblock['_multichainable'],
            lastblock['_block_number'],
            lastblock['_mining_rate'],
            lastblock['_interaction_region'],
            lastblock['_encryption_dynamic_hash'],
            lastblock['_block_type'],
            lastblock['_lifetime'],
            lastblock['_data'],
            lastblock['_scheduled_time']
        )

    def to_dict(self):
        dt = {
            '_height': self._height,
            '_blocksize': self._blocksize,
            '_blockheader': self._blockheader.to_dict(),
            '_txcount': self._txcount,
            '_txs': [tx.to_dict() for tx in self._txs],
            '_data_size_limit': self._data_size_limit,
            '_form': self._form,
            '_user_transaction_number': self._user_transaction_number,
            '_priority': self._priority,
            '_multichainable': self._multichainable,
            '_block_number': self._block_number,
            '_mining_rate': self._mining_rate,
            '_interaction_region': self._interaction_region,
            '_encryption_dynamic_hash': self._encryption_dynamic_hash,
            '_block_type': self._block_type,
            '_lifetime': self._lifetime,
            '_data': self._data,
            '_scheduled_time': self._scheduled_time
        }
        return dt
