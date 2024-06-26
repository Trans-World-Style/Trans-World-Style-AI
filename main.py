import multiprocessing
import os

import uvicorn
from fastapi import FastAPI, HTTPException
import boto3
from botocore.exceptions import NoCredentialsError
from video2x.tests.test_upscaler import test_upscaling

app = FastAPI()

# S3_BUCKET_NAME='trans-world-style'
# AWS_ACCESS_KEY='AKIA4NJHVZKRCWWUG5KJ'
# AWS_SECRET_KEY='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'

S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

task_running = False
temp_file_name = 'temp.mp4'

def download_file_from_s3(key):
    global temp_file_name
    os.makedirs(os.path.dirname(key), exist_ok=True)
    try:
        s3.download_file(Bucket=S3_BUCKET_NAME, Key=key, Filename=temp_file_name)
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


def process_file(key, new_key):
    global temp_file_name
    # Placeholder for AI processing
    try:
        test_upscaling(input_url=temp_file_name, output_url=new_key, height=1080)
    except Exception as e:
            print(e)
    return new_key


@app.post("/upscale_video", include_in_schema=False)
def process_video(key: str):
    global task_running
    task_running = True
    import time
    st = time.time()

    download_successful = download_file_from_s3(key)
    if not download_successful:
        task_running = False
        return HTTPException(status_code=500, detail="S3 download failed")

    new_key = 'output/' + key.split('/')[-1]
    try:
        # process_file(key, new_key)
        video_process = multiprocessing.Process(target=process_file, args=(key, new_key,))
        video_process.start()
        video_process.join()
    except Exception as e:
        print(e)

    upload_successful = upload_file_to_s3(new_key)
    if not upload_successful:
        task_running = False
        return HTTPException(status_code=500, detail="S3 upload failed")

    print(f'api running time: {time.time() - st}')
    task_running = False
    return {"status": "successful", "result": new_key}

@app.get("/readiness")
def readiness():
    if task_running:
        raise HTTPException(status_code=500, detail="Task is running")
    return {"status": "ready"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
