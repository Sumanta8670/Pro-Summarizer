# Pro-Summarizer
Pro-Summarizer is an intelligent text summarization tool powered by advanced Natural Language Processing (NLP) techniques. It takes lengthy pieces of text and condenses them into concise, coherent summaries — making information easier to digest and retain.
# WorkFlows
1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the app.py

# How to run?
### STEPS:

clone the repository

```bash
https://github.com/Sumanta8670/Pro-Summarizer
```
### Step 01:- Create a virtual environment after opening the repository

```bash
conda create -n summary python=version -y
python -m venv(virtual environment name) env
```
### Step 02:- Activate the virtual environment
```bash
conda activate summary
source venv/Scripts/activate or source venv/bin/activate
```
### Step 03:- Install the required packages
```bash
pip install -r requirements.txt
```
### Step 04:- Run the following command
```bash
python app.py
```
### Step 05:- Open the browser and navigate to http://localhost:portnumber
```bash
http://localhost:customportnumber or available 8080
```
````bash
Author: Sumanta Jana
Email: sumanta8670@gmail.com
````
# AWS-CI/CD-Deployment-with-github-Actions

## 1. Login to AWS console

## 2. Create a new IAM user for deployment with specific access

    1. EC2 access: It is virtual machine
    2. ECR: Elastic container registry to save your docker image in AWS

    # Description: About the deployment

    1. Build Docker image of the source code
    2. Push the Docker image to ECR
    3. Launch your EC2
    4. Pull your image from ECR in EC2
    5. Launch your docker image in EC2

    # Policy:

    1. AmazonEC2ContainerRegistryFullAccess
    2. AmazonEC2FullAccess
    
## 3. Create a ECR repository to store/save docker image
    - Save the URI: 342130852425.dkr.ecr.us-east-1.amazonaws.com/prosummarizer

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and install docker in EC2 machine :

    #(OPTIONAL)

    sudo apt-get update -y
    sudo apt-get upgrade

    #REQUIRED
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker

### Step 06:- Configure EC2 as self-hosted runner:

    setting>actions>runner>new self hosted runners> choose os> then run command one by one

### Step 07:- Setup github secrets:

    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY=
    AWS_REGION=us-east-1
    AWS_ECR_LOGIN_URI=demo>> value.dkr.ecr.us-east-1.amazonaws.
    com
    ECR_REPOSITORY_NAME=simple-app