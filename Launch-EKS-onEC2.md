# Install kubernetes on EC2 
Prerequisite:
==========

1 - Ubuntu Serves

2 - Manager  (4GB RAM , 2 Core) t2.medium

3 - Workers  (1 GB, 1 Core)     t2.micro

# Steps 

-  First, login as ‘root’ user because the following set of commands need to be executed with ‘sudo’ permissions.

* Install Required packages and apt keys.
1. Update the apt package index and install packages needed to use the Kubernetes apt repository:
 > sudo apt-get update         
>  sudo apt-get install -y apt-transport-https ca-certificates curl

2. Download the Google Cloud public signing key:
  > sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg

3. Add the Kubernetes apt repository:
  > echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list

4. Update apt package index, install kubelet, kubeadm and kubectl, and pin their version:

 > sudo apt-get update           
 > sudo apt-get install -y kubelet kubeadm kubectl      
 > sudo apt-mark hold kubelet kubeadm kubectl        

5. Turn Off Swap Space
   > swapoff -a
   > sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab

6.  Install And Enable Docker
     > apt install docker.io -y       
     > usermod -aG docker ubuntu         
     > systemctl restart docker         
     > systemctl enable docker.service

7.  Install kubeadm, Kubelet And Kubectl       

    > apt-get install -y kubelet kubeadm kubectl kubernetes-cni
8.   Enable and start kubelet service
     
     >  systemctl daemon-reload                
     >  systemctl start kubelet              
     >  systemctl enable kubelet.service           

*  Now all Changes are done you can config check by using following command
      >  kubectl get nodes                  
      >  kubectl get pod                 
      >  kubectl get all         
      >  kubectl get pods -o wide --all-namespaces


IF used terraform follow this steps

1) install kubectl 
2) install aws-cli using ---  
     curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
     unzip awscliv2.zip
    sudo ./aws/install
3) now check aws-cli and configure aws credentials again to access cluster if not access----
4)      # aws configure
5)      now final work add kube/config file defaultly using ---  aws eks update-kubeconfig --name terraform-eks-demo --region us-east-1
6)      check node and delete if required !!!!!!!!


