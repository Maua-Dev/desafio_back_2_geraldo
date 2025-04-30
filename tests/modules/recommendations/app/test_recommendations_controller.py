import pytest
from src.modules.recommendations.app.recommendations_controller import RecommendationsController
from src.modules.recommendations.app.recommendations_usecase import RecommendationsUsecase

from src.shared.domain.repositories.challenge_repository_interface import IChallengeRepository
from src.shared.domain.repositories.purchase_repository_mock import PurchaseRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest


def test_recommendations_controller():
    repo = PurchaseRepositoryMock()
    usecase = RecommendationsUsecase(repo)
    controller = RecommendationsController(usecase)

    request = HttpRequest(body={"user_id": "3c0c67a5-2dc4-4b90-be13-73b7d29718f0"})
    response = controller(request)

    assert response.status_code == 200
    assert response.body == {
        "message": "Success",
        "recommended_categories": {
            "recommended_categories": ["CLOTHES"]
        }
    }