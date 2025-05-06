import json
import time
import pytest

from src.modules.recommendations.app.recommendations_presenter import lambda_handler

class Test_RecommendationsPresenter:
    def test_recommendations_presenter(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/recommendations",
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
                "preferences": ["CLOTHES", "ELECTRONICS"],
            }),
            "isBase64Encoded": False
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 200  
        body = json.loads(response["body"])
        assert body["message"] == "Success"  
        assert isinstance(body["recommended_categories"], list)  

    def test_recommendations_presenter_missing_field(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/recommendations",
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
                "preferences": ["CLOTHES", "ELECTRONICS"],
                # Falta o campo "user_id"
            }),
            "isBase64Encoded": False
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 403  

