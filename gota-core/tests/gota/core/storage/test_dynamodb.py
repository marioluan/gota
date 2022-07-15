import pytest


def test_importable():
    from src.gota.core.storage import dynamodb  # noqa


@pytest.mark.skip(
    "Integration tests are giving me enough confidence this is working. I will implement this if times allow."
)
@pytest.mark.skip
def get_items():
    pass


@pytest.mark.skip(
    "Integration tests are giving me enough confidence this is working. I will implement this if times allow."
)
@pytest.mark.skip
def get_item():
    pass


@pytest.mark.skip(
    "Integration tests are giving me enough confidence this is working. I will implement this if times allow."
)
@pytest.mark.skip
def save_item():
    pass
