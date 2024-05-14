from diagrams import Cluster, Diagram
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server
from diagrams.onprem.database import MongoDB
from diagrams.programming.language import Python
from diagrams.aws.network import CloudFront
from diagrams.custom import Custom


with Diagram("Flask Application Architecture", show=False):

    user = Users("User")

    with Cluster("Docker"):
        flask_app = Server("Flask App")
        nginx = Custom("Nginx", icon_path="nginx1.png")
        redis_db = Custom("Redis", icon_path="redis1.png")
        mongo_db = MongoDB("MongoDB")

    cloudfront = CloudFront("HTTPS Traffic")

    user >> cloudfront >> nginx >> flask_app 

    with Cluster("Flask App Components"):
        flask_app >> redis_db >> mongo_db
        flask_app << redis_db << mongo_db
   

