FROM python:3.10-slim

# Install system dependencies including zbar
RUN apt-get update && apt-get install -y libzbar0

# Create app directory
WORKDIR /

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Run your app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
