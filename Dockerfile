FROM python:3.8-slim-buster

WORKDIR /endpoint-dockerized

COPY . .
RUN pip install flask

CMD ["python3", "rest.py"]
