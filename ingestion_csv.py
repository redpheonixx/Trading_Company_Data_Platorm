import csv
import requests
import boto3
import pandas as pd

class PushandPullCsvData:
    def __init__(self):
        self.client=boto3.client("s3", endpoint_url='http://localhost:4566')
        cur_time=datetime.datetime.now().isoformat()
    
    def push(self, file_path, fileName):
        s3Key= fileName+self.cur_time
        response = self.client.upload_file(file_path, 'csvdata-ldzone', s3Key)
        print(response)

    def pull(self):
        result=self.client.get_object(Bucket='csvdata-ldzone', Key='data_01.csv')
        initial_df = pd.read_csv(result['Body'])
        print(initial_df)



