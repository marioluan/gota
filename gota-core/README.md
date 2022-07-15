# gota-core

Core library which implements an API to create, read and update recipes.

## Deployment mode: ASGI Web Server

The API is powered by [FastAPI](https://github.com/tiangolo/fastapi) and backed by [uvicorn ASGI web server](https://www.uvicorn.org/).

## Development

The steps below should help you get started.

**Pre-requisite**

-   package manager: pip
-   runtime: python3

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

These are testing the api contract and the business logic in general. It's using a vanilla python  
client, but I have plans to use one generated from the api spec (openapi).

1. Start the web server:
    ```bash
    uvicorn gota.core.api:app --reload
    ```
1. Run tests:
    ```bash
    pytest tests-integration
    ```

Note: you will need to start both processes separately.

### Code coverage

TBD.

## Contributing

TBD.
