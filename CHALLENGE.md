# Challenge

Problem to resolve: Gota, an API for recipes.

## Requirements

1. [x] We want to create a (REST) API that can manage recipes that supports these operations:
    - Create a new recipe.
    - Retrieve a recipe.
    - Modify a recipe.
1. [] Also, we want a diagram and brief explanation of how this will run and be deployed on a Cloud Platform (e.g. AWS).
1. [] Optional: Add some kind of authentication (e.g. token).
1. [] Optional: Create a lightweight client to query the API.

## Deliverable

You should share with us a private Git repository that contains:

-   [x] A separated branch (not main) with the code of your solution and a Pull Request against the main branch so we can discuss your solution.
-   [x] Instructions on how to run your solution (README).
-   [] A document (in the format that you prefer) with the diagram and explanation of how to deploy and run your solution in the cloud.
-   [] You should give access to this repo to the following users (so they can review your solution on the Pull Request): adriantomas, - conor-mooney ,kabute, ruduran, rmunoz, sercantor
-   [] Optional: Provide a containerized solution (e.g. Dockerfile).

### Considerations

-   [x] Programming Languages: Python or Go are recommended.
-   [x] You can choose what Schema definitions and data structures to use.
-   [x] You can choose any storage/persistence that you consider.
-   [] Standard specifications (e.g. OpenAPI) are optional but encouraged.

### Recipe Format

The recipe format is open the whatever you consider but, please think about things such as:

-   [x] A recipe has a list of ingredients and ingredients have quantities (e.g. 50 gr of Olive Oil).
-   [x] A recipe has steps to follow.
