FROM python:3.12-slim-buster

# Install system packages
RUN apt-get update && apt-get install -y awscli && apt-get clean

# Set working directory
WORKDIR /app

# Copy code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
