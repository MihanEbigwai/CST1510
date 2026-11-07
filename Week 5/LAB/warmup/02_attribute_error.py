# completed warm-up

class Record:
    def __init__(self, label, amount, limit):
        self.label = label
        self.amount = amount    # stored as "amount", not "value"
        self.limit = limit

r = Record("R-001", 87.0, 100.0)
print(r.amount)
