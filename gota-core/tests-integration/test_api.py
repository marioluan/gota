import json
import random
import uuid

import requests


def test_get_recipes(api_url, headers):
    response = requests.get(api_url, headers=headers)
    response_body = json.loads(response.text)
    assert isinstance(response_body, list)


def test_create_recipe_successful(recipe, api_url, headers):
    response = requests.post(f"{api_url}", json=recipe, headers=headers)

    # TODO: assert body and headers
    assert response.status_code == 200


def test_create_recipe_missing_required_fields(recipe, api_url, headers):
    del recipe["duration"]
    response = requests.post(f"{api_url}", json=recipe, headers=headers)

    # TODO: assert body and headers
    assert response.status_code == 422


def test_get_recipe_successful(recipe, api_url, headers):
    # create recipe
    post_response = requests.post(f"{api_url}", json=recipe, headers=headers)
    post_recipe_id = json.loads(post_response.text)["recipe_id"]

    # get recipe
    get_response = requests.get(f"{api_url}/{post_recipe_id}", headers=headers)
    get_recipe_id = json.loads(get_response.text)["recipe_id"]

    # TODO: assert body and headers
    assert get_response.status_code == 200
    assert get_recipe_id == post_recipe_id


def test_get_recipe_not_found(recipe, api_url, headers):
    # create recipe
    requests.post(f"{api_url}", json=recipe, headers=headers)

    # attempt to get recipe
    recipe_id = str(uuid.uuid4())
    response = requests.get(f"{api_url}/{recipe_id}", headers=headers)

    # TODO: assert body and headers
    assert response.status_code == 404


def test_update_recipe_successful(recipe, api_url, headers):
    # create recipe
    post_response = requests.post(f"{api_url}", json=recipe, headers=headers)
    post_recipe_id = json.loads(post_response.text)["recipe_id"]

    post_duration_cook_time_millis = recipe["duration"]["cook_time_millis"]
    put_duration_cook_time_millis = random.randint(1, 10)
    recipe["duration"]["cook_time_millis"] = put_duration_cook_time_millis

    put_response = requests.put(f"{api_url}/{post_recipe_id}", json=recipe, headers=headers)

    # TODO: assert body and headers
    assert put_response.status_code == 200

    # get recipe
    get_response_after_put = requests.get(f"{api_url}/{post_recipe_id}", headers=headers)
    get_response_after_put_body = json.loads(get_response_after_put.text)
    current_duration_cook_time_millis = get_response_after_put_body["duration"]["cook_time_millis"]

    # TODO: assert body and headers
    assert get_response_after_put.status_code == 200
    # value from PUT is != from POST
    assert current_duration_cook_time_millis != post_duration_cook_time_millis
    # current is == from PUT
    assert current_duration_cook_time_millis == put_duration_cook_time_millis


def test_update_recipe_not_found(recipe, api_url, headers):
    # create recipe
    requests.post(f"{api_url}", json=recipe, headers=headers)

    # attempt to update recipe
    put_recipe_id = str(uuid.uuid4())
    put_response = requests.put(f"{api_url}/{put_recipe_id}", json=recipe, headers=headers)

    # TODO: assert body and headers
    assert put_response.status_code == 404
