# 🏗️ **Stage 1: Build Stage (Temporary, Not in Final Image)**
FROM python:3.9 AS builder

# Set working directory
WORKDIR /app

# Copy only requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining application files
COPY . .

# 🏗️ **Stage 2: Final Lightweight Image**
# Smaller base image
FROM python:3.9-alpine  

WORKDIR /app

# Install Python packages (IMPORTANT: Copy site-packages correctly)
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Copy application files
COPY --from=builder /app /app

# Use the correct Python binary in Alpine
CMD ["python3", "app.py"]