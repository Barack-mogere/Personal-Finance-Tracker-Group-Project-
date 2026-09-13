# emmanuel
from models.transaction import Transaction


class Income(Transaction):
    def __init__(self, amount, category, description, date, user_id):
        super().__init__(amount, category, description, date, user_id)

    def __str__(self):
        return f"Income: {self.category} - Ksh {self.amount} - {self.description}"