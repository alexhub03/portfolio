# Provisioning and Management of a highly available EKS cluster with 3 Worker Nodes deployment

+ Created k8-admin user from IAM
+ Added the user to admin security group
+ Created an EC2 instance: 
    + Auto assign public ip to connect to public IP 
+ Interactive terminal session initialized
+ Updated AWS cli version to version 2 
+ Deploy EKS cluster creation with 3 worker nodes
+ Launch the nginx application deployment on the pods
+ Best practice: create the service first, before the pods/deployments (when Kubernetes starts container creates env variables pointing to all the services when started)
+ Accessed the app through the load balancer which exposed the app to the internet
+ Tested Kubernetes cluster high availability shutting down all 3 nodes


## Quick Command Reference:
```
kubectl get deployment # List a particular deployment

kubectl get pod  # Running pods

kubectl get rs # Current replica sets deployed

kubectl get service # Load balancer information found here

https://kubernetes.io/docs/reference/kubectl/cheatsheet/

```



## Important Notes

+ Sequnce of commands to provision EKS cluster
---
```


https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html

aws --version

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"   #aws cli version 2

unzip awscliv2.zip

sudo ./aws/install

which aws

sudo ./aws/install --bin-dir /usr/bin --install-dir /usr/bin/aws-cli --update 


aws configure
	us-east-1
	json

chmod

	• Install kubectl
https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html

curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.21.2/2021-07-05/bin/linux/amd64/kubectl

chmod +x ./kubectl
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin

kubectl version --short --client


	• Install eksktl (tool to create update and get info about eks cluster)
https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-eksctl.html

curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp

sudo mv /tmp/eksctl /usr/local/bin

eksctl version

eksctl --help


Provision EKS Cluster:
eksctl create cluster --name dev-cluster --verison 1.16 --region us-east-1 --nodegroup-name standard-workers --node-type t3.micro --nodes 3 --nodes-min 1 --nodes.max 4 --managed

eksctl get cluster

aws eks update-kubeconfig --name dev-cluster --region us-east-1

git clone https://gitbub.com/ACLoudGuru-Resources/Course_EKS-Basics

kubectl apply -f ./nginx-svc.yaml

kubectl apply -f ./nginx-deployment.yaml

kubectl get service  # load balancer information 

kubectl get deployment

kubectl get pod

kubectl get rs

kubectl get service

curl a36bc1a82ce4747f9b6129a1f63dea3d-2026412805.us-east-1.elb.amazonaws.com

```


## EKS Cluster Creation and Infrastructure
---
<a href="https://drive.google.com/uc?export=view&id=1qaZvO4pglTs1cqy0E9GBMFoABCW8gRcl"><img src="https://drive.google.com/uc?export=view&id=1qaZvO4pglTs1cqy0E9GBMFoABCW8gRcl" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

<a href="https://drive.google.com/uc?export=view&id=1y6IJN4MoyUoBqCtB_SBmCwchWcM1If2i"><img src="https://drive.google.com/uc?export=view&id=1y6IJN4MoyUoBqCtB_SBmCwchWcM1If2i" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

<a href="https://drive.google.com/uc?export=view&id=1Q1RWXjvaAVamMVg-8UFN-DfLBOdZQYNC"><img src="https://drive.google.com/uc?export=view&id=1Q1RWXjvaAVamMVg-8UFN-DfLBOdZQYNC" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

<a href="https://drive.google.com/uc?export=view&id=1pmij5nn3JEP1etCVnaCZTf-XHA3nZK4T"><img src="https://drive.google.com/uc?export=view&id=1pmij5nn3JEP1etCVnaCZTf-XHA3nZK4T" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

<a href="https://drive.google.com/uc?export=view&id=1dcRdc3ZDFOlDDugA5ay1nxJZPRKEAzB7"><img src="https://drive.google.com/uc?export=view&id=1dcRdc3ZDFOlDDugA5ay1nxJZPRKEAzB7" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>


## EKS Cluster High Availability Cluster Test - 3 Nodes/VMs were shut down for testing

+ Kubernetes high availability spun up 3 more vms for high availability
---
<a href="https://drive.google.com/uc?export=view&id=1qaZvO4pglTs1cqy0E9GBMFoABCW8gRcl"><img src="https://drive.google.com/uc?export=view&id=1qaZvO4pglTs1cqy0E9GBMFoABCW8gRcl" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

