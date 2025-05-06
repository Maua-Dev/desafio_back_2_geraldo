import pytest

from src.modules.purchase_summary.app.purchase_summary_viewmodel import PurchaseSummaryViewmodel


class TestPurchaseSummaryViewmodel:

    def test_to_dict(self):
        user_id = "user-123"
        start_date = 1744644600
        end_date = 1744659000
        total_spent = 250.0
        total_purchases = 4
        category_breakdown = {
            "CLOTHES": {"amount_spent": 150.0, "count": 3},
            "ELECTRONIC": {"amount_spent": 100.0, "count": 1}
        }

        viewmodel = PurchaseSummaryViewmodel(
            user_id=user_id,
            start_date=start_date,
            end_date=end_date,
            total_spent=total_spent,
            total_purchases=total_purchases,
            category_breakdown=category_breakdown
        )

        expected = {
            "purchase_summary": {
                "user_id": user_id,
                "start_date": start_date,
                "end_date": end_date,
                "total_spent": total_spent,
                "total_purchases": total_purchases,
                "category_breakdown": category_breakdown
            },
            "message": "The purchase summary has been created"
        }

        assert viewmodel.to_dict() == expected
