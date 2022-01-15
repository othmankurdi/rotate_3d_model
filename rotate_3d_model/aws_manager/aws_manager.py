import boto3


class AWSManager:
    def download_from_s3(self, bucket_name, file_name, save_path):
        s3 = boto3.client('s3')
        s3.download_file(bucket_name, file_name, save_path)
