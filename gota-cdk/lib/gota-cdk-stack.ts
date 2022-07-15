import { Stack, StackProps } from 'aws-cdk-lib'
import * as apigateway from 'aws-cdk-lib/aws-apigateway'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import { Construct } from 'constructs'

export class GotaCdkStack extends Stack {
    // FIXME: don't use relative paths
    private static DOCKER_FILE_ROOT = '../gota-core'

    constructor(scope: Construct, id: string, props?: StackProps) {
        super(scope, id, props)

        // API
        const api = new apigateway.RestApi(this, 'Api', {
            restApiName: 'Recipes Service',
            description: 'This service manages recipes.',
        })

        // Request handler
        const handler = new lambda.DockerImageFunction(this, 'RequestHandler', {
            code: lambda.DockerImageCode.fromImageAsset(GotaCdkStack.DOCKER_FILE_ROOT),
        })

        // Integration between Api Gateway and gota-core's handlers
        const integration = new apigateway.LambdaIntegration(handler, {
            // TODO: find out what's this
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
