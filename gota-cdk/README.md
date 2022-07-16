# gota-cdk

Infrastructure management for `gota-core`.

**Pre-requisites**

-   [aws cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
-   [aws sam cli](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac.html)
-   [aws cdk](https://docs.aws.amazon.com/cdk/v2/guide/cli.html)
-   [docker](https://docs.docker.com/get-docker/)

## Deploy

### Production

Ideally, I'd create a CI/CD pipeline in AWS, but for the sake of time, I decided to use vanilla
cdk to deploy. Also, it will deploy and use the default API Gateway url - but I'd use a DNS/Route53  
instead.

**Pre-requisite**
Valid aws credentials.

```bash
# run only if you'r running for the first time
cdk bootstrap

# run only if it's already deployed
cdk diff

# this is used all the time
cdk deploy
```

### Local

We use `sam local` to [start a local instance of API Gateway](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-start-api.html) and integrate with our Lambda. The steps below will deploy  
docker containers locally with an in-memory DynamoDB, API Gateway and Lambda.

> Read [this blog post](https://medium.com/@mahesh_61440/using-aws-cdk-to-quickly-create-a-proof-of-concept-dca2696fad77)  
> to understand the integration between cdk and sam.

1. Start a local DynamoDB server:

    ```bash
    # dynamodb-local is the name of the service present on the docker-compose.yaml file
    cd ../gota-core
    docker compose up "dynamodb-local" -d

    # it should start running on http://localhost:8000, this is also configured
    # in the docker-compose.yaml file
    ```

1. Create the "Recipes" table in DynamoDB:

    ```bash
    # local dynamodb doesn't need real creds. region can be any. endpoint is from the previous
    # command [above]
    export TABLE_NAME="Recipes" \
    && export AWS_ACCESS_KEY_ID="LEAVE_AS_IS" \
    && export AWS_SECRET_ACCESS_KEY="LEAVE_AS_IS" \
    && export REGION="us-east-1" \
    && export ENDPOINT_URL="http://localhost:8000"
    aws dynamodb create-table \
        --table-name "${TABLE_NAME}" \
        --attribute-definitions "AttributeName=recipe_id,AttributeType=S" \
        --key-schema "AttributeName=recipe_id,KeyType=HASH" \
        --provisioned-throughput "ReadCapacityUnits=5,WriteCapacityUnits=5" \
        --region "${REGION}" \
        --endpoint-url "${ENDPOINT_URL}"
    ```

1. Generate a cloudformation template from the cdk application:
    ```bash
    cd ../gota-cdk
    AWS_SAM_LOCAL="true" cdk synth --no-staging > "template.yaml"
    ```
1. Build a docker image from the cloudformation template:
    ```bash
    sam build
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

#### Test

Now that the service is up and running, you can execute the command below to validate the
api is working as expected (or play with it as you wish):

```bash
cd ../gota-core
pytest tests-integration
```

#### Clean up

1. Delete the Recipes table:
    ```bash
    export TABLE_NAME="Recipes" \
    && export AWS_ACCESS_KEY_ID="LEAVE_AS_IS" \
    && export AWS_SECRET_ACCESS_KEY="LEAVE_AS_IS" \
    && export REGION="us-east-1" \
    && export ENDPOINT_URL="http://localhost:8000"
    aws dynamodb delete-table \
        --table-name "${TABLE_NAME}" \
        --endpoint-url "${ENDPOINT_URL}" \
        --region "${REGION}"
    ```
1. Delete the local DynamoDB:
    ```bash
    cd ../gota-core
    docker compose down "dynamodb-local"
    ```
