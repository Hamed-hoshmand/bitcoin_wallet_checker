# Base Image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY app/ /app/

# Run Celery worker
CMD ["celery", "-A", "tasks.celery_app", "worker", "--loglevel=info"]
