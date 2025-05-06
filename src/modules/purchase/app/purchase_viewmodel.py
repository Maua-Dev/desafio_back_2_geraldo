from src.shared.domain.entities import Purchase


class PurchaseViewmodel:
    user_id: str
    product_id: str
    category: str
    price: float
    purchase_date: int

    def __init__(self, purchase: Purchase):
        self.user_id = purchase.user_id
        self.product_id = purchase.product_id
        self.category = purchase.category.value if hasattr(purchase.category, 'value') else purchase.category
        self.price = purchase.price
        self.purchase_date = purchase.purchase_date

    def to_dict(self):
        return {
            'purchase': {
                'user_id': self.user_id,
                'product_id': self.product_id,
                'category': self.category if isinstance(self.category, str) else self.category.value,
                'price': self.price,
                'purchase_date': self.purchase_date
            },
            'message': "the purchase has been created"
        }
