# emmanuel
class Transaction:
    def __init__(self, amount, category, description, date, user_id):
        self._amount = amount
        self._category = category
        self._description = description
        self._date = date
        self._user_id = user_id

    @property
    def amount(self):
        return self._amount

    @property
    def category(self):
        return self._category

    @property
    def description(self):
        return self._description

    @property
    def date(self):
        return self._date

    @property
    def user_id(self):
        return self._user_id

    def __str__(self):
        return f"{self.category} - Ksh {self.amount} - {self.description}"