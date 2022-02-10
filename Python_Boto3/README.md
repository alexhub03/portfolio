# Docker Documentation


## AWS Docker 
```
+ AWS: Cloudformation Template - Prebuilt Application Stack:
https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0030-aws-associate-ec2docker/ec2docker.yaml&stackName=EC2DOCKER

```


## Quick Command Reference:

```
sudo amazon-linux-extras install docker
sudo service docker start   
sudo usermod -a -G docker ec2-user    
LOGOUT and login
sudo su - ec2-user

# Build Docker Image
cd aws-sa-associate-saac02/09-Containers-ECS/container_of_test/container
docker build -t containeroftest .
docker images --filter reference=containeroftest

# Run Container from Image
docker run -t -i -p 80:80 containeroftest


# Docker file:
FROM centos: latest     
LABEL maintainer="test4"  
RUN yum -y install httpd    
COPY index.html /var/www/html  
COPY containerandtest*.jpg /var/www/html     
ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]    
EXPOSE 80   #which services should be exposed. Port 80

# Upload Container to Dockerhub 
docker login --username=YOUR_USER
docker images
docker tag IMAGEID YOUR_USER/containeroftest
docker push YOUR_USER/containeroftest:latest




```


