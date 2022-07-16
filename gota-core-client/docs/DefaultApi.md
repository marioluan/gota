# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_recipe_recipes_post**](DefaultApi.md#create_recipe_recipes_post) | **POST** /recipes | Create Recipe
[**get_recipe_recipes_recipe_id_get**](DefaultApi.md#get_recipe_recipes_recipe_id_get) | **GET** /recipes/{recipe_id} | Get Recipe
[**get_recipes_recipes_get**](DefaultApi.md#get_recipes_recipes_get) | **GET** /recipes | Get Recipes
[**update_recipe_recipes_recipe_id_put**](DefaultApi.md#update_recipe_recipes_recipe_id_put) | **PUT** /recipes/{recipe_id} | Update Recipe


# **create_recipe_recipes_post**
> Recipe create_recipe_recipes_post(recipe)

Create Recipe

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.recipe import Recipe
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    recipe = Recipe(
        name="name_example",
        created_at_millis=1,
        updated_at_millis=1,
        recipe_id="recipe_id_example",
        dificulty=RecipeDificulty("EASY"),
        author="author_example",
        calories=1,
        description="description_example",
        ingredients=[
            RecipeIngredient(
                ingredient=Ingredient("FRESH_THYME"),
                preparation_kind="preparation_kind_example",
                quantity=IngredientQuantity(
                    value=1,
                    unit=IngredientQuantityUnit("KG"),
                ),
            ),
        ],
        instructions=[
            RecipeInstruction(
                description="description_example",
                ingredients=[
                    Ingredient("FRESH_THYME"),
                ],
            ),
        ],
        notes=[
            "notes_example",
        ],
        serves=RecipeServes(
            max=1,
            min=1,
        ),
        tools_needed=[
            RecipeTool("INSTANT_POT"),
        ],
        duration=RecipeDuration(
            cook_time_millis=1,
            preparation_time_millis=1,
            total_time_millis=1,
        ),
    ) # Recipe | 

    # example passing only required values which don't have defaults set
    try:
        # Create Recipe
        api_response = api_instance.create_recipe_recipes_post(recipe)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_recipe_recipes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipe** | [**Recipe**](Recipe.md)|  |

### Return type

[**Recipe**](Recipe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recipe_recipes_recipe_id_get**
> Recipe get_recipe_recipes_recipe_id_get(recipe_id)

Get Recipe

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.recipe import Recipe
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    recipe_id = "recipe_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Recipe
        api_response = api_instance.get_recipe_recipes_recipe_id_get(recipe_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_recipe_recipes_recipe_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipe_id** | **str**|  |

### Return type

[**Recipe**](Recipe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recipes_recipes_get**
> [Recipe] get_recipes_recipes_get()

Get Recipes

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.recipe import Recipe
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Recipes
        api_response = api_instance.get_recipes_recipes_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_recipes_recipes_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Recipe]**](Recipe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recipe_recipes_recipe_id_put**
> bool, date, datetime, dict, float, int, list, str, none_type update_recipe_recipes_recipe_id_put(recipe_id, recipe)

Update Recipe

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.recipe import Recipe
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    recipe_id = "recipe_id_example" # str | 
    recipe = Recipe(
        name="name_example",
        created_at_millis=1,
        updated_at_millis=1,
        recipe_id="recipe_id_example",
        dificulty=RecipeDificulty("EASY"),
        author="author_example",
        calories=1,
        description="description_example",
        ingredients=[
            RecipeIngredient(
                ingredient=Ingredient("FRESH_THYME"),
                preparation_kind="preparation_kind_example",
                quantity=IngredientQuantity(
                    value=1,
                    unit=IngredientQuantityUnit("KG"),
                ),
            ),
        ],
        instructions=[
            RecipeInstruction(
                description="description_example",
                ingredients=[
                    Ingredient("FRESH_THYME"),
                ],
            ),
        ],
        notes=[
            "notes_example",
        ],
        serves=RecipeServes(
            max=1,
            min=1,
        ),
        tools_needed=[
            RecipeTool("INSTANT_POT"),
        ],
        duration=RecipeDuration(
            cook_time_millis=1,
            preparation_time_millis=1,
            total_time_millis=1,
        ),
    ) # Recipe | 

    # example passing only required values which don't have defaults set
    try:
        # Update Recipe
        api_response = api_instance.update_recipe_recipes_recipe_id_put(recipe_id, recipe)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_recipe_recipes_recipe_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipe_id** | **str**|  |
 **recipe** | [**Recipe**](Recipe.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

