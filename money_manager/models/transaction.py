class Transaction:
    def __init__(self, merchant, amount, tag, id = None):
        self.merchant = merchant
        self.amount = amount
        self.tag = tag
        self.id = id
        