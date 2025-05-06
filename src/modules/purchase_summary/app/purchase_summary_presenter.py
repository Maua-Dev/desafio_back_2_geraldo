from src.modules.purchase.app.purchase_controller import PurchaseController

from src.modules.purchase_summary.app.purchase_summary_controller import PurchaseSummaryController
from src.modules.purchase_summary.app.purchase_summary_usecase import PurchaseSummaryUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_purchase = Environments.get_purchase_repo()()
usecase = PurchaseSummaryUsecase(repo=repo_purchase)
controller = PurchaseSummaryController(usecase)

def purchase_summary_presenter(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    if response.status_code == 200:
        response.body = {
            "message": "Success",
            "purchase_summary": response.body.get("data", {}).get("purchase_summary", [])
        }

    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

def lambda_handler(event, context):
    
    response = purchase_summary_presenter(event, context)
   
    return response

