Monolithic vs Microservices architecture.

Monolithic--*

If all the functionalities of a project exist in a single codebase, then that application is known as a monolithic application. We design our application in various layers like presentation, service, and persistence and then deploy that codebase as a single jar/war file. This is nothing but a monolithic application, where “mono” represents the single codebase containing all the required functionalities. 

Disadvantages of Monolithic applications: 

It becomes too large with time and hence, difficult to manage.
As the size of the application increases, its start-up and deployment time also increases.
Even if a single part of the application is facing a large load/traffic, we need to deploy the instances of the entire application in multiple servers. It is very inefficient and takes up more resources unnecessarily. Hence, horizontal scaling is not feasible in monolithic applications.

-------------------------------------------------------------------------------------------------------------

Microservices--*

Microservices are an architectural and organizational approach to software development where software is composed of small independent services that communicate over well-defined APIs

https://enonic.com/blog/what-are-microservices/_/image/398d9cfa-912e-4402-9d34-d3f68f6e74f6:76de5eb4dc2e3a89dd2dada5d8ca2bcb5ee56ad3/width-768/Microservices.gif

https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-microservices/images/aks.png

Advantages of microservices:  

If there’s any update in one of the microservices, then we need to redeploy only that microservice.
Microservices are self-contained and, hence, deployed independently. Their start-up and deployment times are relatively less.
If a particular microservice goes down due to some bug, then it doesn’t affect other microservices and the whole system remains intact and continues providing other functionalities to the users.

----------------------------------------------------------------------------------------------------------------

Steps for Migrating Monolithic Application to Microservices

1. Identify Logical Components
2. Flatten and Refactor Components
3. Identify Component Dependencies
4. Identify Component Groups
5. Create an API for Remote User Interface
6. Migrate Component Groups to Macroservices
7. Migrate Macroservices to Microservices
8. Deployment and Testing.

---------------------------------------------------------------------------------------------------------------

Microservice Architecture Components

1) Cloud Provider (AWS,GCP,Azure)

2) Docker (Container provider )

3) Kubernetes Service (Container orchestration tools)

4) Nginx Loadbalancer (Internal Routing)

5) Ingress -part of kubernetes (Path based routing)

6) EC2 Instances T2.Medium and 2 t2.small for manuall/automatci cluster 

7) EFS (part of aws to store data of microservice PV & PVC)

8) Route53 (Domain Routing)

9) ELB (part of aws external(Application) load balancing )

10) Docker Hub account for create store and access docker images.
