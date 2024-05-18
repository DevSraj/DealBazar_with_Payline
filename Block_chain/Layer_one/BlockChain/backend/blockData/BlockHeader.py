


class BlockHeader:
    def __init__(self, version, prevBlockHash, merkleRoot, timestamp, bits):
        self.version = version
        self.prevBlockHash = prevBlockHash
        self.merkleRoot = merkleRoot
        self.timestamp = timestamp
        self.bits = bits
        self.nonce = 0
        self.blockHash = ""
        self._from_account = None
        self._to_account = None

        self._nounce = None
        self._timestamp = {'form': None, 'send': None, 'receive': None}
        self._hash_of_previous = None
        self._encrypted_ip = {'sender': None, 'receiver': None}

        self._user_points = {'sender': None, 'receiver': None, 'ai_fraud_detection': None}
        self._supply = None

    # Getter and Setter for From Account
    @property
    def from_account(self):
        return self._from_account

    @from_account.setter
    def from_account(self, value):
        self._from_account = value

    # Getter and Setter for To Account
    @property
    def to_account(self):
        return self._to_account

    @to_account.setter
    def to_account(self, value):
        self._to_account = value

    # Getter and Setter for Nounce
    @property
    def nounce(self):
        return self._nounce

    @nounce.setter
    def nounce(self, value):
        self._nounce = value

    # Getter and Setter for Timestamp
    @property
    def timestamp_data(self):
        return self._timestamp

    @timestamp_data.setter
    def timestamp_data(self, value):
        self._timestamp = value

    # Getter and Setter for Hash of Previous Block
    @property
    def hash_of_previous(self):
        return self._hash_of_previous

    @hash_of_previous.setter
    def hash_of_previous(self, value):
        self._hash_of_previous = value

    # Getter and Setter for Encrypted IP
    @property
    def encrypted_ip(self):
        return self._encrypted_ip

    @encrypted_ip.setter
    def encrypted_ip(self, value):
        self._encrypted_ip = value

    # Getter and Setter for User Points
    @property
    def user_points(self):
        return self._user_points

    @user_points.setter
    def user_points(self, value):
        self._user_points = value

    # Getter and Setter for Supply
    @property
    def supply(self):
        return self._supply

    @supply.setter
    def supply(self, value):
        self._supply = value
