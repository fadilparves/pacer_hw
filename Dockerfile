# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the Django project code into the container
COPY . .

# Set environment variables if needed
ENV DJANGO_SETTINGS_MODULE=pacer_hw.settings

# Expose the port that Django runs on (default is 8000)
EXPOSE 8000

# Set the command to run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
