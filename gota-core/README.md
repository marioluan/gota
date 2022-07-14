# gota-core

Core library which handles api requests to create, read and update recipes.

## Development

**Pre-requisite**

-   package manager: pip
-   runtime: python3
-   test runner: pytest
-   web server: uvicorn

### Environment setup

1. Create a virtualenv:
    ```bash
    python3 -m venv env
    . env/bin/activate
    ```
1. Upgrade pip and setuptools:
    ```bash
    python -m pip install --upgrade pip setuptools
    ```
1. Install dependencies and goto-core in editable mode:
    ```bash
    pip install -r requirements.txt && pip install -e .
    ```

### Testing

```bash
pytest
```

## Run a standalone API

1. Start the web server:
    ```bash
    uvicorn gota.core.api:app --reload
    ```
1. Interact with it: http://127.0.0.1:8000/recipes
