from typing import List, Union

from gota.core.storage.istorage import IStorage
from gota.core.storage.types import StorageItem, StorageItemID


class MemoryStorage(IStorage):
    """
    Dummy lightweight in-memory implementation of a storage to retrieve and save items using a Python dict.

    NOTE: This is a temporary storage being used during development-only. It will be replaced soon,
    before deploying the app to production.
    """

    def __init__(self):
        self._items = {}

    def get_items(self) -> List[StorageItem]:
        return [item for item in self._items.values()]

    def get_item(self, item_id: StorageItemID) -> Union[StorageItem, None]:
        return self._items.get(item_id)

    def save_item(self, item_id: StorageItemID, item: StorageItem) -> None:
        self._items[item_id] = item
