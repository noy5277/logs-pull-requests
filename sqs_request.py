import boto3
import os
import sys
import json
import requests
from boto3.session import  Session

access_key_id = os.getenv("AWS_ACCESS_KEY")
secret_key = os.getenv("AWS_SECRET_KEY")
session = Session(aws_access_key_id=access_key_id,
                  aws_secret_access_key=secret_key,
                  region_name='us-west-2')

pr_number = os.getenv("PR_NUMBER")
github_token = os.getenv("GITHUB_TOKEN")
github_repo = os.getenv("GITHUB_REPOSITORY")


def trigger_lambda_sqs_message():
    try:
        print(f"Logging pull request number:{pr_number}")
        url = f'https://api.github.com/repos/{github_repo}/pulls/{pr_number}/files'
        headers = {
            'Authorization': f'token {github_token}',
            'Accept': 'application/vnd.github.v3+json',
        }
        changed_files = ''
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            changed_files = response.json(filename)
        
        files = {}
        for file in changed_files:
            files.update({ f'{file["filename"]}': f'{file["status"]}' })
        message = {
            "repository_name" : f'https://github.com/{github_repo}',
            "changed_files" : files
        }
        message_json = json.dumps(message, indent=4)
        sqs = session.client('sqs',region_name='us-west-2')
        queue_url = 'https://sqs.us-west-2.amazonaws.com/622395351311/pr-trigger'
        sqs_response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=changed_files,
            DelaySeconds=5
        )
        print(f"Message ID: {sqs_response['MessageId']}")
        # else:
        #     print("No new pull request created")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        sys.exit(1)
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        sys.exit(1)
    except boto3.exceptions.Boto3Error as boto_err:
        print(f"Boto3 error occurred: {boto_err}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

trigger_lambda_sqs_message()
