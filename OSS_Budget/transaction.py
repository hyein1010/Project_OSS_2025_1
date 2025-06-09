
class Transaction:
    def __init__(self, date, category, description, amount, type_):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
        self.type = type_  # 'income' 또는 'expense'

    def __str__(self):
        return f"[{self.date}] {self.category} - {self.description}: {self.amount}원 ({self.type})"