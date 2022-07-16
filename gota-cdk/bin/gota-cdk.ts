#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib'
import 'source-map-support/register'
import { GotaCdkStack } from '../lib/gota-cdk-stack'

// A few things are still needed, such as Auth/Cognito and a CI/CD pipeline.
const app = new cdk.App()
new GotaCdkStack(app, 'GotaCdkStack', {})
