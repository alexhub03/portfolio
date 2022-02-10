# Importing boto3 library to make functionality available
import boto3


session = boto3.Session(profile_name='iamadmin-general')

# Creating a client connection with AWS S3
s3 = session.client('s3')
# Creating a bucket
s3.create_bucket(Bucket='testbucket20220210second')    #no characters in the bucket name e.g. _ or - 
print("Bucket created succesfully")



#session methods:
# https://stackoverflow.com/questions/33378422/how-to-choose-an-aws-profile-when-using-boto3-to-connect-to-cloudfront