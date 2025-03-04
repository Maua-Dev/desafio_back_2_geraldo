from abc import ABC, abstractmethod
from typing import List

from src.shared.domain.entities import Purchase



class IChallengeRepository(ABC):

    @abstractmethod
    def post_new_purchase(self, purchase: Purchase) -> Purchase:
        pass

    @abstractmethod
    def get_purchase_by_user_id(self, purchase: Purchase) -> List[str]:
        pass

    @abstractmethod
    def get_purchase_by_user_id_in_interval(self, purchase: Purchase) -> List[str]:
        pass

