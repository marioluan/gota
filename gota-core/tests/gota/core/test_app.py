import pytest


def test_importable():
    from src.gota.core.app import RecipeApp  # noqa


@pytest.mark.skip(
    "Integration tests are giving me enough confidence this is working. I will implement this if times allow."
)
def test_new_recipe_app():
    pass


@pytest.mark.skip(
    "Integration tests are giving me enough confidence this is working. I will implement this if times allow."
)
@pytest.mark.skip
def test__set_up_repository():
    pass
