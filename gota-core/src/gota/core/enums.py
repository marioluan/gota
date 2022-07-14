from enum import Enum


class Ingredient(str, Enum):
    FRESH_THYME = "FRESH_THYME"
    GARLIC_CLOVE = "GARLIC_CLOVE"


class IngredientQuantityUnit(str, Enum):
    KG = "KG"
    G = "G"


class RecipeDificulty(str, Enum):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"


class RecipeTool(str, Enum):
    INSTANT_POT = "INSTANT_POT"
    INNER_POT = "INNER_POT"
