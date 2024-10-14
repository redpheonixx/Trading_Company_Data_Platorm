import csv
import requests
import boto3


class BucketDefinition:
    def __init__(self):
        self.client=boto3.client("s3", endpoint_url='http://localhost:4566')

    def createBucket(self, name):
        try:
            self.client.create_bucket(
                Bucket='trading_data', 
                CreateBucketConfiguration={
                    'LocationConstraint': 'us-west-1'
                    }
            )
            print(f"Bucket {name} created successfully")
        except:
            

    def createPartition():