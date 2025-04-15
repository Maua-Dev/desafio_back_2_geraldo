from abc import ABC, abstractmethod
from typing import List, Optional
from src.shared.domain.entities.purchase import Purchase




class IChallengeRepository(ABC):

    @abstractmethod
    def create_purchase(self, purchase: Purchase) -> Purchase:
        pass

    @abstractmethod
    def purchase_already_exists(self, purchase: Purchase) -> bool:
        pass

    @abstractmethod
    def get_category_from_user_id(self, user_id: str) -> Optional[List[str]]:
        pass

    @abstractmethod
    def get_purchase_from_user_id_and_interval(self,user_id: str, start_date: int, end_date: int) -> Optional[List[str]]:
        pass

