from diagrams import Cluster, Diagram
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server
from diagrams.onprem.database import MongoDB
from diagrams.programming.language import Python
from diagrams.aws.network import CloudFront

with Diagram("Flask Application Architecture", show=False):

    user = Users("User")

    flask_app = Server("Flask App")
    redis_db = MongoDB("Redis")
    mongo_db = MongoDB("MongoDB")

    cloudfront = CloudFront("HTTPS Traffic")

    user >> cloudfront >> flask_app

    with Cluster("Flask App Components"):
        flask_app >> redis_db >> mongo_db

        flask_app >> mongo_db   

