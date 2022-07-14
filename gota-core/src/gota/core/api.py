import uuid
from typing import Dict, List

from fastapi import FastAPI, HTTPException
from gota.core.models import Recipe, RecipeID
from mangum import Mangum

app = FastAPI()


@app.get("/recipes")
def get_recipes() -> List[Recipe]:
    return []


@app.get("/recipes/{recipe_id}")
def get_recipe(recipe_id: uuid.UUID) -> Recipe:
    recipe = None
    if not recipe:
        raise HTTPException(status_code=404)
    return recipe


@app.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: uuid.UUID, recipe: Recipe) -> None:
    pass


@app.post("/recipes")
def create_recipe(recipe: Recipe) -> Dict[str, RecipeID]:
    return {"recipe_id": uuid.uuid4()}


handler = Mangum(app)
