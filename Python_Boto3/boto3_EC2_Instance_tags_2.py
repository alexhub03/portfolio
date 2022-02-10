import boto3
from pprint import pprint

session = boto3.Session(profile_name='iamadmin-general')

ec2_client = session.client('ec2')

response = ec2_client.describe_instances()

instances = response['Reservations']

print(instances)

for instance in instances:
    print(instance['Instances'][0]['InstanceId'])
    
instance_ids = []

for instance in instances:
    instance_ids.append(instance['Instances'][0]['InstanceId'])
    
tag_creation = ec2_client.create_tags(
    Resources =
        instance_ids,
    Tags =  [
      {
        
        'Key': 'OperatingHours',   
        'Value': 'start=(M-S,0;stop=(M-F,8);tx=et'
      }         
             
     
             
             
             
    ]
    

    
    
)

    
