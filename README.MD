# GitHub Pull Request Logger Service

This project demonstrates how to build a service using AWS that logs the GitHub repository name and files changed when a pull request (PR) is merged. The solution is implemented using an SQS (Simple Queue Service) queue to trigger an AWS Lambda function. The infrastructure is provisioned using Terraform, and the logic is written in Python.
Table of Contents

## Architecture Overview

    GitHub Pull Request Event: GitHub sends an event when a pull request is merged.
    SQS Queue: The event is passed into the SQS queue.
    Lambda Function: The SQS queue triggers the Lambda function, which logs the repository name and the files that were changed in the pull request.
    Terraform: All AWS resources are managed via Terraform for a fully automated deployment.

## Pre-requisites

## Before running this project, ensure you have:

    AWS account with the necessary permissions.
    GitHub repository for which the pull request events will be logged.
    Terraform installed.
    Python 3.x installed.

## Setup Instructions
### Clone the Repository

```bash
git clone https://github.com/noy5277/logs-pull-requests.git
cd logs-pull-requests
```

### Update Terraform Variables

Modify the conf.tfvars files to include your AWS region, GitHub repository details, and any other necessary configurations.

### Deploy the Infrastructure

Use Terraform to deploy the AWS resources and GitHub webhook:

```bash
terraform init
terraform apply
```

#### This will set up the following:

    An SQS queue to receive GitHub events.
    A Lambda function that is triggered by the SQS queue.
    A GitHub webhook to trigger the service on pull request merges.

### Add GitHub Secrets by terraform github provider

Ensure that your GitHub repository has the necessary secrets.
```bash
AWS_ACCESS_KEY
AWS_SECRET_KEY
CP_GITHUB_TOKEN
```
Usage

    Triggering the Service:
        When a pull request is merged in the GitHub repository, a webhook will send an event to the SQS queue.
        The SQS queue triggers the Lambda function to log the repository name and files that were changed in the PR.

    Logging:
        The Lambda function logs can be viewed in AWS CloudWatch.
        The logs will contain:
            GitHub repository name
            List of files changed in the pull request

### Testing

To test the service:

    Create a pull request in your GitHub repository.
    Merge the pull request.
    Check AWS CloudWatch logs to confirm that the repository name and changed files were logged.

### Cleanup

To clean up and remove all AWS resources created by this project, run:

```bash

terraform destroy
```

This will delete the SQS queue, Lambda function, and all other resources.