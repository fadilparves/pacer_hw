# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the scheduler.py file into the container
COPY etl_pipeline/. .

# Copy the .env file into the container
COPY .env .

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Set the command to run the scheduler.py script
CMD ["python", "scheduler.py"]
