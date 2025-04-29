from src.modules.purchase.app.purchase_controller import PurchaseController
from src.modules.purchase.app.purchase_usecase import PurchaseUsecase
from src.shared.domain.enums.category_enum import CATEGORY
from src.shared.domain.repositories.purchase_repository_mock import PurchaseRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest



class Test_PurchaseController:

    def test_purchase_controller(self):
        repo = PurchaseRepositoryMock()
        usecase = PurchaseUsecase(repo=repo)
        controller = PurchaseController(usecase=usecase)

        request = HttpRequest(
            body={
                "user_id": "3c0c67a5-2dc4-4b90-be13-73b7d29718f0",
                "product_id": "b5466cbf-581e-4f65-885f-247d03c96602",
                "category": CATEGORY.CLOTHES.value,
                "price": 50.0,
                "purchase_date": 1744644600
            },
            headers={
                "requester_user": {
                    "user_id": "3c0c67a5-2dc4-4b90-be13-73b7d29718f0"
                }
            }
        )

        response = controller(request)

        assert response.status_code == 201
        assert response.body["message"] == "the purchase has been created"
        assert response.body["purchase"]["price"] == 50.0

