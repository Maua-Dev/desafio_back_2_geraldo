import pytest

from src.modules.purchase_summary.app.purchase_summary_usecase import PurchaseSummaryUsecase
from src.modules.purchase_summary.app.purchase_summary_controller import PurchaseSummaryController
from src.shared.domain.repositories.purchase_repository_mock import PurchaseRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, OK


class TestPurchaseSummaryController:

    def test_purchase_summary_success(self):
        repo = PurchaseRepositoryMock()
        usecase = PurchaseSummaryUsecase(repo)
        controller = PurchaseSummaryController(usecase)

        request = HttpRequest(body={
            "user_id": "3c0c67a5-2dc4-4b90-be13-73b7d29718f0",
            "start_date": 1744644600,
            "end_date": 1744659000
        })

        response = controller(request)

        assert response.status_code == 200
        assert response.body["purchase_summary"]["user_id"] == "3c0c67a5-2dc4-4b90-be13-73b7d29718f0"


    def test_purchase_summary_missing_user_id(self):
        repo = PurchaseRepositoryMock()
        usecase = PurchaseSummaryUsecase(repo)
        controller = PurchaseSummaryController(usecase)

        request = HttpRequest(body={
            "start_date": 1744644600,
            "end_date": 1744659000
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Missing parameter: Field user_id is missing"

    def test_purchase_summary_missing_start_date(self):
        repo = PurchaseRepositoryMock()
        usecase = PurchaseSummaryUsecase(repo)
        controller = PurchaseSummaryController(usecase)

        request = HttpRequest(body={
            "user_id": "3c0c67a5-2dc4-4b90-be13-73b7d29718f0",
            "end_date": 1744659000
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Missing parameter: Field start_date is missing"

    def test_purchase_summary_missing_end_date(self):
        repo = PurchaseRepositoryMock()
        usecase = PurchaseSummaryUsecase(repo)
        controller = PurchaseSummaryController(usecase)

        request = HttpRequest(body={
            "user_id": "3c0c67a5-2dc4-4b90-be13-73b7d29718f0",
            "start_date": 1744644600
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Missing parameter: Field end_date is missing"
