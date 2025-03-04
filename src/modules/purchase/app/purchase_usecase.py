from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.shared.domain.entities import Purchase


class PurchaseUsecase:
    user_id: str
    product_id: str
    category: str
    price: float
    purchase_date: int

    def __init__(self, purchase: Purchase):
        self.user_id = purchase.user_id
        self.product_id = purchase.product_id
        self.category = purchase.cateogry
        self.price = purchase.price
        self.purchase_date = purchase.purchase_date

    def to_dict(self):
        return {
            'purchase': {
                'user_id': self.user_id,
                'product_id': self.product_id,
                'category': self.category,
                'price': self.price,
                'purchase_date': self.purchase_date
            },

            'message': "the purchase has been created"
        }
