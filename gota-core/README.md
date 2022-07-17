# gota-core

Core library which implements an API to create, read and update recipes.

## Deployment modes

The API is powered by [FastAPI](https://github.com/tiangolo/fastapi). It supports OpenAPI and can generate clients from the specification. Lastly, it supports many authentication mechanisms, such as JTW. [Uvicorn](https://www.uvicorn.org/) is used to spin up a standalone web server (quite useful in tests). To integrate with AWS, I'm using [Mangum](https://mangum.io/asgi-frameworks/) adapter.

### Local ASGI Web Server

```bash
docker compose up gota-core -d
```

### Local AWS Stack

Go to `gota-cdk` and check the `Deploy > Local` section in its README.md file.

## Development

**Pre-requisite**

-   [python3](https://www.python.org/downloads/)
-   [pip](https://github.com/pypa/pip)
-   [pipenv](https://github.com/pypa/pipenv)
-   [docker](https://docs.docker.com/get-docker/)

### Environment setup

Follow the steps below to prepare your local python environment, which will allow integration with IDEs, run unit and integration tests and spin up a local web server for quick testing.

1. Create a virtualenv:
    ```bash
    pipenv --python 3.8
    pipenv shell
    ```
1. Install all dependencies (dev included):
    ```bash
    pipenv install --dev
    ```

## Testing

### Unit

```bash
pytest tests
```

### Integration

These are testing the api contract and the business logic in general. It spins up a web service as a docker container in your local enviroment and uses a vanilla python client (`requests`) to send requests to the api.

1. Start the web server:
    ```bash
    docker compose up gota-core -d
    ```
1. Run tests:
    ```bash
    API_URL="http://localhost:8080" \
    API_STAGE="local" \
        pytest tests-integration
    ```
1. Stop the web server:
    ```bash
    docker compose stop gota-core
    ```

## Format

Format the code:

```bash
FOLDERS="src tests tests-integration"
LINE_LENGTH="100"

isort ${FOLDERS}
black --line-length "${LINE_LENGTH}" ${FOLDERS}
```

### Code Style

```bash
FOLDERS="src tests tests-integration"
flake8 ${FOLDERS}
```

## Accessing the OpenAPI spec

JSON spec: http://localhost:8080/openapi.json  
Interactive console: http://localhost:8080/docs

## Clients

To update the client, simply run the command below:

```bash
docker compose run gota-core-client-generator
```

The client in gota-core-client will be updated with the new code.
