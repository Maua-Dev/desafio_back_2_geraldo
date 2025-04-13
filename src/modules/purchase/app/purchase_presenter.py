from src.modules.purchase.app.purchase_controller import purchase_controller
from src.modules.purchase.app.purchase_usecase import purchase_usecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_user = Environments.get_user_repo()()
repo_schedule = Environments.get_order_repo()()
usecase = purchase_usecase(repo_schedule=repo_schedule, repo_user=repo_user)
controller = purchase_controller(usecase)

def purchase_presenter(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

def lambda_handler(event, context):
    
    response = purchase_presenter(event, context)
   
    return response

