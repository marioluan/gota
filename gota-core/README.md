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

There are currently two types of testing setup available: unit and integration. You can find below  
how to run them:

### Unit

```bash
pytest tests
```

### Integration

These are testing the api contract and the business logic in general. It spins up a web service  
as a docker container in your local enviroment and uses a vanilla python client to send requests  
to the api.

1. Start the web server:
    ```bash
    docker compose up -d
    ```
1. Run tests:
    ```bash
    pytest tests-integration
    ```
1. Stop the web server:
    ```bash
    docker compose down
    ```

## Contributing

### Adding a new python dependency

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

### TODO

-   Add search capabilities to API.
-   Add mypy, flake8, black and isort as development dependencies.
-   Integrate with GitHub actions to enforce running mypy, flake8, black, isort and unit test.
-   Add code coverage integration.
-   Generate client for integration tests from openapi spec.
-   Add middleware for logging and tracing.
-   Add authentication and autorization.
-   Integrate with DynamoDB or S3.
-   Make OpenAPI spec available either from S3 or as part of the api.
-   Publish service metrics and logs to CloudWatch.
