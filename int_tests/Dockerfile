FROM python:3.8.12-alpine3.14

WORKDIR /app
COPY requirements.txt ./
COPY *.py ./

RUN apk update && \
    apk add --no-cache --virtual .build-deps build-base libc-dev gcc>9 openssl-dev~=1.1 && \
    pip install --no-cache-dir -r /app/requirements.txt && \
    addgroup -g 1000 app && adduser -u 1000 -G app -s /bin/sh -D app

USER app
CMD ["python", "-m", "pytest", "."]
