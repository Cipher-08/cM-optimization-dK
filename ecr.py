import boto3

aws_access_key_id = 'AKIAZQ3DQ4GWRVR332OF'
aws_secret_access_key = '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'
aws_region = 'us-east-1'

ecr_client = boto3.client('ecr',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name=aws_region)

repository_name = "trial_and_tested"

response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)
