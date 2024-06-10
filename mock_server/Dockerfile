FROM golang:1.17-alpine

HEALTHCHECK --start-period=10s --retries=30 CMD curl -f http://127.0.0.1:8080/health-check  || exit 1

WORKDIR /app

COPY go.mod ./
COPY *.go ./
COPY mocks ./

RUN go build -o /server . && ls -l

CMD ["/server"]
