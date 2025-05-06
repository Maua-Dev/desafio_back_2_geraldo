from decimal import Decimal
from typing import Dict, List, Optional

from src.shared.domain.entities.purchase import Purchase
from src.shared.domain.entities.challenge import Challenge
from src.shared.domain.repositories.challenge_repository_interface import IChallengeRepository
from src.shared.environments import Environments
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.dto.challenge_dynamo_dto import ChallengeDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class ChallengeRepositoryDynamo(IChallengeRepository):

    @staticmethod
    def partition_key_format(user_id: str) -> str:
        return f"user#{user_id}"
    

    @staticmethod
    def sort_key_format(timestamp: int) -> str:
        return f"purchase#{timestamp}"

    def __init__(self):
        self.dynamo = DynamoDatasource(
            endpoint_url=Environments.get_envs().endpoint_url,
            dynamo_table_name=Environments.get_envs().dynamo_table_name,
            region=Environments.get_envs().region,
            partition_key=Environments.get_envs().dynamo_partition_key,
            sort_key=Environments.get_envs().dynamo_sort_key,
        )

    
    def create_purchase(self, new_purchase: Purchase) -> Purchase:
        purchase_dto = ChallengeDynamoDTO.from_entity(purchase=new_purchase)
        item = purchase_dto.to_dynamo()

        item[self.dynamo.partition_key] = self.partition_key_format(
            new_purchase.user_id)
        item[self.dynamo.sort_key] = self.sort_key_format(
            new_purchase.purchase_date)

        resp = self.dynamo.put_item(partition_key=self.partition_key_format(new_purchase.user_id),
                                    sort_key=self.sort_key_format(new_purchase.purchase_date), item=item,
                                    is_decimal=True)

        return new_purchase

    def get_category_from_user_id(self, user_id: str) -> Optional[List[str]]:
        response = self.dynamo.dynamo_table.query(
            partition_key=self.partition_key_format(user_id),
        )

        if 'Items' not in response:
            raise NoItemsFound("No items found for this user_id")

        categories = []

        try:
            for item in response["Items"]:
                if self.dynamo.partition_key in item and item[self.dynamo.partition_key] == self.partition_key_format(user_id):
                    if self.dynamo.sort_key in item and 'purchase#' in item[self.dynamo.sort_key]:
                        dto = ChallengeDynamoDTO.from_dynamo(product_data=item)
                        categories.append(dto.category)

            if not categories:
                raise NoItemsFound("No items found for this user_id")

            return categories

        except BaseException as err:
            print(err)
            return None

    def get_purchase_from_user_id_and_interval(self, user_id: str, start_date: int, end_date: int) -> Optional[Dict]:
        response = self.dynamo.dynamo_table.query(
            partition_key=self.partition_key_format(user_id),
            sort_key_start=self.sort_key_format(start_date),
            sort_key_end=self.sort_key_format(end_date)
        )

        if 'Items' not in response:
            raise NoItemsFound("No items found for this user_id")

        purchases = []

        try:
            for item in response['Items']:
                if 'purchase#' in item[self.dynamo.sort_key]:
                    dto = ChallengeDynamoDTO.from_dynamo(product_data=item)
                    purchases.append(dto.to_entity())

            return {
                "user_id": user_id,
                "purchases": purchases
            }
        except BaseException as err:
            print(f"Error while parsing items: {err}")
            return None

