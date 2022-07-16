from typing import NamedTuple, Tuple

from gota.core.repository import RecipeRepository
from gota.core.storage.dynamodb import DynamoDBStorage
from gota.core.storage.istorage import IStorage
from gota.core.storage.memory import MemoryStorage

DynamoDBSettings = NamedTuple(
    "DynamoDBSettings",
    [
        ("table_name", str),
        ("partition_key", str),
        ("endpoint_url", str),
    ],
)


class RecipeApp:
    """
    Handles initialization of the application, such as
    dynamodb client.
    """

    def __init__(
        self,
        is_sam_local: bool,
        is_local: bool,
        dynamodb_settings: DynamoDBSettings,
    ):
        self.repository: RecipeRepository = self._set_up_repository(
            is_sam_local=is_sam_local,
            is_local=is_local,
            dynamodb_table_name=dynamodb_settings.table_name,
            dynamodb_partition_key=dynamodb_settings.partition_key,
            dynamodb_endpoint_url=dynamodb_settings.endpoint_url,
        )

    @staticmethod
    def _set_up_repository(
        is_sam_local: bool,
        is_local: bool,
        dynamodb_table_name: str,
        dynamodb_partition_key: str,
        dynamodb_endpoint_url: str,
    ) -> Tuple[RecipeRepository]:
        storage: IStorage

        if is_sam_local:
            storage = DynamoDBStorage(
                table_name=dynamodb_table_name,
                partition_key=dynamodb_partition_key,
                endpoint_url=dynamodb_endpoint_url,
            )
        elif is_local:
            storage = MemoryStorage()
        else:
            storage = DynamoDBStorage(
                table_name=dynamodb_table_name, partition_key=dynamodb_partition_key
            )

        return RecipeRepository(storage)
