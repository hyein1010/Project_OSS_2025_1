import datetime
from transaction import Transaction

class Budget:
    def __init__(self):
        self.transactions = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        transaction = Transaction(today, category, description, amount, 'expense')
        self.transactions.append(transaction)
        print("지출이 추가되었습니다.\n")

    def add_income(self, category, description, amount):
        today = datetime.date.today().isoformat()
        transaction = Transaction(today, category, description, amount, 'income')
        self.transactions.append(transaction)
        print("수입이 추가되었습니다.\n")

    def list_transactions(self):
        if not self.transactions:
            print("내역이 없습니다.\n")
            return
        print("\n[전체 내역]")
        for idx, t in enumerate(self.transactions, 1):
            color = "\033[91m" if t.type == 'expense' else "\033[92m"  # 빨강: expense, 초록: income
            reset = "\033[0m"
            print(f"{color}{idx}. {t}{reset}")
        print()

    def total_summary(self):
        income_total = sum(t.amount for t in self.transactions if t.type == 'income')
        expense_total = sum(t.amount for t in self.transactions if t.type == 'expense')
        balance = income_total - expense_total
        print(f"총 수입: {income_total}원")
        print(f"총 지출: {expense_total}원")
        print(f"잔액: {balance}원\n")

