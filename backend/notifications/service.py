import os
import boto3
from botocore.exceptions import BotoCoreError, ClientError

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")


def send_email_ses(subject: str, body_text: str, to_addresses: list[str]) -> bool:
    ses = boto3.client("ses", region_name=AWS_REGION)
    try:
        ses.send_email(
            Source=os.getenv("DEFAULT_FROM_EMAIL", "noreply@example.com"),
            Destination={"ToAddresses": to_addresses},
            Message={
                "Subject": {"Data": subject, "Charset": "UTF-8"},
                "Body": {"Text": {"Data": body_text, "Charset": "UTF-8"}},
            },
        )
        return True
    except (BotoCoreError, ClientError):
        return False