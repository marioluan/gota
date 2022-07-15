# gota

Gota, an API for recipes powered by AWS and FastAPI.

## Components

-   gota-cdk: infrastructure management and deployment.
-   gota-core: core library which implements an api to create, read and update recipes.

## Run Locally

There are two ways to run the api locally: via an ASGI web service or a local aws environment.

### ASGI Web Service

Go to `gota-core` and check the `Testing > Integration` section in its README.md file.

### AWS Environment

Go to `gota-cdk` and check the `Deploy > Local > Build & Run` section in its README.md file.

## Roadmap

-   [Feature] Add support to query recipes by fields other than id.
-   [Feature] Add thumbnails to recipes.
-   [Feature] Create a lightweight client to query the API.
-   [Feature] Add custom validation to models, such as min, max, etc.
-   [CI/CD] Add CI/CD pipeline.
-   [CI/CD] Add performance tests and run them as part of CI/CD.
-   [CI/CD] Add smoke tests and run them as part of CI/CD.
-   [CI/CD] Add [always up] canaries to produce traffic and help measure service health.
-   [CodeQuality] Add git integration to run various code quality checks for cdk and python.
-   [CodeQuality] Add code coverage integration.
-   [Monitoring/Operations] Add service health monitors (availability and latency) and alarm on breach of SLA.
-   [Monitoring/Operations] Publish business and service metrics/logs to metrics/logs storage.
-   [Monitoring/Operations] Add business and operational dashboards.
-   [Monitoring/Operations] Add service-impairent runbooks to help troubleshoot, find root causes and mitigate them.
-   [Security] Add some kind of authentication (e.g. token).
-   [Security] Run a thread model to capture security vulnerabilities.
