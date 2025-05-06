from decimal import Decimal
from typing import Optional

from src.shared.domain.entities.purchase import Purchase


class ChallengeDynamoDTO:
    user_id: str
    product_id: str
    category: str
    price: float
    purchase_date: int

    def __init__(self, user_id: str, product_id: str, category: str, price: float, purchase_date: int):
        self.user_id = user_id
        self.product_id = product_id
        self.category = category
        self.price = price
        self.purchase_date = purchase_date

    @staticmethod
    def from_entity(purchase: Purchase) -> "ChallengeDynamoDTO":
        """
        Parse data from Purchase to ChallengeDynamoDTO
        """
        return ChallengeDynamoDTO(
            user_id=purchase.user_id,
            product_id=purchase.product_id,
            category=purchase.category,
            price=purchase.price,
            purchase_date=purchase.purchase_date,
        )

    def to_dynamo(self) -> dict:
        """
        Parse data from ChallengeDynamoDTO to dict
        """
        data = {
            "user_id": self.user_id,
            "product_id": self.product_id,
            "category": self.category,
            "price": Decimal(self.price),
            "purchase_date": Decimal(self.purchase_date),
        }
    
        data_without_none_values = {k: v for k, v in data.items() if v is not None}
         
        return data_without_none_values

    @staticmethod
    def from_dynamo(product_data: dict) -> "ChallengeDynamoDTO":
        """
        Parse data from DynamoDB to ChallengeDynamoDTO
        @param product_data: dict from DynamoDB
        """
        return ChallengeDynamoDTO(
            user_id=product_data.get("user_id"),
            product_id=product_data.get("product_id"),
            category=product_data.get("category"),
            price=float(product_data.get("price", 0)),
            purchase_date=int(product_data.get("purchase_date", 0)),
        )

    def to_entity(self) -> Purchase:
        """
        Parse data from UserDynamoDTO to Product
        """
        return Purchase(
            user_id=self.user_id,
            product_id=self.product_id,
            category=self.category,
            price=self.price,
            purchase_date=self.purchase_date,
        )

    def __repr__(self):
        return f"ChallengeDynamoDTO(user_id={self.user_id}, product_id={self.product_id}, category={self.category}, price={self.price}, purchase_date={self.purchase_date})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    