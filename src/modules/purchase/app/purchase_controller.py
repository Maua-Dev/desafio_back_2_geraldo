from src.modules.purchase.app.purchase_usecase import PurchaseUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

class PurchaseController:

    def __init__(self, usecase: PurchaseUsecase):
        self.PurchaseUsecase = PurchaseUsecase

    def __call__()
        
