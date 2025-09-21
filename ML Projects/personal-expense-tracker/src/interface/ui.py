from datetime import datetime
from src.models.expense import Expense


class UI:
    @staticmethod
    def get_expense_input() -> Expense:
        while True:
            try:
                print("\n=== Add New Expense ===")
                print("(Press Ctrl+C at any time to cancel)")
                
                # Show today's date as default
                today = datetime.now().strftime('%Y-%m-%d')
                date = input(f"Enter date (YYYY-MM-DD) [default: {today}]: ").strip()
                if not date:
                    date = today

                # Show available categories
                print("\nAvailable categories:")
                for i, cat in enumerate(Expense.CATEGORIES, 1):
                    print(f"{i}. {cat}")
                category = input("Enter category (or number from list): ").strip()
                try:
                    cat_idx = int(category) - 1
                    if 0 <= cat_idx < len(Expense.CATEGORIES):
                        category = Expense.CATEGORIES[cat_idx]
                except ValueError:
                    pass  # User entered a custom category, which is fine

                amount = input("Enter amount: ₹").strip()
                description = input("Enter description: ").strip()
                
                # Create and validate expense
                expense = Expense(date, category, float(amount), description)
                
                # Show summary before confirming
                print("\nExpense Summary:")
                print(f"📅 Date: {expense.date}")
                print(f"📝 Category: {expense.category}")
                print(f"💰 Amount: ₹{expense.amount:.2f}")
                print(f"📝 Description: {expense.description}")
                
                if input("\nLooks good? (Y/n): ").lower() not in ['n', 'no']:
                    return expense
                print("Ok, let's try again...")
                
            except ValueError as e:
                print(f"\n❌ Error: {str(e)}")
                if input("\nWould you like to try again? (Y/n): ").lower() in ['n', 'no']:
                    return None
            except KeyboardInterrupt:
                print("\n\nExpense entry cancelled.")
                return None

    @staticmethod
    def get_budget_input() -> float:
        while True:
            try:
                amount_str = input("\nEnter your monthly budget: ₹").strip()
                amount = float(amount_str)
                if amount <= 0:
                    print("❌ Budget must be greater than zero!")
                    continue
                return amount
            except ValueError:
                print("❌ Please enter a valid number!")
            except KeyboardInterrupt:
                print("\nBudget setting cancelled.")
                return 0

    @staticmethod
    def display_expenses(expenses: list):
        if not expenses:
            print("\n📭 No expenses recorded yet.")
            return
            
        total = sum(exp.amount for exp in expenses)
        print("\n📋 List of Expenses:")
        print("ID  | Date       | Category      | Amount        | Description")
        print("-" * 70)
        
        for idx, exp in enumerate(expenses, start=1):
            print(f"{idx:2d}. | {exp.date:10} | {exp.category:<12} | ₹{exp.amount:>9.2f} | {exp.description}")
        
        print("-" * 70)
        print(f"Total Expenses: ₹{total:,.2f}")

    @staticmethod
    def display_menu():
        print("\n=== Personal Expense Tracker ===")
        print("1. 📝 Add Expense")
        print("2. 📋 View Expenses")
        print("3. 💰 Check Budget Status")
        print("4. 💾 Save Expenses")
        print("5. 🚪 Exit")
        return input("\nEnter your choice (1-5): ")
