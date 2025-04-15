import abc
import re

from src.shared.domain.enums.category_enum import CATEGORY
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, NoItemsFound

class Purchase(abc.ABC):
    user_id: str
    product_id: str
    category: str
    price: float
    purchase_date: int

    def __init__(self, user_id: str, product_id: str, category: CATEGORY, price: float, purchase_date: int):

        if not isinstance(user_id, str):
            raise EntityError("user_id")
        self.user_id = user_id

        if not isinstance(product_id, str):
            raise EntityError("product_id")
        self.product_id = product_id

        if not isinstance(category, CATEGORY):
            raise EntityError("category")
        self.category = category

        if not isinstance(price, float):
            raise EntityError("price")
        if price <= 0:
            raise ForbiddenAction("Price can't be 0 or lower")
        self.price = price

        if not isinstance(purchase_date, int):
            raise EntityError("purchase_date")
        if purchase_date <= 0:
            raise EntityError("Purchase_date can't be 0 or lower")
        self.purchase_date = purchase_date


