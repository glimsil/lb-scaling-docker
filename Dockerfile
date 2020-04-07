FROM python:3.7-slim

WORKDIR /app

COPY . /app
RUN apt-get update && \
    apt-get install -y build-essential gcc libpq-dev && \
    pip install -r requirements.txt

EXPOSE 80
ENV NAME World
ENTRYPOINT python app.py