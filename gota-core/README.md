# gota-core

Core library which implements an API to create, read and update recipes.

## Deployment mode: ASGI Web Server

The API is powered by [FastAPI](https://github.com/tiangolo/fastapi) and backed by [uvicorn ASGI web server](https://www.uvicorn.org/).

## Development

The steps below should help you get started.

**Pre-requisite**

-   package manager: pip
-   runtime: python3
-   container: docker

### Environment setup

Follow the steps below to prepare your local python environment, which will allow integration with  
IDEs, run unit and integration tests and spin up a local web server for quick testing.

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
1. That's it. You're ready to integrate your IDE, make code changes, test and spin up the web  
   server.

## Testing

### Unit

```bash
pytest tests
```

### Integration

These are testing the api contract and the business logic in general. It spins up a web service  
as a docker container in your local enviroment and uses a vanilla python client (`requests`) to  
send requests to the api.

1. Start the web server:
    ```bash
    docker compose up gota-core -d
    ```
1. Run tests:
    ```bash
    pytest tests-integration
    ```
1. Stop the web server:
    ```bash
    docker compose down
    ```

## Adding a new python dependency

1. Create a virtualenv:
    ```bash
    python3 -m venv env
    . env/bin/activate
    ```
1. Install the dependency:
    ```bash
    pip3 install "{dependency}"
    ```
1. Remove gota-core from the dependency tree (which is only used for development):
    ```bash
    pip3 uninstall gota
    ```
1. Update requirements.txt:
    ```bash
    pip3 freeze > requirements.txt
    ```

## Accessing the OpenAPI spec

JSON spec: http://localhost:8080/openapi.json
Interactive console: http://localhost:8080/docs
