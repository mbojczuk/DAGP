FROM python:3.11-slim

# Create a app directory
WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App code
COPY src/ ./src

# Default command to run  a quick smoke query
CMD ["python", "-m", "src.query_trino", "--smoke"]
