from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.modules.recommendations.app.recommendations_usecase import RecommendationsUsecase
from src.modules.recommendations.app.recommendations_viewmodel import RecommendationsViewmodel
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.helpers.external_interfaces.http_codes import OK, Forbidden, InternalServerError

class RecommendationsController:

    def __init__(self, usecase: RecommendationsUsecase):
        self.usecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            user_id = request.data.get("user_id")

            if not user_id:
                raise EntityError("user_id is required")

            recommended_categories = self.usecase(user_id=user_id)

            viewmodel = RecommendationsViewmodel(recommended_categories)
            return OK({"message": "Success", "recommended_categories": viewmodel.to_dict()})

        except (EntityError, ForbiddenAction) as error:
            return Forbidden(body={"message": error.message})

        except Exception as error:
            return InternalServerError(body={"message": str(error)})
