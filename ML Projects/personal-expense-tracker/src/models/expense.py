from datetime import datetime

class Expense:
    # Predefined categories for expenses
    CATEGORIES = ['Food', 'Transport', 'Bills', 'Shopping', 'Entertainment', 'Health', 'Education', 'Other']
    
    def __init__(self, date: str, category: str, amount: float, description: str):
        self.validate_date(date)
        self.validate_amount(amount)
        self.validate_category(category)
        self.validate_description(description)
        
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description
    
    @staticmethod
    def validate_date(date: str) -> None:
        try:
            parsed_date = datetime.strptime(date, '%Y-%m-%d')
            if parsed_date > datetime.now():
                raise ValueError("📅 Future dates are not allowed. Please enter today's date or a past date.")
        except ValueError as e:
            if "Future dates" in str(e):
                raise e
            raise ValueError("📅 Invalid date format!\n   Please use YYYY-MM-DD format (e.g., 2025-05-30)\n   Today's date is: " + datetime.now().strftime('%Y-%m-%d'))

    @staticmethod
    def validate_amount(amount: float) -> None:
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("💰 Amount must be greater than zero!\n   Example valid amounts: 100, 50.50, 1500.75")
            if amount > 1000000:  # Add reasonable upper limit
                raise ValueError("💰 Amount seems too large!\n   Please verify the amount or split into multiple expenses.")
        except ValueError as e:
            if "Amount must be" in str(e) or "Amount seems" in str(e):
                raise e
            raise ValueError("💰 Invalid amount format!\n   Please enter a valid number (e.g., 100, 50.50)")

    @staticmethod
    def validate_category(category: str) -> None:
        if not category or not category.strip():
            suggestions = ", ".join(Expense.CATEGORIES)
            raise ValueError(f"📝 Category cannot be empty!\n   Suggested categories: {suggestions}")
        if len(category) > 50:
            raise ValueError("📝 Category name is too long!\n   Please keep it under 50 characters")
        
    @staticmethod
    def validate_description(description: str) -> None:
        if not description or not description.strip():
            raise ValueError("📝 Please add a brief description of your expense!\n   Example: 'Grocery shopping at Walmart'")
        if len(description) > 200:
            current_length = len(description)
            raise ValueError(f"📝 Description is too long! ({current_length}/200 characters)\n   Please shorten it to less than 200 characters")
    
    def to_dict(self):
        return {
            'date': self.date,
            'category': self.category,
            'amount': self.amount,
            'description': self.description
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            date=data['date'],
            category=data['category'],
            amount=float(data['amount']),
            description=data['description']
        )

