from os import environ
from typing import List

from fastapi import FastAPI, HTTPException
from gota.core.app import DynamoDBSettings, RecipeApp
from gota.core.errors import RecipeNotFoundError
from gota.core.models import Recipe
from mangum import Mangum

# this spins up the API
# root_path is usually present when deployed to aws/api gateway
app = FastAPI(root_path=environ.get("API_ROOT_PATH", ""))

_recipe_app = RecipeApp(
    is_sam_local=environ.get("AWS_SAM_LOCAL"),
    is_local=environ.get("APP_LOCAL"),
    dynamodb_settings=DynamoDBSettings(
        table_name=environ.get("DYNAMODB_TABLE_NAME"),
        partition_key=environ.get("DYNAMODB_PARTITION_KEY"),
        endpoint_url=environ.get("DYNAMODB_ENDPOINT_URL"),
    ),
)


# TODO: add filtering to support query by fields other than {recipe_id}
@app.get("/recipes", response_model=List[Recipe])
def get_recipes() -> List[Recipe]:
    return _recipe_app.repository.get_recipes()


@app.get("/recipes/{recipe_id}", response_model=Recipe)
def get_recipe(recipe_id: str) -> Recipe:
    try:
        return _recipe_app.repository.get_recipe(recipe_id)
    except RecipeNotFoundError:
        raise HTTPException(status_code=404)


# TODO: drop unknown fields from model
# Reason is the fact FastAPI doesn't do this validation
# See https://github.com/tiangolo/fastapi/pull/1297
@app.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: str, recipe: Recipe) -> None:
    try:
        return _recipe_app.repository.update_recipe(recipe_id, recipe)
    except RecipeNotFoundError:
        raise HTTPException(status_code=404)


# TODO: drop unknown fields from model
# Reason is the fact FastAPI doesn't do this validation
# See https://github.com/tiangolo/fastapi/pull/1297
@app.post("/recipes", response_model=Recipe, response_model_include={"recipe_id"})
def create_recipe(recipe: Recipe) -> Recipe:
    return _recipe_app.repository.save_recipe(recipe)


# this adapts the api to work in aws
handler = Mangum(app)
