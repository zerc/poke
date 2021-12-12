# Poke service

## How to run

```shell
docker compose up poke
```

after that, you can query the serivice like this:

```shell
http http://127.0.0.1:8080/pokemon/mewtwo
```

or 

```shell
http http://127.0.0.1:8080/pokemon/translated/mewtwo
```

To run tests:

```shell
docker compose up poke-test
```


## Production API notes

### Python specific

To run this app in production, one would use something like Nginx + UWSGI/Gunicorn to allow concurrent requests. The current implementation uses the development server and can only run one request at a time and does not support pool connections or buffering.

### Design simplifications

#### Caching

For GET requests to the Pokeapi service, I used a simple in-memory LRU cache - the data is unlikely to change frequently and using caching would improve the performance significantly. However, this specific implementation of the cache has 2 issues:

* it doesn't support TTL i.e. it will be in memory until the process killed
* it's not shared between processes/containers i.e. each of them would have its own copy

For production, I would use something like Redis for caching.

#### Errors handling

Not implemented i.e. if one of the third-party services returns an error or there is a networking error happens our API would return 500. In production implementation, I would, for example, attempt to automatically retry networking errors. Also, I would add more verbose error messages to my end-users with different error codes to make it clear what's happened.

#### Testing

I only implemented unit tests. In production, depending on the importance of this logic, I may consider adding integrational tests. I would have a simple web server that would emulate third-party APIs behaviour for specific request-response and my test code would do requests against it. This way I would be able to test how different pieces of my application work together.
