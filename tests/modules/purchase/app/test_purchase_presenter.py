import json
import time
import pytest

from src.modules.purchase.app.purchase_presenter import lambda_handler

class Test_PurchasePresenter:
    def test_purchase_presenter(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/purchase",
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
                "product_id": "7aa45600-3e44-46ca-8064-aa90874288cf",
                "category": "CLOTHES",
                "price": 25.0,
                "purchase_date": int(time.time())
            }),
            "isBase64Encoded": False
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 201
        body = json.loads(response["body"])
        assert body["message"] == "the purchase has been created"
        assert body["purchase"]["user_id"] == "3c0c67a5-2dc4-4b90-be13-73b7d29718f0"
        assert body["purchase"]["product_id"] == "7aa45600-3e44-46ca-8064-aa90874288cf"
        assert body["purchase"]["category"] == "CLOTHES"
        assert body["purchase"]["price"] == 25.0
        assert isinstance(body["purchase"]["purchase_date"], int)

    def test_purchase_presenter_missing_field(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/purchase",
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
                "product_id": "7aa45600-3e44-46ca-8064-aa90874288cf",
                "category": "CLOTHES",
                "price": 25.0
                # Falta o campo "purchase_date"
            }),
            "isBase64Encoded": False
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 403  
