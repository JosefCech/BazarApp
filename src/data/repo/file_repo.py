import boto3


class FileRepo():
    def __init__(self, bucket_name="", session=boto3):
        self._bucket_name = bucket_name
        self._s3_client = session.client('s3')

    def read_bytes(self, key):
        s3_object = self._s3_client.get_object(Bucket=self._bucket_name, Key=key.replace("-", "/"))
        body = s3_object['Body']
        return body.read()

    def list_s3_keys(self, prefix):
        """Get a list of keys in an S3 bucket."""
        resp = self._s3_client.list_objects_v2(Bucket=self._bucket_name, Prefix=prefix)
        files = []
        if 'Contents' not in resp:
            return files
        for obj in resp['Contents']:
            print(obj)
            file_name_array = obj['Key'].split(".")
            if len(file_name_array) < 2:
                continue
            if file_name_array[-1] not in ["jpg", "jpeg", "png"]:
                continue
            files.append(obj['Key'])
        return files
