import os

import uvicorn
from fastapi import FastAPI, HTTPException
import boto3
from botocore.exceptions import NoCredentialsError
from video2x.tests.test_upscaler import test_upscaling

app = FastAPI()

S3_BUCKET_NAME = "trans-world-style"
AWS_ACCESS_KEY = "AKIA4NJHVZKRCWWUG5KJ"
AWS_SECRET_KEY = "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"

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)


def download_file_from_s3(key):
    os.makedirs(os.path.dirname(key), exist_ok=True)
    try:
        s3.download_file(Bucket=S3_BUCKET_NAME, Key=key, Filename=key)
        return True
    except NoCredentialsError:
        return False


def upload_file_to_s3(key):
    os.makedirs(os.path.dirname(key), exist_ok=True)
    try:
        s3.upload_file(Filename=key, Bucket=S3_BUCKET_NAME, Key=key)
        return True
    except NoCredentialsError:
        return False


def process_file(key):
    # Placeholder for AI processing
    new_key = 'output/' + key.split('/')[-1]
    print("-----------------------------")
    print(f'new_key: {new_key}')
    try:
        test_upscaling(key, new_key, 1080)
    except Exception as e:
        print(e)
    return new_key


@app.post("/process_video")
def process_video(key: str):
    download_successful = download_file_from_s3(key)
    if not download_successful:
        raise HTTPException(status_code=500, detail="S3 download failed")

    new_key = process_file(key)

    upload_successful = upload_file_to_s3(new_key)
    if not upload_successful:
        raise HTTPException(status_code=500, detail="S3 upload failed")

    return {"status": "successful"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
