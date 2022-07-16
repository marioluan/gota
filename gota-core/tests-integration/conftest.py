from os import environ

from pytest import fixture
from warrant import Cognito

# TODO: split recipe fixture into individual models, such as ingredients, instructions, etc.


def _get_auth_token_id():
    """
    Retrieve a token from Cognito to be used to authenticate with api gateway.
    """
    auth = Cognito(
        user_pool_id=environ["AUTH_USER_POOL_ID"],
        client_id=environ["AUTH_CLIENT_ID"],
        username=environ["AUTH_USERNAME"],
        user_pool_region=environ["AUTH_USER_POOL_REGION"],
    )
    auth.authenticate(password=environ["AUTH_PASSWORD"])

    return auth.id_token


@fixture
def recipe():
    return {
        "name": "Paprika Chicken and Spinach with White Wine Butter Thyme Sauce",
        "dificulty": "EASY",
        "author": "Mary",
        "calories": 1,
        "description": "This quick, easy, chicken dinner is bathed in a flavorful garlic, thyme, butter and white wine sauce. This is sure to impress, and only takes 30 minutes!",
        "ingredients": [
            {
                "ingredient": "FRESH_THYME",
                "preparation_kind": "destalked",
                "quantity": {"value": 10, "unit": "G"},
            },
            {
                "ingredient": "GARLIC_CLOVE",
                "preparation_kind": "destalked",
                "quantity": {"value": 3, "unit": "KG"},
            },
        ],
        "instructions": [
            {
                "description": "Cook, stirring the thyme, for about 2 minutes before adding the wine.",
                "ingredients": ["FRESH_THYME"],
            },
            {"description": "Add garlic.", "ingredients": ["GARLIC_CLOVE"]},
        ],
        "notes": [
            "*You could use olive oil in place of some or all of the butter here. I’ve done this dish using about 1/2 and 1/2."
        ],
        "serves": {"min": 2, "max": 4},
        "thumbnail": "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/chorizo-mozarella-gnocchi-bake-cropped-9ab73a3.jpg?quality=90&resize=768,574",
        "tools_needed": ["INSTANT_POT", "INNER_POT"],
        "duration": {"cook_time_millis": 300000, "preparation_time_millis": 300000},
    }


@fixture
def api_url():
    return environ["API_URL"] + "/recipes"


@fixture
def stage():
    return environ["API_STAGE"]


@fixture
def headers(stage):
    if stage.lower() == "prod":
        return {"Authorization": _get_auth_token_id()}
    return {}
