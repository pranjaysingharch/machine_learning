import csv
import os
from pathlib import Path
from src.models.expense import Expense


class FileHandler:
    def __init__(self, filename: str = "expenses_tracker.csv"):
        # Get the absolute path to the src/data directory
        base_path = Path(__file__).parent.parent / 'data'
        base_path.mkdir(exist_ok=True)  # Create the data directory if it doesn't exist
        self.filename = str(base_path / filename)
        self.fieldnames = ['date', 'category', 'amount', 'description']
    
    def load_expenses(self) -> list:
        expenses = []
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    expenses.append(Expense.from_dict(row))
        except FileNotFoundError:
            print("No previous data found. Starting fresh.")
        return expenses
    
    def save_expenses(self, expenses: list):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows([exp.to_dict() for exp in expenses])
