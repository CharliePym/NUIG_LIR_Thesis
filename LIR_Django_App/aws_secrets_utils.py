# method to get secrets from AWS Secrets Manager

import boto3
from botocore.exceptions import ClientError
import json

def get_LIR_secrets() -> dict:

    secret_name = "LIR_secrets"
    region_name = "eu-west-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']
    
    # return secrets dict
    return json.loads(secret)

def  get_DB_secrets() -> dict:
    
    secret_name = "arn:aws:secretsmanager:eu-west-2:792287265845:secret:rds!db-730a82ce-d85a-4c8f-8dbf-7601d82ef681-GeVhZW"
    region_name = "eu-west-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']
    
    # return secrets dict
    return json.loads(secret)



