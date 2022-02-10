import boto3
from pprint import pprint

aws_mag_con=boto3.session.Session(profile_name="iamadmin-general")

ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")


response=ec2_con_cli.describe_instances()['Reservations'] 
for each_item in response:  
    for each in each_item ['Instances']:   
        print("=======================")
        print("The image id is: {}\nThe instance ID is: {}\n".format(each['ImageId'],each['InstanceId']))

