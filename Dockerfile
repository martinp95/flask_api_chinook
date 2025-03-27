FROM python:3.12-slim

# Set work directory
WORKDIR /code

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y build-essential

# Copy dependencies file and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Set PYTHONPATH to allow package-based imports
ENV PYTHONPATH=/code

# Run the app (via docker-compose)
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
