import copy
import json
import random
import uuid

import requests
from pytest import fixture

from fixtures import recipe

# TODO: spin up the server, run tests and shutdown programatically
# TODO: set address, port and root path dynamically.

_PORT = 8000
_API_URL = f"http://localhost:{_PORT}/recipes"


@fixture
def recipe_copy():
    # this is necessary to prevent test cases from mutating and sharing the same fixture
    return copy.deepcopy(recipe)


def test_create_recipe_successful(recipe_copy):
    response = requests.post(_API_URL, json=recipe_copy)

    # TODO: assert body and headers
    assert response.status_code == 200


def test_create_recipe_missing_required_fields(recipe_copy):
    del recipe_copy["duration"]
    response = requests.post(_API_URL, json=recipe_copy)

    # TODO: assert body and headers
    assert response.status_code == 422


def test_get_recipe_successful(recipe_copy):
    # create recipe
    post_response = requests.post(_API_URL, json=recipe_copy)
    post_recipe_id = json.loads(post_response.text)["recipe_id"]

    # get recipe
    get_response = requests.get(f"{_API_URL}/{post_recipe_id}")
    get_recipe_id = json.loads(get_response.text)["recipe_id"]

    # TODO: assert body and headers
    assert get_response.status_code == 200
    assert get_recipe_id == post_recipe_id


def test_get_recipe_not_found(recipe_copy):
    # create recipe
    requests.post(_API_URL, json=recipe_copy)

    # attempt to get recipe
    recipe_id = uuid.uuid4()
    response = requests.get(f"{_API_URL}/{recipe_id}")

    # TODO: assert body and headers
    assert response.status_code == 404


def test_update_recipe_successful(recipe_copy):
    # create recipe
    post_response = requests.post(_API_URL, json=recipe_copy)
    post_recipe_id = json.loads(post_response.text)["recipe_id"]

    post_duration_cook_time_millis = recipe_copy["duration"]["cook_time_millis"]
    put_duration_cook_time_millis = random.randint(1, 10)
    recipe_copy["duration"]["cook_time_millis"] = put_duration_cook_time_millis

    put_response = requests.put(f"{_API_URL}/{post_recipe_id}", json=recipe_copy)

    # TODO: assert body and headers
    assert put_response.status_code == 200

    # get recipe
    get_response_after_put = requests.get(f"{_API_URL}/{post_recipe_id}")
    get_response_after_put_body = json.loads(get_response_after_put.text)
    current_duration_cook_time_millis = get_response_after_put_body["duration"]["cook_time_millis"]

    # TODO: assert body and headers
    assert get_response_after_put.status_code == 200
    # value from PUT is != from POST
    assert current_duration_cook_time_millis != post_duration_cook_time_millis
    # current is == from PUT
    assert current_duration_cook_time_millis == put_duration_cook_time_millis


def test_update_recipe_not_found(recipe_copy):
    # create recipe
    requests.post(_API_URL, json=recipe_copy)

    # attempt to update recipe
    put_recipe_id = uuid.uuid4()
    put_response = requests.put(f"{_API_URL}/{put_recipe_id}", json=recipe_copy)

    # TODO: assert body and headers
    assert put_response.status_code == 404
