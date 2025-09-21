from src.models.expense import Expense

class ExpenseManager:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
    
    def get_all_expenses(self):
        return self.expenses
    
    def get_total_expenses(self):
        return sum(exp.amount for exp in self.expenses)
    
    def load_expenses(self, expenses: list):
        self.expenses = expenses
    
    def clear_expenses(self):
        self.expenses = []
