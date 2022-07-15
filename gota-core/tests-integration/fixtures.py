# TODO: split recipe fixture into individual models, such as ingredients, instructions, etc.

recipe = {
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
