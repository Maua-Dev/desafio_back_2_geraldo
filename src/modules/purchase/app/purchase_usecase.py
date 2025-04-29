from src.shared.domain.entities.purchase import Purchase
from src.shared.domain.enums.category_enum import CATEGORY
from src.shared.domain.repositories.challenge_repository_interface import IChallengeRepository
from src.shared.helpers.errors.usecase_errors import DuplicatedItem


class PurchaseUsecase:
    user_id: str
    product_id: str
    category: CATEGORY
    price: float
    purchase_date: int

    def __init__(self, repo: IChallengeRepository):
        self.repo = repo

    def __call__(self, user_id: str, product_id: str, category: CATEGORY, price: float, purchase_date) -> Purchase:
        
        purchase = Purchase(user_id=user_id, product_id = product_id, category=category, price=price,purchase_date=purchase_date)
        
        return self.repo.create_purchase(purchase=purchase)

