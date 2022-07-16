from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.general import User
from diagrams.aws.management import Cloudwatch
from diagrams.aws.network import APIGateway
from diagrams.aws.security import Cognito

with Diagram("High-Level Architecture", show=False):
    with Cluster("Internet"):
        service_user = User("Customer")

    with Cluster("Amazon Web Services"):
        auth = Cognito("Auth")
        storage = Dynamodb("Storage")
        monitoring = Cloudwatch("Monitoring")
        request_handler = Lambda("RequestHandler")
        reverse_proxy = APIGateway("ReverseProxy")

        service_user - auth
        service_user - reverse_proxy

        reverse_proxy - auth
        reverse_proxy - request_handler

        request_handler - storage
        request_handler - monitoring
