# gota-cdk

Infrastructure management for `gota-core`.

**Pre-requisites**

-   aws resources management: [aws cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
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
    cdk synth --no-staging > "template.yaml"
    ```

1. Build a docker image with the stack(s) from the cloudformation template:
    ```bash
    sam build
    ```
1. Start a local DynamoDB server:
    ```bash
    cd ../gota-core && docker compose up "dynamodb-local"
    ```
1. Create the recipes table in local DynamoDB server:
    ```bash
    # given we're using dynamodb locally, creds can be fake
    AWS_ACCESS_KEY_ID='LEAVE_AS_IS' \
    AWS_SECRET_ACCESS_KEY='LEAVE_AS_IS' \
    aws dynamodb create-table \
        --table-name "Recipe" \
        --attribute-definitions "AttributeName=recipe_id,AttributeType=S" \
        --key-schema "AttributeName=recipe_id,KeyType=HASH" \
        --provisioned-throughput "ReadCapacityUnits=5,WriteCapacityUnits=5" \
        --region "us-east-1" \
        --endpoint-url "http://localhost:8000"
    ```
1. Spin up an API Gateway integrated with gota API through Lambda:
    ```bash
    sam local start-api \
        --warm-containers "LAZY" \
        --env-vars ".sam-local.env.json" \
        --port "8080" \
        --docker-network "sam-local"
    ```

##### Test

Go to go-core package and execute integration tests:

```bash
pytest tests-integration
```
