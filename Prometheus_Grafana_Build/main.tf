
provider "aws" {
  region = "us-east-1"
}


# 1. Create VPC
resource "aws_vpc" "firstvpc" {   
  cidr_block = "10.0.0.0/16"
  tags = {
       Name = "production-1"    
  }
}

# 2. Create Internet Gateway
resource "aws_internet_gateway" "gw" {
  vpc_id     = aws_vpc.firstvpc.id  
  tags = {
    Name = "prod-subnet-1"
  }
}

# 3. Create Custom Route Table

resource "aws_route_table" "tf_public_route" {
  vpc_id = aws_vpc.firstvpc.id 
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }
  tags = {
    Name = "Terraform-Public-RouteTable"
  }
}


# 4. Create a Subnet
resource "aws_subnet" "subnet-1" {
    vpc_id = aws_vpc.firstvpc.id 
    cidr_block = "10.0.1.0/24"
    availability_zone = "us-east-1a"

    tags = {
        Name = "prod-subnet"
    }
}

# 5. Associate Subnet with Route Table

resource "aws_route_table_association" "tf_public_assoc" {
  subnet_id      = aws_subnet.subnet-1.id
  route_table_id = aws_route_table.tf_public_route.id
}

# 6. Create Security Group to Allow Port 22, 80 443

resource "aws_security_group" "tf_public_sg" {
  name        = "allow_web_traffic" 
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_vpc.firstvpc.id 

  ingress {                  
    
      description      = "HTTPS traffic"
      from_port        = 443
      to_port          = 443
      protocol         = "tcp"
      cidr_blocks      = ["0.0.0.0/0"]   
      
    }

  ingress {                 
    
      description      = "HTTP"
      from_port        = 80
      to_port          = 80
      protocol         = "tcp"
      cidr_blocks      = ["0.0.0.0/0"]   
      
    }

  ingress {                 
    
      description      = "HTTP"
      from_port        = 3000
      to_port          = 3000
      protocol         = "tcp"
      cidr_blocks      = ["0.0.0.0/0"]   
      
    }

  ingress {                 
    
      description      = "HTTP"
      from_port        = 9090
      to_port          = 9090
      protocol         = "tcp"
      cidr_blocks      = ["0.0.0.0/0"]   
      
    }

  ingress {                  
    
      description      = "SSH traffic"
      from_port        = 22
      to_port          = 22
      protocol         = "tcp"
      cidr_blocks      = ["0.0.0.0/0"]   
      
    }
  

  egress {
    
      from_port        = 0
      to_port          = 0
      protocol         = "-1"
      cidr_blocks      = ["0.0.0.0/0"]      
  }
  tags = {
    Name = "Terraform-SecurityGroup"
  }
}


# 9. Create EC2 Instance to Deploy Prometheus, Grafana, Tomcat Through Ansible

resource "aws_instance" "prometheus_grafana_tomcat" {
   instance_type     = "t2.micro"
   ami               =   "ami-0c2b8ca1dad447f8a"   
   availability_zone = "us-east-1a"
   key_name          = "keyname"
   tags = {
     Name = "webserver_tf"

}
  associate_public_ip_address = true
  vpc_security_group_ids      = [aws_security_group.tf_public_sg.id]
  subnet_id                   = aws_subnet.subnet-1.id
  
# connection {
#       type        = "ssh"
#       user        = "ec2-user"
#       private_key   = file(var.ssh_key_private)
#       host        = self.public_ipterr
#   }

connection {
      type          = "ssh"
      host          = self.public_ip
      user          = "ec2-user"
      password       = ""
      private_key   = file(var.ssh_key_private)
      
  }

# # Local exec provisioner
# provisioner "local-exec" {
#     command     = "echo ${aws_instance.prometheus_grafana_tomcat.public_ip} > inv"
#     working_dir =  "/root/terraform_ansible_prometheus_grafana_build" 

# }

# 11 Execute a Script On a Remote Resource
provisioner "local-exec" {
    command     = "ansible-playbook --private-key=/root/key -i inv /root/jenkins_ansible.yml -k"

 }
}
