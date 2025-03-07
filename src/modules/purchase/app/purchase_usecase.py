from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.shared.domain.repositories.challenge_repository_interface import IChallengeRepository
from src.shared.domain.entities import Purchase
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, NoItemsFound


class PurchaseUsecase:
    user_id: str
    product_id: str
    category: str
    price: float
    purchase_date: int

    def __init__(self, repo: IChallengeRepository):
        self.repo = repo

    def __call__(self, user_id: str, product_id: str, category: str, price: float, purchase_date) -> Purchase:

        if self.repo.create_purchase(purchase=purchase) is not None:
            raise DuplicatedItem("Purchase already exists")
        
        if self.repo.create_purchase(price <= 0) is not None:
            raise ForbiddenAction("Price can't be 0 or lower")
        
        
        purchase = Purchase(user_id=user_id, product_id = product_id, category=category, price=price,purchase_date=purchase_date)

        return self.repo.create_purchase
    
