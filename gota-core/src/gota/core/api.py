import uuid
from typing import List

from fastapi import FastAPI, HTTPException
from gota.core.errors import RecipeNotFoundError
from gota.core.models import Recipe
from gota.core.repository import RecipeRepository
from gota.core.storage.memory import MemoryStorage
from mangum import Mangum

app = FastAPI()
storage = MemoryStorage()
repository = RecipeRepository(storage)


@app.get("/recipes", response_model=List[Recipe])
def get_recipes() -> List[Recipe]:
    return repository.get_recipes()


@app.get("/recipes/{recipe_id}", response_model=Recipe)
def get_recipe(recipe_id: uuid.UUID) -> Recipe:
    try:
        return repository.get_recipe(recipe_id)
    except RecipeNotFoundError:
        raise HTTPException(status_code=404)


@app.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: uuid.UUID, recipe: Recipe) -> None:
    try:
        return repository.update_recipe(recipe_id, recipe)
    except RecipeNotFoundError:
        raise HTTPException(status_code=404)


@app.post("/recipes", response_model=Recipe, response_model_include={"recipe_id"})
def create_recipe(recipe: Recipe) -> Recipe:
    return repository.save_recipe(recipe)


handler = Mangum(app)
