class Budget:
    def __init__(self, name, start_date, end_date, amount, id=None):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.amount = amount
        self.id = id
        self.color = ""

    def time_period(self):
        time_period = (self.end_date - self.start_date).days + 1
        return time_period 
        
