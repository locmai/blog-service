FROM python:3.8.2-slim-buster

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY .env .env

COPY ./blog_service ./blog_service

CMD uvicorn blog_service.main:app --host 0.0.0.0 --port 8000