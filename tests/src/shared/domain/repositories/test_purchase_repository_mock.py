import pytest

from src.shared.domain.entities.purchase import Purchase
from src.shared.domain.enums.category_enum import CATEGORY
from src.shared.domain.repositories.purchase_repository_mock import PurchaseRepositoryMock
from src.shared.helpers.errors.domain_errors import EntityError

class Test_purchase_repository_mock:

    def test_create_purchase(self):
        repo = PurchaseRepositoryMock()

        purchase = Purchase(user_id="e52bbdb7-aaa9-49a8-89be-f4ffd4bdc930", product_id="832ddff6-b83e-4759-ba88-0f683ac70fa3", 
                       category=CATEGORY.CLOTHES, price= 27.0, purchase_date= 1744637400)
        result = repo.create_purchase(purchase)

        assert repo.purchase_list[-1] == purchase

    def test_get_category_from_user_id(self):
        repo = PurchaseRepositoryMock()

        result = repo.get_category_from_user_id("3c0c67a5-2dc4-4b90-be13-73b7d29718f0")

        assert result == ["CLOTHES"]

    def test_get_category_from_user_id_none(self):
        repo = PurchaseRepositoryMock()

        with pytest.raises(EntityError):
            repo.get_category_from_user_id("3cc67a5-2dc4-4b90-be13-73b7d29718f0")
        


    def test_get_purchase_from_user_id_and_interval(self):
        repo = PurchaseRepositoryMock()

        result = repo.get_purchase_from_user_id_and_interval("3c0c67a5-2dc4-4b90-be13-73b7d29718f0", 0, 2000000000000)

        assert result == ["CLOTHES"]

    def test_get_purchase_from_user_id_and_interval_none(self):
        repo = PurchaseRepositoryMock()

        result = repo.get_purchase_from_user_id_and_interval("3c0c67a5-2dc4-4b90-be13-73b7d29718f0", 3000000000000, 2000000000000)

        assert result == None

