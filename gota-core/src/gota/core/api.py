import uuid
from typing import List

from fastapi import FastAPI, HTTPException
from gota.core.models import Recipe
from mangum import Mangum

app = FastAPI()


@app.get("/recipes", response_model=List[Recipe])
def get_recipes() -> List[Recipe]:
    return []


@app.get("/recipes/{recipe_id}", response_model=Recipe)
def get_recipe(recipe_id: uuid.UUID) -> Recipe:
    recipe = None
    if not recipe:
        raise HTTPException(status_code=404)
    return recipe


@app.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: uuid.UUID, recipe: Recipe) -> None:
    pass


@app.post("/recipes", response_model=Recipe, response_model_include={"recipe_id"})
def create_recipe(recipe: Recipe) -> Recipe:
    return {"recipe_id": uuid.uuid4()}


handler = Mangum(app)
