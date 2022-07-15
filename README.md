# gota

Gota, an API for recipes powered by AWS and FastAPI.

## Components

-   gota-cdk: infrastructure management and deployment.
-   gota-core: core library which implements an api to create, read and update recipes.

## Run Locally

There are two ways to run the api locally: via a ASGI web service or an emulated aws environment.

### ASGI Web Service

Go to gota-core and check the `Testing > Integration` section in its README.md file.

### Emulated aws environment

Go to gota-cdk and check the `Deploy > Local > Build & Run` section in its README.md file.

## TODO

-   Add CI/CD pipeline.
-   Add availability and latency monitors (based on service-level metrics) and alarm on breach of SLA.
-   Add integration with DynamoDB or S3 to store recipes.
-   Add git integration to run various code quality checks for cdk and python as part of hooks.
-   Add performance tests and integrate with CI/CD to capture regression.
-   Add smoke tests and integrate with CI/CD to validate deployments.
-   Add canaries to produce traffic.
-   Add indexes to DynamoDB and implement search in the API.
