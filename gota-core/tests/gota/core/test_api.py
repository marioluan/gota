import pytest


def test_importable():
    from src.gota.core.api import app  # noqa


@pytest.mark.skip(
    "Integration tests are giving me enough confidence this is working. I will implement this if times allow."
)
def test_recipes():
    pass


@pytest.mark.skip(
    "Integration tests are giving me enough confidence this is working. I will implement this if times allow."
)
@pytest.mark.skip
def test_get_recipe():
    pass


@pytest.mark.skip(
    "Integration tests are giving me enough confidence this is working. I will implement this if times allow."
)
@pytest.mark.skip
def test_update_recipe():
    pass


@pytest.mark.skip(
    "Integration tests are giving me enough confidence this is working. I will implement this if times allow."
)
@pytest.mark.skip
def test_create_recipe():
    pass
