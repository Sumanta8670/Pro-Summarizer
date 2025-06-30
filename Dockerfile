FROM python:3.14-rc-alpine

# Use apk to install awscli and required dependencies
RUN apk update && apk add --no-cache aws-cli

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
