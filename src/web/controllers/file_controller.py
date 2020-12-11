import boto3
from botocore.exceptions import ClientError

from src.web.controllers.base_controller import BaseController


class FileController(BaseController):
    def presigned_upload(self, bucket_name="", object_name="", **kwargs):
        print(kwargs)
        s3_client = boto3.client('s3')
        try:
            response = s3_client.generate_presigned_post(bucket_name,
                                                         object_name,
                                                         ExpiresIn=600)
        except ClientError as e:
            print(e)
            return None

        # The response contains the presigned URL and required fields
        return response
