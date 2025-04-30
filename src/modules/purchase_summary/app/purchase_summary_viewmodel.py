class PurchaseSummaryViewmodel:
    user_id: str
    start_date: int
    end_date: int
    total_spent: float
    total_purchases: int
    category_breakdown: dict[str, dict[str, float]] 

    def __init__(self, user_id: str, start_date: int, end_date: int, total_spent: float, total_purchases: int, category_breakdown: dict[str, dict[str, float]]):
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
        self.total_spent = total_spent
        self.total_purchases = total_purchases
        self.category_breakdown = category_breakdown

    def to_dict(self) -> dict:
        return {
            'purchase_summary': {
                'user_id': self.user_id,
                'start_date': self.start_date,
                'end_date': self.end_date,
                'total_spent': self.total_spent,
                'total_purchases': self.total_purchases,
                'category_breakdown': self.category_breakdown
            },
            'message': "The purchase summary has been created"
        }
