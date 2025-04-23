# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DISPLAY=host.docker.internal:0

# Install system dependencies (including tkinter)
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default command (change main.py to your actual entry point)
CMD ["python", "main.py"]