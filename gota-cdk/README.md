# gota-cdk

Infrastructure management for `gota-core`.

**Pre-requisites**

-   [aws cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
-   [aws sam cli](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac.html)
-   [aws cdk](https://docs.aws.amazon.com/cdk/v2/guide/cli.html)
-   [docker](https://docs.docker.com/get-docker/)

## Deploy

### Production

Coming soon...

### Local

We use `sam local` to [start a local instance of API Gateway](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-start-api.html) and integrate with our Lambda.

#### Build & Run

The steps below will deploy docker containers for a local DynamoDB server, API Gateway and Lambda.
Read [this blog post](https://medium.com/@mahesh_61440/using-aws-cdk-to-quickly-create-a-proof-of-concept-dca2696fad77)  
to understand the integration between cdk and sam.

1. Generate a cloudformation template from the cdk application:
    ```bash
    cdk synth --no-staging > "template.yaml"
    ```
1. Build a docker image from the cloudformation template:
    ```bash
    sam build
    ```
1. Start a local DynamoDB server:

    ```bash
    # dynamodb-local is the name of the service present on the docker-compose.yaml file
    cd ../gota-core && docker compose up "dynamodb-local"

    # it should start running on http://localhost:8000, this is also configured
    # in the docker-compose.yaml file
    ```

1. Create the recipes table in local DynamoDB server:
    ```bash
    # local dynamodb doesn't need real creds. region can be any. endpoint is from the previous
    # command [above]
    AWS_ACCESS_KEY_ID='LEAVE_AS_IS' \
    AWS_SECRET_ACCESS_KEY='LEAVE_AS_IS' \
    REGION='us-east-1' \
    ENDPOINT_URL="http://localhost:8000" \
    aws dynamodb create-table \
        --table-name "Recipe" \
        --attribute-definitions "AttributeName=recipe_id,AttributeType=S" \
        --key-schema "AttributeName=recipe_id,KeyType=HASH" \
        --provisioned-throughput "ReadCapacityUnits=5,WriteCapacityUnits=5" \
        --region "${REGION}" \
        --endpoint-url "${ENDPOINT_URL}"
    ```
1. Spin up an API Gateway integrated with gota API through Lambda:
    ```bash
    # the port here matter for integration test, they need to match
    # docker-network also need to match dynamodb's
    sam local start-api \
        --warm-containers "LAZY" \
        --env-vars ".sam-local.env.json" \
        --port "8080" \
        --docker-network "sam-local"
    ```

##### Test

Now that the service is up and running, you can execute the command below to validate the
api is working as expected:

```bash
cd ../gota-core && pytest tests-integration
cd ../gota-cdk
```
