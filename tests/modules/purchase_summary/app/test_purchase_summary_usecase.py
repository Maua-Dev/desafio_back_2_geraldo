import pytest

from src.modules.purchase_summary.app.purchase_summary_usecase import PurchaseSummaryUsecase
from src.shared.domain.enums.category_enum import CATEGORY
from src.shared.domain.repositories.purchase_repository_mock import PurchaseRepositoryMock

class TestPurchaseSummaryUsecase:

    def test_purchase_summary(self):
        
        repo_mock = PurchaseRepositoryMock()
        usecase = PurchaseSummaryUsecase(repo=repo_mock)

        user_id = "3c0c67a5-2dc4-4b90-be13-73b7d29718f0"
        start_date = 1744644600
        end_date = 1744659000
        
        result = usecase(user_id, start_date, end_date)
        
        # Verificando se o resultado é como esperado
        assert result["user_id"] == user_id
        assert result["total_spent"] == 250.0  # 25.0 + 50.0 + 75.0 + 100.0
        assert result["total_purchases"] == 4  # 4 compras
        assert result["category_breakdown"] == {
            CATEGORY.CLOTHES.value: {"amount_spent": 150.0, "count": 3},
            CATEGORY.ELECTRONIC.value: {"amount_spent": 100.0, "count": 1}
        }
    
    def test_purchase_summary_empty(self):

        repo_mock = PurchaseRepositoryMock()
        usecase = PurchaseSummaryUsecase(repo=repo_mock)

        user_id = "3c0c67a5-2dc4-4b90-be13-73b7d29718f0"
        start_date = 1744662600  
        end_date = 1744749000    
        
        result = usecase(user_id, start_date, end_date)
        

        assert result["user_id"] == user_id
        assert result["total_spent"] == 0.0
        assert result["total_purchases"] == 0
        assert result["category_breakdown"] == {}
