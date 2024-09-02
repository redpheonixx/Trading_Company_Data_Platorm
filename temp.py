import csv
import requests
import boto3
import pandas as pd

class PushCsvData:
    def __init__(self):
        self.client=boto3.client("s3", endpoint_url='http://localhost:4566')
    
    def push(self):
        file_path=r"C:\Users\singsina\Documents\DE\Trading_Platform_Data_Platorm\Data\trade_data.csv"
        response = self.client.upload_file(file_path, 'csvdata-ldzone', 'data_01.csv')
        print(response)

    def pull(self):
        result=self.client.get_object(Bucket='csvdata-ldzone', key='data_01.csv')
        initial_df = pd.read_csv(obj['Body'])
        print(initial_df)

new_obj=PushCsvData()
new_obj.pull()

