class BudgetTracker:
    def __init__(self, budget: float = 0):
        # self.budget belongs to this specific instance
        self.budget = budget
        # This is just a class-wide constant, shared by all instances
        self.MIN_BUDGET = 0
    
    def set_budget(self, amount: float):
        # We can use self to access both the instance's budget
        # and the class-wide MIN_BUDGET
        if amount < self.MIN_BUDGET:
            raise ValueError("Budget cannot be negative")
        self.budget = amount
    
    def get_budget(self):
        # self tells Python which instance's budget to return
        return self.budget
    
    def track_budget(self, total_expenses: float):
        if self.budget <= 0:
            return "Please set a valid monthly budget first."
        
        remaining = self.budget - total_expenses
        status = (
            f"\n💸 Total expenses so far: ₹{total_expenses:.2f}\n"
            f"{'🚨 Budget exceeded by' if total_expenses > self.budget else '🟢 You have'} "
            f"₹{abs(remaining):.2f} {'over budget!' if total_expenses > self.budget else 'remaining for the month.'}"
        )
        return status
