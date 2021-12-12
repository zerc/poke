FROM python:3.8.12-alpine3.14 AS poke-service
ENV SERVER_HOST=0.0.0.0
ENV SERVER_PORT=8080
EXPOSE 8080

COPY requirements.txt /app/requirements.txt
COPY app.py /app/app.py
COPY providers /app/proviers/

RUN apk update && \
    apk add --no-cache --virtual .build-deps build-base libc-dev gcc>9 openssl-dev~=1.1 && \
    pip install --no-cache-dir -r /app/requirements.txt && \
    addgroup -g 1000 app && adduser -u 1000 -G app -s /bin/sh -D app

WORKDIR /app
USER app
CMD ["python", "app.py"]

FROM poke-service AS poke-tests
COPY requirements.test.txt /app/requirements.test.txt
COPY tests /app/tests/
RUN pip install --no-cache-dir -r /app/requirements.test.txt
