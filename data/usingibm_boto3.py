import ibm_boto3
from ibm_botocore.client import Config, ClientError

# Constants for IBM COS values
COS_ENDPOINT = "https://s3.private.eu-de.cloud-object-storage.appdomain.cloud"
COS_API_KEY_ID = "ad9e0d58-e283-4ffd-a456-3e10af0310a7" 
COS_INSTANCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/d64b4549737c46368b166243aaaa3a2f:395e4e8c-1e9a-4010-abf9-7c74db93a467::" 


# Create resource
cos = ibm_boto3.resource("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_INSTANCE_CRN,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)

# Upload a new file
data = open('test.jpg', 'rb')
cos.Bucket('cars-test-bucket').put_object(Key='test.jpg', Body=data)