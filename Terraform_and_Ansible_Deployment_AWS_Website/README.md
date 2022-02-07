# Create/Provision an Apache Website through Terraform and Ansible

+ Configure AWS Keys
+ Terraform Code:
    + Terraform main.tf: connected to compute and vpc definitions 
    + Terraform Virtual (vpc): 
        + Defined region us-east1
        + Created internet gateway 
        + Created public route table
        + Created subnet 10.0.1.0/24
        + Created security group (ingress and egress) tcp ports 22 and 80 , opened on 0.0.0.0/0
    + Terraform compute:
        + Specified instance type & keys
        + Remote exec provisioner specified to install ansible     playbook isntall_apache.yaml to assist with apache webserver setup



## Quick Command Reference:
```
terraform init

terraform validate #validate config files

terraform plan  #execution plan 

terraform apply auto approve

```

### Terraform deployment + Output:
<a href="https://drive.google.com/uc?export=view&id=SeBuUq57NZRVyH7HKSzqW9bLNdBtD"><img src="https://drive.google.com/uc?export=view&id=SeBuUq57NZRVyH7HKSzqW9bLNdBtD" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>



### Proof of Concept:
<a href="https://drive.google.com/uc?export=view&id=1TVQol_i5XVQGsZkhDxU2ZaskcEi758Nn"><img src="https://drive.google.com/uc?export=view&id=1TVQol_i5XVQGsZkhDxU2ZaskcEi758Nn" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>


