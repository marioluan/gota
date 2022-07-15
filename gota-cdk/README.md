# gota-cdk

Infrastructure management for `gota-core`.

**Pre-requisites**

-   serverless deployment: [aws sam cli](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac.html)
-   infrastructure management: [aws cdk](https://docs.aws.amazon.com/cdk/v2/guide/cli.html)
-   container: [docker](https://docs.docker.com/get-docker/)

## Deploy

### Production

Coming soon...

### Local

We use `sam local` to [start a local instance of API Gateway](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-start-api.html) and integrate with our Lambdas.

#### Build & Run

1. Generate cloudformation template:

    ```bash
    cdk synth --no-staging > template.yaml
    ```

1. Build a docker image with the stack(s) from the cloudformation template:
    ```bash
    sam build
    ```
1. Spin up an API Gateway and Lambda integrated with gota API:
    ```bash
    sam local start-api --warm-containers LAZY --port 8000
    ```

##### Test

Go to go-core package and execute integration tests:

```bash
pytest tests-integration
```
