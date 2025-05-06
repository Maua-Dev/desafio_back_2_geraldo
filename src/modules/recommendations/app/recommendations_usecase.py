from src.shared.domain.entities.purchase import Purchase
from src.shared.domain.enums.category_enum import CATEGORY
from src.shared.domain.repositories.challenge_repository_interface import IChallengeRepository
from src.shared.helpers.errors.usecase_errors import DuplicatedItem


class RecommendationsUsecase:
    user_id: str
    category: CATEGORY
    
    def __init__(self, repo: IChallengeRepository):
        self.repo = repo

    def __call__(self, user_id: str) -> CATEGORY:
        
        return self.repo.get_category_from_user_id(user_id=user_id)

