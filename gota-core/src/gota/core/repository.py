import uuid
from typing import List, Union

import arrow
from gota.core.errors import RecipeNotFoundError
from gota.core.models import Recipe, RecipeID
from gota.core.storage.istorage import IStorage
from gota.core.time_converter import datetime_to_milliseconds


class RecipeRepository:
    def __init__(self, storage: IStorage):
        self._storage = storage

    @staticmethod
    def _update_duration_total_time_millis(recipe: Recipe) -> None:
        recipe.duration.total_time_millis = (
            recipe.duration.cook_time_millis + recipe.duration.preparation_time_millis
        )

    def get_recipes(self) -> List[Recipe]:
        """
        Get all recipes from the repository.

        :return: all recipes from repository
        """
        return [Recipe(**item) for item in self._storage.get_items()]

    def get_recipe(self, recipe_id: RecipeID) -> Union[Recipe, RecipeNotFoundError]:
        """
        Get the recipe with recipe_id from the repository.

        :param recipe_id: the unique identifier of the recipe
        :raises RecipeNotFoundError: if recipe wasn't found
        :return: the recipe found
        """
        item = self._storage.get_item(recipe_id)
        if not item:
            raise RecipeNotFoundError()
        return Recipe(**item)

    def save_recipe(self, recipe: Recipe) -> Recipe:
        """
        Save the recipe in the repository.

        :param recipe: the recipe
        :return: the saved recipe (with auto-generated fields)
        """
        # auto-generated
        recipe.recipe_id = str(uuid.uuid4())
        recipe.created_at_millis = datetime_to_milliseconds(arrow.utcnow())
        self._update_duration_total_time_millis(recipe)

        self._storage.save_item(item_id=recipe.recipe_id, item=recipe.dict())

        return recipe

    def update_recipe(
        self, recipe_id: RecipeID, recipe: Recipe
    ) -> Union[None, RecipeNotFoundError]:
        """
        Update the recipe with the given recipe_id in the repository.

        :param recipe_id: the unique identifier of the recipe to be updated
        :param recipe: the recipe to be saved in the repository
        :raises RecipeNotFoundError: if the recipe isn't present in the repository
        :return: void
        """
        existing_recipe = self.get_recipe(recipe_id=recipe_id)

        # these fields are optional, but once set, we enforce immutability here
        recipe.recipe_id = existing_recipe.recipe_id
        recipe.created_at_millis = existing_recipe.created_at_millis

        # auto-generated
        recipe.updated_at_millis = datetime_to_milliseconds(arrow.utcnow())
        self._update_duration_total_time_millis(recipe)

        self._storage.save_item(item_id=recipe_id, item=recipe.dict())

        return None
