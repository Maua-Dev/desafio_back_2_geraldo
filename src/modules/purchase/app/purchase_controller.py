from src.shared.helpers.external_interfaces.http_models import LambdaHttpRequest, LambdaHttpResponse
from src.shared.helpers.errors.usecase_errors import DuplicatedItem
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.modules.purchase.app.purchase_usecase import PurchaseUsecase
from src.modules.purchase.app.purchase_viewmodel import PurchaseViewmodel

class PurchaseController:

    def __init__(self, usecase: PurchaseUsecase):
        self.usecase = usecase

    def __call__(self, request: LambdaHttpRequest) -> LambdaHttpResponse:

        try:
            user_id = request.data.get("user_id")
            product_id = request.data.get("product_id")
            category = request.data.get("category")
            price = request.data.get("price")
            purchase_date = request.data.get("purchase_date")

            purchase = self.usecase(
                user_id=user_id,
                product_id=product_id,
                category=category,
                price=price,
                purchase_date=purchase_date
            )

            viewmodel = PurchaseViewmodel(purchase)
            return LambdaHttpResponse(status_code=200, body=viewmodel.to_dict())

        except DuplicatedItem as error:
            return LambdaHttpResponse(status_code=409, body={"message": str(error)})    

        except (EntityError, ForbiddenAction) as error:
            return LambdaHttpResponse(status_code=400, body={"message": str(error)})

        except Exception as error:
            return LambdaHttpResponse(status_code=500, body={"message": "Internal server error", "error": str(error)})
