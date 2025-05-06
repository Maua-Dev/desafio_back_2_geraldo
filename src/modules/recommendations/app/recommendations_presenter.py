from src.modules.purchase.app.purchase_controller import PurchaseController

from src.modules.recommendations.app.recommendations_controller import RecommendationsController
from src.modules.recommendations.app.recommendations_usecase import RecommendationsUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_purchase = Environments.get_purchase_repo()()
usecase = RecommendationsUsecase(repo=repo_purchase)
controller = RecommendationsController(usecase)

def recommendations_presenter(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    if response.status_code == 200:
        response.body = {
            "message": "Success",
            "recommended_categories": response.body.get("data", {}).get("recommended_categories", [])
        }

    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

def lambda_handler(event, context):
    
    response = recommendations_presenter(event, context)
   
    return response

