from aws_cdk import aws_ecs_patterns as ecsp
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_elasticloadbalancingv2 as elbv2
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_iam as iam
from aws_cdk import aws_ecs as ecs



vpc = ec2.Vpc(
    stack, "MyVpc",
    max_azs=2
)
# ELB Account ID for us-east-1
elbAccountId = 127311923021
bucket = s3.Bucket(self, "access-log-bucket", bucket_name= 'lb_logs')
bucket.grant_put(iam.AccountPrincipal(elbAccountId))

appLB = elbv2.ApplicationLoadBalancer(self,
    "LB",
    vpc=vpc,
    internet_facing=True,
    log_access_logs={
        "bucket": bucket,
        "prefix": "test-lb",
        "enabled": True,
    )
)

api = ecsp.ApplicationLoadBalancedEc2Service(
      self,
      "my-aws-service",
      service_name="mycoderservice",
      cluster=self.cluster,
      cpu=512,
      memory_limit_mib=512,
      desired_count=4,
      task_image_options={
        "image": ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")
      },
      load_balancer=appLB,
      domain_name="exampledomain.com"
)
