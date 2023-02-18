FROM python:3.9-slim-buster

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir geopy

CMD ["python", "GeoIP.py"]
