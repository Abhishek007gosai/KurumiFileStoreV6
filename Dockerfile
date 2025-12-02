FROM python:3.10-slim

# Disable Python bytecode & enable clean logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system packages (add more if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (better build caching)
COPY requirements.txt .

# Install required Python modules
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project files
COPY . .

# Make sure start.sh is executable
RUN chmod +x start.sh

# Expose port 5000 (Koyeb uses this)
EXPOSE 5000

# Start your Flask server
CMD ["bash", "start.sh"]
