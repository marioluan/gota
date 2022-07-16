import { Duration, Stack, StackProps } from 'aws-cdk-lib'
import * as apigateway from 'aws-cdk-lib/aws-apigateway'
import * as cognito from 'aws-cdk-lib/aws-cognito'
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import { Construct } from 'constructs'

/**
 * This stack deploy an API with API Gateway as a reverse proxy,
 * Lambda as a request handler and dynamodb as the storage layer.
 */
export class GotaCdkStack extends Stack {
    // XXX
    // In a production application, I'd make gota-core and gota-cdk two separate projects.
    // Or something else other than relative paths.
    private static DOCKER_FILE_ROOT = '../gota-core'

    constructor(scope: Construct, id: string, props?: StackProps) {
        super(scope, id, props)

        // Storage
        const PARTITION_KEY = 'recipe_id'
        const storage = new dynamodb.Table(this, 'Table', {
            // NOTE
            // sam local doesn't spin a local dynamodb server, so this definition here won't be taken
            // into account when starting a local sam api. Take a look at the README to see how
            // dynamodb is being created locally and used by sam local api.
            tableName: 'Recipes',
            partitionKey: { name: PARTITION_KEY, type: dynamodb.AttributeType.STRING },
            // TODO: Add secondary indexes for searching
        })

        // Auth
        const userPool = new cognito.UserPool(this, 'UserPool', { userPoolName: 'Gota' })
        const authorizer = new apigateway.CognitoUserPoolsAuthorizer(
            this,
            'CognitoUserPoolsAuthorizer',
            {
                cognitoUserPools: [userPool],
            }
        )
        new cognito.UserPoolClient(this, 'UserPoolClient', {
            userPool,
            authFlows: {
                adminUserPassword: true,
                userPassword: true,
                custom: true,
                userSrp: true,
            },
            supportedIdentityProviders: [cognito.UserPoolClientIdentityProvider.COGNITO],
        })

        // ReverseProxy
        const api = new apigateway.RestApi(this, 'RestApi', {
            restApiName: 'Recipes Service',
            description: 'This service manages recipes.',
            defaultMethodOptions: {
                authorizer: authorizer,
                authorizationType: apigateway.AuthorizationType.COGNITO,
            },
        })

        // RequestHandler
        const handler = new lambda.DockerImageFunction(this, 'DockerImageFunction', {
            code: lambda.DockerImageCode.fromImageAsset(GotaCdkStack.DOCKER_FILE_ROOT),
            // XXX
            // Only reason is the fact the image is built in a mac
            // It's best to upload the code as part of the deployment, and build the image in
            // aws itself. See https://github.com/aws/aws-lambda-base-images/issues/26
            architecture: process.env.AWS_SAM_LOCAL
                ? lambda.Architecture.X86_64
                : lambda.Architecture.ARM_64,
            environment: {
                DYNAMODB_TABLE_NAME: TABLE_NAME,
                DYNAMODB_PARTITION_KEY: PARTITION_KEY,
                API_ROOT_PATH: 'prod',
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

        // TODO: fix the route below. For some reason it isn't rendering the openapi console.
        // const docs = api.root.addResource('docs')
        // docs.addMethod('GET', integration)

        // Routes
        const recipes = api.root.addResource('recipes')
        recipes.addMethod('GET', integration)
        recipes.addMethod('POST', integration)

        const recipe = recipes.addResource('{recipe_id}')
        recipe.addMethod('GET', integration)
        recipe.addMethod('PUT', integration)
    }
}
