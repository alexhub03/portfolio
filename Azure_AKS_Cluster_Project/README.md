# Provisioning and Management of a highly available AKS cluster with 2 replicas in a pod

+ Azure AKS cluster with a node pool of 3 nodes
+ Deployment manifest file of the cluster (2 replicas in the pod) , pod template configure, nginx   image from docker hub + resource limits
+ Port 80 Service opened and load balancer service added for external access



## Quick Command Reference:
```
kubectl get deployment # List a particular deployment

kubectl get pod  # Running pods

kubectl get rs # Current replica sets deployed

kubectl get service # Load balancer information found here

https://kubernetes.io/docs/reference/kubectl/cheatsheet/

```
## Quick Command Reference, Azure Specific:

```
# created variable RG for the resource group
cloud@Azure:~$ RG=491-420b013b-deploying-and-accessing-an-applicatio  

az aks create \ 
--resource-group $RG \ 
--name Cluster01 \            
--node-count 3 \
--generate-ssh-keys \
--node-vm-size Standard_B2s \
--enable-manage-identity

# Configure kubectl to run commands against.   kubectl needs to know which cluster to run against

az aks get-credentials --name Cluster01 --resource-group $RG

# Deploy yaml
cloud@Azure:~$ kubectl apply -f ./deployment.yaml    

cloud@Azure:~$ kubectl apply -f ./service.yaml  
```

## Important Notes

+ Sequnce of commands to provision EKS cluster
---
```
+ Open Azure cloud shell using bash
+ AZ group list: find resource group name


cloud@Azure:~$ RG=491-420b013b-deploying-and-accessing-an-applicatio  # created variable RG

az aks create \ 
--resource-group $RG \ 
--name Cluster01 \            
--node-count 3 \
--generate-ssh-keys \
--node-vm-size Standard_B2s \
--enable-manage-identity

--resource-group $RG \ 
--name Cluster01 \              # name if the cluster
--node-count 3 \                   # 3 nodes
--generate-ssh-keys \          #generate ssh keys for authentication to the nodes
--node-vm-size Standard_B2s \             # standards B2s size for the nodes
--enable-manage-identity                       # cluster to create infra resources


#configure kubectl to run commands against.   kubectl needs to know which cluster to run against

az aks get-credentials --name Cluster01 --resource-group $RG

#create deployment manifest file

touch deployment.yaml


apiVersion: apps/v1
 #The type of workload we are creating 
kind: Deployment
metadata:
  #Name of deployment - Required
  name: aks-web-app-deployment 
spec:
  replicas: 2      # 2 replicas of the pods created 
  selector:
    matchLabels: 
      app: aks-web-app
  #Pod template which decribes the pod you want to deploy
  template: 
    metadata:
      #Used to logically group pods together
      labels: 
        app: aks-web-app
    #Specific details about the containers in the Pod
    spec: 
      containers:
      - name: aks-web-app-container
        #Docker Hub image to use
        image: nginx                               # using nginx image  from public docker hub
        #Define ports to expose
        ports: 
        - containerPort: 80                  # open up port 80  used by load balancer 
          #Reference name of port
          name: http 
        resources:
          #Minimum amount of resources we want
          requests: 
            cpu: 100m
            memory: 128Mi
          #Maximum amount of resources we want
          limits: 
            cpu: 250m
            memory: 256Mi



cloud@Azure:~$ touch deployment.yaml
cloud@Azure:~$ kubectl apply -f ./deployment.yaml                   #deploy the pods with this file.


	• Navigate to the Cluster and workloads to see the deployment 
	• Click inside to see the deployment and pods associated
	• Now do to similar process to create service.yaml

cloud@Azure:~$ touch service.yaml


apiVersion: v1
 #The type of workload we are creating 
kind: Service
metadata:
#Name of Service - Required
  name: aks-web-app-service
#Specific details about the Service
spec:
#Type of Service to be deployed
  type: LoadBalancer
  ports:
  - port: 80
  #Used to tell the Service which Pods to associate with
  selector:
    app: aks-web-app   #tells teh service which app to be associated to 


cloud@Azure:~$ touch service.yaml
cloud@Azure:~$ kubectl apply -f ./service.yaml
service/aks-web-app-service created



https://github.com/linuxacademy/content-aks-basics/tree/master/Lab-Deploying-and-accessing-an-application-to-an-AKS-cluster



```

## AKS Cluster Creation and Infrastructure
---

### AKS Cluster Diagram:
<a href="https://drive.google.com/uc?export=view&id=1JmBHiGa6cr2sCAvh7uvlNDK8ic0scbdA"><img src="https://drive.google.com/uc?export=view&id=1JmBHiGa6cr2sCAvh7uvlNDK8ic0scbdA" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>


### Create storage / account
<a href="https://drive.google.com/uc?export=view&id=1GRTb2FqACeT-qzJoQ_CyTbS_T-XuVZNh"><img src="https://drive.google.com/uc?export=view&id=1GRTb2FqACeT-qzJoQ_CyTbS_T-XuVZNh" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

### Create the Cluster with "az aks create \" command
<a href="https://drive.google.com/uc?export=view&id=1NhcTmfd7LNxLpr6Ery-skDM3T7Xl34Pm"><img src="https://drive.google.com/uc?export=view&id=1NhcTmfd7LNxLpr6Ery-skDM3T7Xl34Pm" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

### Kubernetes Services, AKS Cluster created 
<a href="https://drive.google.com/uc?export=view&id=1gg5mPkOAXusRGeuPQHHjydO7PKuDdlbq"><img src="https://drive.google.com/uc?export=view&id=1gg5mPkOAXusRGeuPQHHjydO7PKuDdlbq" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

### Deployment Manifest file
<a href="https://drive.google.com/uc?export=view&id=1CpH3ov_oE0JpeEo61K5lHbdsINJB1mRJ"><img src="https://drive.google.com/uc?export=view&id=1CpH3ov_oE0JpeEo61K5lHbdsINJB1mRJ" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

### Load balancer service creation 
<a href="https://drive.google.com/uc?export=view&id=1UaP7J9At7M0yS4yII-cECzz1VtYXSymC"><img src="https://drive.google.com/uc?export=view&id=1UaP7J9At7M0yS4yII-cECzz1VtYXSymC" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>


<a href="https://drive.google.com/uc?export=view&id=1uBk6ZSFDhjfkhQlyT0T3YvwEqQM3ZTwX"><img src="https://drive.google.com/uc?export=view&id=1uBk6ZSFDhjfkhQlyT0T3YvwEqQM3ZTwX" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>


