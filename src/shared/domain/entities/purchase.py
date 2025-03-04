import abc
import re

from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError


class Purchase(abc.ABC):
    user_id: str
    product_id: str
    category: str
    price: float
    purchase_date: int
    pass
