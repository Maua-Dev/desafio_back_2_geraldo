import pytest

from src.shared.domain.enums.category_enum import CATEGORY
from src.shared.domain.repositories.purchase_repository_mock import PurchaseRepositoryMock

class Test_purchase_repository_mock:

    def test_get_category_from_user_id(self):
        repo = PurchaseRepositoryMock()

        result = repo.get_category_from_user_id("3c0c67a5-2dc4-4b90-be13-73b7d29718f0")

        assert result == ["CLOTHES"]

    def test_get_category_from_user_id_none(self):
        repo = PurchaseRepositoryMock()

        result = repo.get_category_from_user_id("3cc67a5-2dc4-4b90-be13-73b7d29718f0")

        assert result == None

    def test_get_purchase_from_user_id_and_interval(self):
        repo = PurchaseRepositoryMock()

        result = repo.get_purchase_from_user_id_and_interval("3c0c67a5-2dc4-4b90-be13-73b7d29718f0", 0, 2000000000000)

        assert result == ["CLOTHES"]

    def test_get_purchase_from_user_id_and_interval_none(self):
        repo = PurchaseRepositoryMock()

        result = repo.get_purchase_from_user_id_and_interval("3c0c67a5-2dc4-4b90-be13-73b7d29718f0", 3000000000000, 2000000000000)

        assert result == None

