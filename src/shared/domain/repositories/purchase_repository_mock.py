from typing import List, Optional
from collections import Counter

from src.shared.domain.entities.purchase import Purchase
from src.shared.domain.enums.category_enum import CATEGORY
from src.shared.domain.repositories.challenge_repository_interface import IChallengeRepository
from src.shared.helpers.errors.domain_errors import EntityError

class PurchaseRepositoryMock(IChallengeRepository):
    pruchase_list: list[Purchase] 

    def __init__(self):
        self.purchase_list = [

            Purchase(user_id="3c0c67a5-2dc4-4b90-be13-73b7d29718f0", product_id="7aa45600-3e44-46ca-8064-aa90874288cf", 
                     category=CATEGORY.CLOTHES, price= 25.0, purchase_date= 1744644600),
            Purchase(user_id="b5466cbf-581e-4f65-885f-247d03c96602", product_id="34b53079-824e-48e6-8ac2-fa6a5b0ae9ab", 
                     category=CATEGORY.CLOTHES, price= 50.0, purchase_date= 1744651800),
            Purchase(user_id="a4fa15ac-31c6-468e-ae59-88274d74b19b", product_id="7e39865f-158f-40a1-94e1-8592aed1f74f", 
                     category=CATEGORY.CLOTHES, price= 75.0, purchase_date= 1744655400),
            Purchase(user_id="6481c09f-83bb-4175-a6af-1161fdff3b8b", product_id="1b6d5541-0f33-4cac-8217-c593bca7611f",
                      category=CATEGORY.CLOTHES, price= 100.0, purchase_date= 1744659000)

        ]

    def create_purchase(self, purchase: Purchase) -> Purchase:
        self.purchase_list.append(purchase)
        return purchase
    
    def get_category_from_user_id(self, user_id: str) -> Optional[List[str]]:
        categories = [
            purchase.category.value
            for purchase in self.purchase_list
            if purchase.user_id == user_id
        ]

        if not categories:
            raise EntityError("User ID not found")

        counter = Counter(categories)
        max_count = max(counter.values())
        most_common_categories = [cat for cat, count in counter.items() if count == max_count]

        return most_common_categories

    
    def get_purchase_from_user_id_and_interval(self,user_id: str, start_date: int, end_date: int) -> Optional[List[str]]:
        categories = [
            purchase.category.value
            for purchase in self.purchase_list
            if purchase.user_id == user_id and start_date <= purchase.purchase_date <= end_date
        ]

        if not categories:
            return None

        counter = Counter(categories)
        max_count = max(counter.values())
        most_common_categories = [cat for cat, count in counter.items() if count == max_count]

        return most_common_categories
