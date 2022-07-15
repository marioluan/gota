import { Duration, Stack, StackProps } from 'aws-cdk-lib'
import * as apigateway from 'aws-cdk-lib/aws-apigateway'
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import { Construct } from 'constructs'

export class GotaCdkStack extends Stack {
    // XXX
    // In a production application, I'd make gota-core and gota-cdk two separate projects.
    // Or something else other than relative paths.
    private static DOCKER_FILE_ROOT = '../gota-core'

    constructor(scope: Construct, id: string, props?: StackProps) {
        super(scope, id, props)

        // NOTE
        // sam local doesn't spin a local dynamodb server, so this definition here won't be taken
        // into account when starting a local sam api. Take a look at the README to see how
        // dynamodb is being created locally and used by sam local api.
        const TABLE_NAME = 'Recipe'
        const PARTITION_KEY = 'recipe_id'
        const table = new dynamodb.Table(this, 'Table', {
            tableName: TABLE_NAME,
            partitionKey: { name: PARTITION_KEY, type: dynamodb.AttributeType.STRING },
            // TODO: Add secondary indexes for searching
        })

        // API
        const api = new apigateway.RestApi(this, 'Api', {
            restApiName: 'Recipes Service',
            description: 'This service manages recipes.',
        })

        // Request handler
        const handler = new lambda.DockerImageFunction(this, 'RequestHandler', {
            code: lambda.DockerImageCode.fromImageAsset(GotaCdkStack.DOCKER_FILE_ROOT),
            environment: {
                DYNAMODB_TABLE_NAME: TABLE_NAME,
                DYNAMODB_PARTITION_KEY: PARTITION_KEY,
                // Passing this here, so that sam local can override it and point to a local
                // dynamodb server
                DYNAMODB_ENDPOINT_URL: '',
            },
            // Each request should respond within under a second.
            // Setting it to 10 seconds (which is the timeout for creating Lambda
            // Sandboxes (when the container is launched for the first time) - aka cold invokes.
            timeout: Duration.seconds(10),
        })

        // Integration between Api Gateway and gota-core's handlers
        const integration = new apigateway.LambdaIntegration(handler, {
            // https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html
            requestTemplates: {
                'application/json': JSON.stringify({ statusCode: '200' }),
            },
        })

        // Routes
        const recipes = api.root.addResource('recipes')
        recipes.addMethod('GET', integration)
        recipes.addMethod('POST', integration)

        const recipe = recipes.addResource('{recipe_id}')
        recipe.addMethod('GET', integration)
        recipe.addMethod('PUT', integration)
    }
}
