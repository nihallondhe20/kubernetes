


In IAM role you need to create eks policy 
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "eksadministrator",
            "Effect": "Allow",
            "Action": "eks:*",
            "Resource": "*"
        }
    ]
}

using this u can access iam role 

commands:
  - export AWS_ACCESS_KEY_ID=$TF_VAR_AWS_ACCESS_KEY_ID
  - export AWS_SECRET_ACCESS_KEY=$TF_VAR_AWS_SECRET_ACCESS_KEY

for installing terraform google it
