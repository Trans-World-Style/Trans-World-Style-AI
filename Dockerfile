FROM dodo133/tws-video2x:env

ENV S3_BUCKET_NAME=trans-world-style
ENV AWS_ACCESS_KEY=AKIA4NJHVZKRCWWUG5KJ
ENV AWS_SECRET_KEY=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

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

RUN apt-get update && apt-get install -y git

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the command to start uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker run --gpus all -itd --name ai_container -v $PWD:/app -p 12531:8000 ai_image