# Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# --no-cache-dir to prevent pip from storing cache in the image
# --upgrade pip to ensure pip is up-to-date
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Cloud Run sets the PORT environment variable.
# Your application should listen on this port.
# We'll use 8000 as a fallback for local testing.
ENV PORT 8080

# Command to run the application using Uvicorn
# The --host 0.0.0.0 makes the server accessible from outside the container
# The --port "$PORT" uses the environment variable set by Cloud Run (or default 8080)
# "main:app" refers to the `app` object in `main.py`
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
