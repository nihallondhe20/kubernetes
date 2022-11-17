# Install EKS (Automation Cluster )
This is called Managed Kubernetes Cluster
KOPS -> Kubernetes operation is done by using KOPS we can setup highly available & production level cluster in aws.
KOPS will create 1 Luanch config & Auto scalling group for server and worker each one. We need to attach config to server.KOPS will install all kubectl required packages in config files and worker node we need to manage it manually.

Amazon Elastic Kubernetes Service (Amazon EKS) is a fully managed Kubernetes service.
EKS is the best place to run Kubernetes applications because of its security, reliability, and scalability.

- EKS can be integrated with other AWS services such as ELB,Amazon CloudWatch, Auto Scaling Groups, AWS Identity and Access Management (IAM), and Amazon Virtual Private Cloud (VPC), providing you a seamless experience to monitor, scale, and load- balance your applications.

- Makes it easy for you to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane.

* Managed Control plane     
 Amazon EKS provides a scalable and highly-available control plane that runs across   multiple AWS availability zones. The Amazon EKS service automatically manages the  availability and scalability of the Kubernetes API servers and the etcd persistence layer for each cluster. Amazon EKS runs the Kubernetes control plane across three Availability Zones in order to ensure high availability, and it automatically detects and replaces unhealthy masters.


# Prerequisites

- AWS Account with Admin Privileges
- Instance Managed Cluster
- AWS Cli access to use kubectl utility

# Step By Step Installation Process on EKS
1). Create IAM Role
- Create iam role select with EKS service with # EKS-Cluster
- Mention Name Properly easy to understand
- Before Going to next read this documentation so easily can understand what will be creating in backend VPC, subnet , nat , gateway, public ip , private ip, eip etc. https://docs.aws.amazon.com/eks/latest/userguide/creating-a-vpc.html
- In this we are going to setup 2 public subnet(EC2) and 2 private subnet (EKS)

2). Create Stack (CloudFormation)

- Open the AWS CloudFormation console at  https://console.aws.amazon.com/cloudformation.
- Make sure region is correct and then select create stack.
- Select Amazon S3 URL. and paste it https://s3.us-west-2.amazonaws.com/amazon-eks/cloudformation/2020-10-29/amazon-eks-vpc-sample.yaml  - u can check by open in text editor
- Just give name and no need to change anything next and create.

3). Create EKS cluster

- Open EKS page in aws and create start name properly for eks cluster setup
- Always use default k8s version. 
- Select Iam role which we create in step 1 
- Select endpoint as both public and private
-  next and leave as default overview all and create.
- Create Ec2 instance as k8s server label.
- Now install kubectl into this procedure mention in files follow this dont apply kubeadm into this.
- Check $ kubectl get pod  - it gives error that server refused.
- Now we need to add kube-config file into this instace before this install aws cli into instance follow this docs.- https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
 if unzip error install by $ sudo apt install unzip -y
 Now we have to access kubernetes server(EKS) we can to access our aws from any instance but for this we cant provide master access directly we will provide by security key
 - go to security credentials select Access key(ID and secret key) create new key and download/save 
 go to instance terminal and run commands as follow -
   >* $ aws configure 
   >* $ # provide Access key  and Secret Access Key 
   >* $ ap-south-1  # insert region correct  
   >* o/p format $  table  
    verify by run cmd >* $ aws eks list-clusters

- Now config server by following command 
> - aws eks update-kubeconfig --name < ClusterName> --region < regionName>
 * aws will auto collect required things and server setup will be create/Done
> $ aws eks help

3). Create Iam role(For worker to fetch server)
- create role Use Case => EC2
- Add below policy as it is.
   > AmazonEKSWorkerNodePolicy     
   > AmazonEKS_CNI_Policy       
   > Amazon_EC2ContainerRegistryReadOnly
   you can copy paste in search  make name with node/worker.
  

4). Install Cluster(Worker Nodes)
- Go to eks page select cluster and select Compute => Add node Group
- name with worker 
- select above created iam role.
- Ami type - linux
- capacity - on demand
- Instance type - select as per usage make sure it will create replica with same.
- Disk size also as per requirements

- Node Group scalling
  Minimum =2   * how many node u want to start     
  maximum = 2  * max size can increase         
  desired  = 2   * in ready state
   
- how many unavailable =1

- in subnet selection u can choose all or public subnet only both will work
- u can allow ssh it may be required if want to access node.
- After this created items- Auto scalling group , load balancer , instances , security groups, eip allocate to instances.