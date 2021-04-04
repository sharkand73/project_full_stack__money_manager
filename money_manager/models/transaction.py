class Transaction:
    def __init__(self, date, merchant, amount, tag, id = None):
        self.date = date
        self.merchant = merchant
        self.amount = amount
        self.tag = tag
        self.id = id
        