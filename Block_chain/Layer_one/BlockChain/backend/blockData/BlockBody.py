class BlockBody:
    """
    Block is a storage container that stores transactions.
    """
    def __init__(self):
        self._height = None
        self._blocksize = None
        self._blockheader = None
        self._txcount = None
        self._txs = None
        self._data_size_limit = None
        self._form = {'changeable': None, 'non_exchangeable': None}
        self._user_transaction_number = None
        self._priority = {'scheduled': None}
        self._multichainable = None
        self._block_number = None
        self._mining_rate = None
        self._interaction_region = None
        self._encryption_dynamic_hash = None  # compilation of block
        self._type = {
            'random_allowed': None, 'static': None, 'lifetime': None,
            'upgradable': None, 'immutibilityExtent': None,
            'security_jumpers': None, 'api': None
        }
        self._lifetime = None
        self._data = None
        self._scheduled_time = {'form': None, 'send': None, 'receive': None}

    # Getter and Setter for Height
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    # Getter and Setter for Blocksize
    @property
    def blocksize(self):
        return self._blocksize

    @blocksize.setter
    def blocksize(self, value):
        self._blocksize = value

    # Getter and Setter for BlockHeader
    @property
    def blockheader(self):
        return self._blockheader

    @blockheader.setter
    def blockheader(self, value):
        self._blockheader = value

    # Getter and Setter for TxCount
    @property
    def txcount(self):
        return self._txcount

    @txcount.setter
    def txcount(self, value):
        self._txcount = value

    # Getter and Setter for Txs
    @property
    def txs(self):
        return self._txs

    @txs.setter
    def txs(self, value):
        self._txs = value

    # Getter and Setter for Data Size Limit
    @property
    def data_size_limit(self):
        return self._data_size_limit

    @data_size_limit.setter
    def data_size_limit(self, value):
        self._data_size_limit = value

    # Getter and Setter for Form
    @property
    def form(self):
        return self._form

    @form.setter
    def form(self, value):
        self._form = value

    # Getter and Setter for User Transaction Number
    @property
    def user_transaction_number(self):
        return self._user_transaction_number

    @user_transaction_number.setter
    def user_transaction_number(self, value):
        self._user_transaction_number = value

    # Getter and Setter for Priority
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value

    # Getter and Setter for Multichainable
    @property
    def multichainable(self):
        return self._multichainable

    @multichainable.setter
    def multichainable(self, value):
        self._multichainable = value

    # Getter and Setter for Block Number
    @property
    def block_number(self):
        return self._block_number

    @block_number.setter
    def block_number(self, value):
        self._block_number = value

    # Getter and Setter for Mining Rate
    @property
    def mining_rate(self):
        return self._mining_rate

    @mining_rate.setter
    def mining_rate(self, value):
        self._mining_rate = value

    # Getter and Setter for Interaction Region
    @property
    def interaction_region(self):
        return self._interaction_region

    @interaction_region.setter
    def interaction_region(self, value):
        self._interaction_region = value

    # Getter and Setter for Encryption Dynamic Hash
    @property
    def encryption_dynamic_hash(self):
        return self._encryption_dynamic_hash

    @encryption_dynamic_hash.setter
    def encryption_dynamic_hash(self, value):
        self._encryption_dynamic_hash = value

    # Getter and Setter for Type
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    # Getter and Setter for Lifetime
    @property
    def lifetime(self):
        return self._lifetime

    @lifetime.setter
    def lifetime(self, value):
        self._lifetime = value

    # Getter and Setter for Data
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    # Getter and Setter for Scheduled Time
    @property
    def scheduled_time(self):
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, value):
        self._scheduled_time = value
