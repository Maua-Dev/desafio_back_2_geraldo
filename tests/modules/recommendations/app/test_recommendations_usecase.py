import pytest


from src.modules.recommendations.app.recommendations_usecase import RecommendationsUsecase
from src.shared.domain.repositories.purchase_repository_mock import PurchaseRepositoryMock
from src.shared.domain.enums.category_enum import CATEGORY
from src.shared.helpers.errors.domain_errors import EntityError

class Test_RecommendationsUsecase:

    def test_recommendations_usecase(self):
        repo = PurchaseRepositoryMock()
        usecase = RecommendationsUsecase(repo=repo)

        assert repo.get_category_from_user_id(user_id="3c0c67a5-2dc4-4b90-be13-73b7d29718f0") == [CATEGORY.CLOTHES.value]


    def test_recommendations_usecase_with_invalid_user_id(self):
        repo = PurchaseRepositoryMock()
        usecase = RecommendationsUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(user_id="3c0c67a5-2dc4-4b90-be13-73b7d29718f")
