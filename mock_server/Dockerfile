FROM golang:1.17-alpine

WORKDIR /app

COPY go.mod ./
COPY *.go ./
COPY mocks ./

RUN go build -o /server . && ls -l

CMD ["/server"]
