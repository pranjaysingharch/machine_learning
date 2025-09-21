from src.interface.ui import UI
from src.manager.budget_tracker import BudgetTracker
from src.manager.expense_manager import ExpenseManager
from src.util.file_handler import FileHandler


def main():
    # Initialize components
    file_handler = FileHandler()
    expense_manager = ExpenseManager()
    budget_tracker = BudgetTracker()
    
    # Load existing expenses
    expenses = file_handler.load_expenses()
    expense_manager.load_expenses(expenses)
    
    # Set initial budget
    budget_tracker.set_budget(UI.get_budget_input())
    
    while True:
        choice = UI.display_menu()
        if choice == '1':
            expense = UI.get_expense_input()
            if expense:
                expense_manager.add_expense(expense)
                file_handler.save_expenses(expense_manager.get_all_expenses())
                print("✅ Expense added successfully.")
            else:
                print("❌ Expense entry cancelled.")
        
        elif choice == '2':
            UI.display_expenses(expense_manager.get_all_expenses())
        
        elif choice == '3':
            total = expense_manager.get_total_expenses()
            status = budget_tracker.track_budget(total)
            print(status)
        
        elif choice == '4':
            file_handler.save_expenses(expense_manager.get_all_expenses())
            print("Expenses saved successfully.")
        
        elif choice == '5':
            print("Thank you for using the Personal Expense Tracker! Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()