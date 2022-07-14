import uuid
from typing import Any, Dict, List, Optional
from uuid import UUID

from gota.core.enums import Ingredient, IngredientQuantityUnit, RecipeDificulty, RecipeTool
from pydantic import BaseModel


class _Model(BaseModel):
    name: str
    created_at_millis: Optional[int]
    updated_at_millis: Optional[int]


class _IngredientQuantity(BaseModel):
    value: int
    unit: Optional[IngredientQuantityUnit]


class _RecipeIngredient(BaseModel):
    ingredient: Ingredient
    preparation_kind: Optional[str]
    quantity: _IngredientQuantity


class _RecipeInstruction(BaseModel):
    description: str
    ingredients: Optional[List[Ingredient]]


class _RecipeServes(BaseModel):
    max: int
    min: int


class _RecipeDuration(BaseModel):
    cook_time_millis: int
    preparation_time_millis: int
    total_time_millis: Optional[int]


class _Recipe(_Model):
    recipe_id: Optional[UUID]
    dificulty: RecipeDificulty
    author: str
    calories: int
    description: str
    ingredients: List[_RecipeIngredient]
    instructions: List[_RecipeInstruction]
    notes: List[str]
    serves: _RecipeServes
    tools_needed: List[RecipeTool]
    duration: _RecipeDuration


RecipeID = uuid.UUID
Recipe = Dict[str, Any]
