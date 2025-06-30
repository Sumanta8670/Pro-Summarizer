FROM python:3.14-rc-alpine

# Use apk to install awscli and required dependencies
RUN apk update && apk add --no-cache \
    build-base \
    libffi-dev \
    musl-dev \
    gcc \
    g++ \
    python3-dev \
    openblas-dev \
    aws-cli
    
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
