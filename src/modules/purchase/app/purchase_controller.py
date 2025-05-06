from src.shared.domain.enums.category_enum import CATEGORY
from src.shared.helpers.errors.usecase_errors import DuplicatedItem
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.modules.purchase.app.purchase_usecase import PurchaseUsecase
from src.modules.purchase.app.purchase_viewmodel import PurchaseViewmodel
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.helpers.external_interfaces.http_codes import Conflict, Created, Forbidden, InternalServerError



class PurchaseController:

    def __init__(self, usecase: PurchaseUsecase):
        self.usecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:

        try:
            user_id = request.data.get("user_id")
            product_id = request.data.get("product_id")
            category = CATEGORY[request.data.get("category")]
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
            return Created(viewmodel.to_dict())

        except DuplicatedItem as error:
            return Conflict(body=error.message)    

        except (EntityError, ForbiddenAction) as error:
            return Forbidden(body=error.message)
        
        except Exception as error:
            return InternalServerError(body=error.args[0])


        except Exception as error:
            return InternalServerError(body=error.args[0])
