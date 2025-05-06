import pytest

from src.modules.recommendations.app.recommendations_viewmodel import RecommendationsViewmodel

class Test_RecommendationsViewmodel:

    def test_recommendations_viewmodel_to_dict(self):
        recommended_categories = ["CLOTHES", "FOOD"]
        viewmodel = RecommendationsViewmodel(recommended_categories=recommended_categories)

        expected = {
            "recommended_categories": ["CLOTHES", "FOOD"]
        }

        assert viewmodel.to_dict() == expected
