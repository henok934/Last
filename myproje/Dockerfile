# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app


# Install chromium and its dependencies
RUN apt-get update && apt-get install -y \
    libsystemd-dev \
    libudev-dev

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run the application
CMD ["python3", "manage.py", "runserver"]
