import csv
import requests
import boto3

class PushCsvData:
    def __init__(self):
        self.client=boto3.client("s3", endpoint_url='http://localhost:4566')
    
    def push(self):
        file_path=r"C:\Users\singsina\Documents\DE\Trading_Platform_Data_Platorm\Data\trade_data.csv"
        response = self.client.upload_file(file_path, 'csvdata-ldzone', 'data_01.csv')
        print(response)


