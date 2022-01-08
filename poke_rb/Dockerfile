FROM ruby:2.7.5-alpine3.15
EXPOSE 8080

COPY Gemfile /app/Gemfile
COPY *.rb /app/

RUN apk update && \
    apk add --no-cache --virtual .build-deps build-base libc-dev gcc>9 openssl-dev~=1.1 && \
    addgroup -g 1000 app && adduser -u 1000 -G app -s /bin/sh -D app

WORKDIR /app
RUN bundle install
USER app

CMD ["ruby", "app.rb", "-p", "8080", "-o", "0.0.0.0"]
