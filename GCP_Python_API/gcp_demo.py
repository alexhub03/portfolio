import os
from google.cloud import storage #storage module

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cloudstorage2_service_key_GCP.json'  #locate the service account file

storage_client = storage.Client()  #create storage client instance

bucket_name = '<bucket name'

"""
Create New Bucket
"""
bucket_name = 'data_bucket_20220208_version2'
bucket = storage_client.bucket(bucket_name)
bucket.create(location='US')

"""
Print Bucket Detail
"""
vars(my_bucket)   #vars function

"""
Accessing a specific bucket
"""

my_bucket = storage_client.get_bucket('data_bucket_20220208_version2')

"""
Upload Files
"""

#Upload file to bucket function

def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        block.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False
    
file_path = 'E:\\2022_GCP\\Data Files'
upload_to_bucket('test file', os.path.join(file_path, 'test.csv', 'data_bucket_20220208_version2')
"""
Download Files
"""
#To be continued

# Credit to tutorial: https://www.youtube.com/watch?v=pEbL_TT9cHg&t=659s