import uuid

from pytest import fixture

from src.gota.core.storage.istorage import IStorage
from src.gota.core.storage.memory import MemoryStorage
from src.gota.core.storage.types import StorageItem, StorageItemID


@fixture
def item_id() -> StorageItemID:
    return str(uuid.uuid4())


@fixture
def item() -> StorageItem:
    return {"key": "value"}


@fixture
def storage() -> MemoryStorage:
    return MemoryStorage()


def test_save_item_when_existing(storage: IStorage, item_id: StorageItemID, item: StorageItem):
    storage.save_item(item_id=item_id, item=item)
    storage.save_item(item_id=item_id, item=item)

    assert storage.get_items() == [item]


def test_save_item_when_new(storage: IStorage, item_id: StorageItemID, item: StorageItem):
    storage.save_item(item_id=item_id, item=item)

    assert storage.get_items() == [item]


def test_get_items_when_empty(storage: IStorage):
    assert storage.get_items() == []


def test_get_items_when_non_empty(storage: IStorage, item_id: StorageItemID, item: StorageItem):
    storage.save_item(item_id=item_id, item=item)
    assert len(storage.get_items()) == 1


def test_get_item_when_present(storage: IStorage, item_id: StorageItemID, item: StorageItem):
    storage.save_item(item_id=item_id, item=item)
    assert storage.get_item(item_id=item_id) == item


def test_get_item_when_absent(storage: IStorage, item_id: StorageItemID, item: StorageItem):
    storage.save_item(item_id=item_id, item=item)
    assert storage.get_item(item_id=str(uuid.uuid4())) != item
