from src.modules.purchase_summary.app.purchase_summary_viewmodel import PurchaseSummaryViewmodel
from src.shared.domain.repositories.challenge_repository_interface import IChallengeRepository
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.http_codes import BadRequest, OK, InternalServerError
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse

from .purchase_summary_usecase import PurchaseSummaryUsecase

class PurchaseSummaryController:

    def __init__(self, usecase: PurchaseSummaryUsecase):
        self.usecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:

        try:
            user_id = request.data.get("user_id")
            start_date = request.data.get("start_date")
            end_date = request.data.get("end_date")

            if user_id is None:
                raise MissingParameters("user_id")
            if start_date is None:
                raise MissingParameters("start_date")
            if end_date is None:
                raise MissingParameters("end_date")

            result = self.usecase(user_id=user_id, start_date=start_date, end_date=end_date)

            viewmodel = PurchaseSummaryViewmodel(
                user_id=result["user_id"],
                start_date=result["start_date"],
                end_date=result["end_date"],
                total_spent=result["total_spent"],
                total_purchases=result["total_purchases"],
                category_breakdown=result["category_breakdown"]
            )

            return OK(viewmodel.to_dict())

        except MissingParameters as error:
            return BadRequest(body=f"Missing parameter: {error.message}")

        except EntityError as error:
            return BadRequest(body=f"Missing parameter: {error.message}")

        except Exception as error:
            return InternalServerError(body=f"Missing parameter: {error.message}")
