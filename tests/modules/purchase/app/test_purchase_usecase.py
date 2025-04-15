import pytest


from src.shared.domain.repositories.purchase_repository_mock import PurchaseRepositoryMock
from src.modules.purchase.app.purchase_usecase import PurchaseUsecase
from src.shared.domain.enums.category_enum import CATEGORY
from src.shared.helpers.errors.usecase_errors import DuplicatedItem

class Test_PurchaseUsecase:

    def test_create_purchase(self):
        repo = PurchaseRepositoryMock()
        usecase = PurchaseUsecase(repo)

        purchase = usecase(user_id="e52bbdb7-aaa9-49a8-89be-f4ffd4bdc930", product_id="832ddff6-b83e-4759-ba88-0f683ac70fa3", 
                       category=CATEGORY.CLOTHES, price= 27.0, purchase_date= 1744637400)

        assert repo.purchase_list[-1] == purchase