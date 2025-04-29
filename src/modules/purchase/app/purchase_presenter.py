from src.modules.purchase.app.purchase_controller import PurchaseController
from src.modules.purchase.app.purchase_usecase import PurchaseUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_purchase = Environments.get_purchase_repo()()
usecase = PurchaseUsecase(repo=repo_purchase)
controller = PurchaseController(usecase)

def purchase_presenter(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

def lambda_handler(event, context):
    
    response = purchase_presenter(event, context)
   
    return response

