import json
import pytest
from src.modules.purchase_summary.app.purchase_summary_presenter import purchase_summary_presenter
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest

class TestPurchaseSummaryPresenter:
    def test_purchase_summary_presenter(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/purchase-summary",
            "headers": {},
            "requestContext": {
                "authorizer": {
                    "claims": {
                        "sub": "3c0c67a5-2dc4-4b90-be13-73b7d29718f0",
                        "name": "Lucas Milas",
                        "email": "milas@maua.br",
                        "custom:isMaua": True
                    }
                }
            },
            "body": json.dumps({
                "user_id": "3c0c67a5-2dc4-4b90-be13-73b7d29718f0",
                "start_date": 1744644600,
                "end_date": 1744659000,
            }),
            "isBase64Encoded": False
        }

        # Simula o contexto de execução
        context = None
        
        response = purchase_summary_presenter(event, context)

        # Verificações
        assert response["statusCode"] == 200
        body = json.loads(response["body"])
        assert body["message"] == "Success"
        assert "purchase_summary" in body
        assert isinstance(body["purchase_summary"], list)

    def test_purchase_summary_presenter_missing_user_id(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/purchase-summary",
            "headers": {},
            "requestContext": {
                "authorizer": {
                    "claims": {
                        "sub": "3c0c67a5-2dc4-4b90-be13-73b7d29718f0",
                        "name": "Lucas Milas",
                        "email": "milas@maua.br",
                        "custom:isMaua": True
                    }
                }
            },
            "body": json.dumps({
                "start_date": 1744644600,
                "end_date": 1744659000,
                # Falta o campo "user_id"
            }),
            "isBase64Encoded": False
        }

        context = None
        response = purchase_summary_presenter(event, context)
        
        assert response["statusCode"] == 400
        body = json.loads(response["body"])
        assert body == "Missing parameter: Field user_id is missing"

    def test_purchase_summary_presenter_missing_start_date(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/purchase-summary",
            "headers": {},
            "requestContext": {
                "authorizer": {
                    "claims": {
                        "sub": "3c0c67a5-2dc4-4b90-be13-73b7d29718f0",
                        "name": "Lucas Milas",
                        "email": "milas@maua.br",
                        "custom:isMaua": True
                    }
                }
            },
            "body": json.dumps({
                "user_id": "3c0c67a5-2dc4-4b90-be13-73b7d29718f0",
                "end_date": 1744659000,
                # Falta o campo "start_date"
            }),
            "isBase64Encoded": False
        }

        context = None
        response = purchase_summary_presenter(event, context)
        
        assert response["statusCode"] == 400
        body = json.loads(response["body"])
        assert body == "Missing parameter: Field start_date is missing"
