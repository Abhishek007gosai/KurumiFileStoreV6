FROM python:3.10-slim

# Prevent Python from writing .pyc files & enable stdout logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (modify if your project needs more)
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to use Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project
COPY . .

# Ensure start.sh is executable
RUN chmod +x start.sh

# Default command
CMD ["bash", "start.sh"]
